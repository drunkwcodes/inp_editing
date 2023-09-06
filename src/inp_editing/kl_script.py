
"""Read gds file and export black white image."""

from pathlib import Path
import pya

gds_path=str(Path(__file__).parent.parent.parent / "PNL.gds")
output_path=str(Path(__file__).parent.parent.parent / "bw1.png")
app = (
    pya.Application.instance()
)  # TODO: FIXME module 'pya' has no attribute 'Application'
mw = app.main_window()

mw.load_layout(gds_path, 1)
# mw.current_layout()

layout_view = mw.current_view()  
for lyp in layout_view.each_layer():
    lyp.fill_color     = 0
    lyp.frame_color    = 0
    lyp.dither_pattern = 0

layout_view.save_image(output_path, 2000, 2000)