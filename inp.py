from dataclasses import dataclass
from pathlib import Path
from typing import List, Iterator
import itertools

from PIL import Image


@dataclass
class Node: 
    x: float
    y: float
    z: float
    no: int | None = None
    id_iter = itertools.count(start=1)

    def __post_init__(self):
        if self.no is None:
            self.no = next(self.id_iter)



@dataclass
class Element:
    nodes: List[Node]
    grayscale: int = 255
    no: int | None = None
    id_iter = itertools.count(start=1)

    def __post_init__(self):
        if self.no is None:
            self.no = next(self.id_iter)





@dataclass
class Material:
    name: str
    density: float | None = None
    elastic: tuple[float, float] | None = None
    conductivity: float | None = None
    specific_heat: float | None = None
    expansion: float | None = None


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

@dataclass
class Elset:
    name: str
    elements: list[int]

    def dump(self):
        lines = [f"*Elset, elset={self.name}"]

        line = " "
        for element in self.elements:
            line += f"{element},"
            if len(line) > 88:
                lines.append(line)
                line = " "
        return lines

# TODO: Section
# ** Section: FR4
# *Solid Section, elset=Set-FR4, orientation=Ori-1, material=FR4
# ,

@dataclass
class Section:
    name: str
    elset: Elset
    orientation: str
    material: Material



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
            lines.append(f"{node.no}, {node.x}, {node.y}, {node.z}")
        if self.nodes:
            return lines

    def dump_elements(self):
        if self.elements is None:
            return []
        lines = ["*ELEMENT, type=C3D8I, ELSET=Volume1"]
        for element in self.elements:
            line = f"{element.no}, "
            for node in element.nodes:
                line += f"{node.no}, "
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
        # ** Section: FR4
        # *Solid Section, elset=Set-FR4, orientation=Ori-1, material=FR4
        # ,
        if self.sections is None:
            return []
        for section in self.sections:
            lines = [f"** Section: {section.name}"]
            lines += [
                f"*Solid Section, elset={section.elset}, orientation={section.orientation}, material={section.material.name}"
            ]
            lines += [","]
        return lines
    
    def dump_elsets(self):
        lines = []
        if self.elsets is None:
            return []
        for elset in self.elsets:
            lines += elset.dump()
        return lines

    def write(self):
        with open(self.heading, "w", encoding="utf-8") as f:
            f.writelines(line + "\n" for line in self.dump_heading())
            f.writelines(line + "\n" for line in self.dump_nodes())
            f.writelines(line + "\n" for line in self.dump_elements())
            f.writelines(line + "\n" for line in self.dump_materials())
            f.writelines(line + "\n" for line in self.dump_sections())
            f.writelines(line + "\n" for line in self.dump_elsets())


test_inp = Inp(
    heading=r"D:\projects\inp_editing\test.inp",
    materials=[copper_fr4, fr4],
)


def main():
    n1 = Node(0, 0, 0)
    n2 = Node(1, 0, 0)
    n3 = Node(1, 1, 0)
    n4 = Node(0, 1, 0)

    n5 = Node(0, 0, 1)
    n6 = Node(1, 0, 1)
    n7 = Node(1, 1, 1)
    n8 = Node(0, 1, 1)


    e1 = Element(1, [n1, n2, n3, n4, n5, n6, n7, n8], grayscale=255)
    test_inp.nodes = [n1, n2, n3, n4, n5, n6, n7, n8]

    test_inp.elements = [e1]
    test_inp.write()

def read_bmp_and_create_elements(bmp_path="resized_100x100.bmp", thickness=0.3):
    image = Image.open(bmp_path).convert("L")  # Open and convert to grayscale
    width, height = image.size

    elements = []
    nodes = []

    for y in range(height - 1):
        for x in range(width - 1):
            n1 = Node(x, y, 0)
            n2 = Node(x + 1, y, 0)
            n3 = Node(x + 1, y + 1, 0)
            n4 = Node(x, y + 1, 0)

            n5 = Node(x, y, thickness)
            n6 = Node(x + 1, y, thickness)
            n7 = Node(x + 1, y + 1, thickness)
            n8 = Node(x, y + 1, thickness)

            grayscale_values = [
                image.getpixel((x, y)),
                image.getpixel((x + 1, y)),
                image.getpixel((x + 1, y + 1)),
                image.getpixel((x, y + 1)),
            ]

            # Calculate the average grayscale value
            avg_grayscale = sum(grayscale_values) // 4

            if avg_grayscale < 255:  # Not white
                e = Element([n1, n2, n3, n4, n5, n6, n7, n8], grayscale=avg_grayscale)
                elements.append(e)
                nodes += [n1, n2, n3, n4, n5, n6, n7, n8]

    test_inp.nodes = nodes
    test_inp.elements = elements
    test_inp.write()


if __name__ == "__main__":
    # main()
    read_bmp_and_create_elements(bmp_path="resized_200x200.bmp")
