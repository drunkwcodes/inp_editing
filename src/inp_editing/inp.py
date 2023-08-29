import itertools
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, List, Tuple

from PIL import Image

from inp_editing.models import Node, init_db, node_id


def find_project_root(cwd: str = ".", max_depth: int = 10) -> str | None:
    """Recursively find a `pyproject.toml` at given path or current working directory.
    If none if found, go to the parent directory, at most `max_depth` levels will be
    looked for.
    """
    original_path = Path(cwd).absolute()
    path = original_path
    for _ in range(max_depth):
        # print(path)
        if path.joinpath("pyproject.toml").exists():
            # return path.as_posix()
            return path
        if path.parent == path:
            # Root path is reached
            break
        path = path.parent
    return None


# @dataclass
# class Node:
#     x: float
#     y: float
#     z: float
#     no: int | None = None
#     id_iter = itertools.count(start=1)

#     def __post_init__(self):
#         if self.no is None:
#             self.no = next(self.id_iter)

#     def __hash__(self):
#         return self.no


# def node_no(nodes: list[Node], x, y, z) -> int | None:
#     for node in nodes:
#         if node.x == x and node.y == y and node.z == z:
#             return node.no
#     return None


@dataclass
class Material:
    name: str
    density: float | None = None
    elastic: tuple[float, float] | None = None
    conductivity: float | None = None
    specific_heat: float | None = None
    expansion: float | None = None


@dataclass
class Layer:
    name: str
    thickness: float
    material_type: Material | None = None
    thickness_unit: str = "MM"


@dataclass
class Element:
    nodes: List[Node]
    grayscale: int = 255
    no: int | None = None
    material: Material | None = None
    id_iter = itertools.count(start=1)

    def __post_init__(self):
        if self.no is None:
            self.no = next(self.id_iter)


copper_fr4 = Material(
    name="Copper_FR4_O_0",
    density=1.90000e-09,
    elastic=(2.47640e04, 1.50000e-01),
    conductivity=2.00000e-01,
    specific_heat=1.38600e09,
    expansion=1.70810e-05,
)

fr4 = Material(
    name="FR4",
    elastic=(2.47640e04, 1.50000e-01),
    density=1.90000e-09,
    expansion=1.70810e-05,
    conductivity=2.00000e-01,
    specific_heat=1.38600e09,
)

layer_fr4 = Layer(
    name="FR4",
    thickness=0.1,
    material_type=fr4,
)

layer_copper = Layer(
    name="Copper",
    thickness=0.1,
    material_type=copper_fr4,
)


def generate_element(
    x, y, z_top, z_bottom, grayscale, material: Material
) -> Tuple[Element, list[Node]]:
    n1 = Node.get_or_create(x=x, y=y, z=z_bottom)[0]
    n2 = Node.get_or_create(x=x + 1, y=y, z=z_bottom)[0]
    n3 = Node.get_or_create(x=x + 1, y=y + 1, z=z_bottom)[0]
    n4 = Node.get_or_create(x=x, y=y + 1, z=z_bottom)[0]

    n5 = Node.get_or_create(x=x, y=y, z=z_top)[0]
    n6 = Node.get_or_create(x=x + 1, y=y, z=z_top)[0]
    n7 = Node.get_or_create(x=x + 1, y=y + 1, z=z_top)[0]
    n8 = Node.get_or_create(x=x, y=y + 1, z=z_top)[0]

    nodes = [n1, n2, n3, n4, n5, n6, n7, n8]
    assert isinstance(nodes, list), type(nodes)
    for node in nodes:
        assert isinstance(node, Node), type(node)

    return (
        Element(
            nodes=nodes,
            material=material,
            grayscale=grayscale,
        ),
        nodes,
    )


def generate_element_by_layers(
    x, y, layers: list[Layer], grayscale: int
) -> Tuple[list[Element], list[Node]]:
    # The first layer is the bottom layer, the last layer is the top layer, z is the thickness
    zs = [0]
    for layer in layers:
        zs.append(zs[-1] + layer.thickness)
    elements = []
    nodes = []
    for lindex, layer in enumerate(layers):
        element, ns = generate_element(
            x,
            y,
            z_top=zs[lindex + 1],
            z_bottom=zs[lindex],
            grayscale=grayscale,
            material=layer.material_type,
        )
        # print(f"{total_nodes = }")

        # z_top = zs[lindex + 1]
        # z_bottom = zs[lindex]

        # element = Element(
        #     nodes=nodes,
        #     material=layer.material_type,
        #     grayscale=grayscale,
        # )
        # elements.append(element)
        # print(f"{total_nodes = }")
        assert isinstance(element.nodes, list), type(element.nodes)
        for node in element.nodes:
            assert isinstance(node, Node), type(node)
        elements.append(element)
        nodes += ns

    # total_nodes = list(set(total_nodes))
    return elements


@dataclass
class Elset:
    name: str
    elements: list[Element]

    def dump(self):
        lines = [f"*Elset, elset={self.name}"]

        line = " "
        for element in self.elements:
            line += f"{element.no},"
            if len(line) > 88:
                lines.append(line)
                line = " "
        return lines


@dataclass
class Orientation:
    name: str
    strings: list[str]

    def dump(self):
        lines = [f"*Orientation, name={self.name}"]
        lines += self.strings
        return lines


ori1 = Orientation(name="Ori-1", strings=["1., 0., 0., 0., 1., 0.", "3, 0."])

# ** Section: FR4
# *Solid Section, elset=Set-FR4, orientation=Ori-1, material=FR4
# ,


