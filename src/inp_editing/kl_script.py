
"""Read gds file and export black white image."""

from pathlib import Path
import pya

gds_path=str(Path(__file__).parent.parent.parent / "PNL.gds")
output_path=str(Path(__file__).parent.parent.parent / "bw6.png")
app = (
    pya.Application.instance()
)  # TODO: FIXME module 'pya' has no attribute 'Application'
mw = app.main_window()

mw.load_layout(gds_path, 2)
# mw.current_layout()

layout_view = mw.current_view()  
for lyp in layout_view.each_layer():
    lyp.fill_color     = 0
    lyp.frame_color    = 0
    lyp.dither_pattern = 0

    # print(lyp.layer_index)

    # # Set the visibility of the layer (True for visible, False for invisible)
    # layer_info.visible = False  # Make the layer invisible
    if lyp.layer_index() == 4:
        lyp.visible = False
# screenshot = layout_view.get_screenshot()
# screenshot.save(output_path, "PNG", -1)
# layout_view.zoom_fit()  # not working
app.process_events()
layout_view.save_image(output_path, 2000, 2000)
