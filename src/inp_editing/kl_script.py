
"""Read gds file and export black white image."""

from pathlib import Path
import pya

gds_path=str(Path(__file__).parent.parent.parent / "PNL.gds")
output_path=str(Path(__file__).parent.parent.parent / "bw9.png")

layout_view = pya.LayoutView()
layout_view.load_layout(gds_path)
layout_view.max_hier() 
layout_view.set_config("background-color", "#ffffff")
layout_view.set_config("grid-show-ruler", "false")
layout_view.set_config("grid-visible", "false")

for lyp in layout_view.each_layer():
    lyp.fill_color = 0
    lyp.frame_color = 0
    lyp.dither_pattern = 0
    if lyp.layer_index() in [4]:
        lyp.visible = False

layout_view.update_content()
screenshot = layout_view.get_image(1000, 1000)
screenshot.save(output_path, "PNG", -1)
# screenshot = layout_view.get_screenshot()
# screenshot.save(output_path, "PNG", -1)
# layout_view.zoom_fit()  # not working
# app.process_events()
# layout_view.save_image(output_path, 2000, 2000)