@dataclass
class Section:
    name: str
    elset: Elset
    orientation: Orientation
    material: Material

    def dump(self):
        # *Elset, elset=Set-FR4
        # 2,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,
        # 50,53,56,59,
        # ** Section: FR4
        # *Solid Section, elset=Set-FR4, orientation=Ori-1, material=FR4
        # ,

        # dump elset first
        lines = self.elset.dump()
        lines += [f"** Section: {self.name}"]
        lines += [
            f"*Solid Section, elset={self.elset}, orientation={self.orientation.name}, material={self.material.name}"
        ]
        lines += [","]
        return lines


@dataclass
class Inp:
    heading: str | Path  # inp file path
    nodes: list[Node] | None = None
    elements: list[Element] | None = None
    materials: list[Material] | None = None
    sections: list[Section] | None = None
    elsets: list[Elset] | None = None

    # TODO: mysterious attributes
    # *Orientation, name=Ori-1
    # *Elset, elset=Set-Copper_FR4_O_0

    def dump_heading(self):
        lines = ["*Heading", str(self.heading)]
        return lines

    def dump_nodes(self):
        if self.nodes is None:
            return []
        lines = ["*NODE"]
        for node in self.nodes:
            lines.append(f"{node.id}, {node.x}, {node.y}, {node.z}")
        if self.nodes:
            return lines

    def dump_elements(self):
        if self.elements is None:
            return []
        lines = ["*ELEMENT, type=C3D8I, ELSET=Volume1"]
        for element in self.elements:
            line = f"{element.no}, "
            for node in element.nodes:
                line += f"{node.id}, "
            line.rstrip(", ")
            lines.append(line)
        return lines

    def dump_materials(self):
        if self.materials is None:
            return []
        lines = ["** MATERIALS", "**"]

        for material in self.materials:
            lines.append(f"*Material, name={material.name}")
            if material.density:
                lines.append("*density")
                lines.append(f" {material.density:.5e}")
            if material.elastic:
                lines.append("*elastic")
                lines.append(f" {material.elastic[0]:.5e},{material.elastic[1]:.5e}")
            if material.conductivity:
                lines.append("*Conductivity")
                lines.append(f"{material.conductivity:.5e}")
            if material.specific_heat:
                lines.append("*Specific Heat")
                lines.append(f"{material.specific_heat:.5e}")
            if material.expansion:
                lines.append("*expansion")
                lines.append(f" {material.expansion:.5e}")
        return lines

    def dump_sections(self):
        """Includes elset and section."""
        # ** Section: FR4
        # *Solid Section, elset=Set-FR4, orientation=Ori-1, material=FR4
        # ,
        if self.sections is None:
            return []
        lines = []
        for section in self.sections:
            lines += section.dump()
        return lines

    def write(self):
        with open(self.heading, "w", encoding="utf-8") as f:
            f.writelines(line + "\n" for line in self.dump_heading())
            f.writelines(line + "\n" for line in self.dump_nodes())
            f.writelines(line + "\n" for line in self.dump_elements())
            f.writelines(line + "\n" for line in self.dump_sections())
            f.writelines(line + "\n" for line in self.dump_materials())


def main():
    test_inp = Inp(
        heading=r"D:\projects\inp_editing\test.inp",
        materials=[copper_fr4, fr4],
    )
    n1 = Node(0, 0, 0)
    n2 = Node(1, 0, 0)
    n3 = Node(1, 1, 0)
    n4 = Node(0, 1, 0)

    n5 = Node(0, 0, 1)
    n6 = Node(1, 0, 1)
    n7 = Node(1, 1, 1)
    n8 = Node(0, 1, 1)

    n9 = Node(0, 0, 2)
    n10 = Node(1, 0, 2)
    n11 = Node(1, 1, 2)
    n12 = Node(0, 1, 2)

    e1 = Element([n1, n2, n3, n4, n5, n6, n7, n8], grayscale=255)
    e2 = Element([n5, n6, n7, n8, n9, n10, n11, n12])
    test_inp.nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]

    test_inp.elements = [e1, e2]
    test_inp.write()


def read_bmp_and_create_elements(bmp_path="resized_100x100.bmp", thickness=0.3):
    init_db()
    test_inp = Inp(
        heading=r"D:\projects\inp_editing\test.inp",
        materials=[copper_fr4, fr4],
    )
    layers = [layer_fr4, layer_copper]

    image = Image.open(bmp_path).convert("L")  # Open and convert to grayscale
    width, height = image.size

    set_fr4 = Elset(
        name="Set-FR4",
        elements=[],
    )

    elements = []

    for y in range(height - 1):
        for x in range(width - 1):
            grayscale_values = [
                image.getpixel((x, y)),
                image.getpixel((x + 1, y)),
                image.getpixel((x + 1, y + 1)),
                image.getpixel((x, y + 1)),
            ]

            # Calculate the average grayscale value
            avg_grayscale = sum(grayscale_values) // 4

            if avg_grayscale < 255:  # Not white
                es = generate_element_by_layers(
                    x, y, layers=layers, grayscale=avg_grayscale
                )
                # start to add elements to elsets
                if avg_grayscale < 255:
                    # add to fr4 elset
                    set_fr4.elements += es
                # elif :

                # assert isinstance(es, list), type(es)
                elements += es
    section_fr4 = Section(
        name="FR4",
        elset=set_fr4,
        orientation=ori1,
        material=fr4,
    )

    test_inp.nodes = list(Node.select())
    test_inp.elements = elements
    test_inp.sections.append(section_fr4)
    test_inp.write()

    # test
    # print(f"{node_no(nodes, 26, 5, 0) = }")


if __name__ == "__main__":
    # main()
    start_time = time.time()
    read_bmp_and_create_elements(bmp_path="resized_200x200.bmp")
    end_time = time.time()

    elapsed_time = end_time - start_time

    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)

    print(f"Execution time: {hours} hours, {minutes} minutes, {seconds} seconds")
