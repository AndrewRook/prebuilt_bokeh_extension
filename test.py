import os
os.environ["BOKEH_MINIFIED"] = "false"
os.environ["BOKEH_PRETTY"] = "true"

import numpy as np
import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show

from package.models import Pick

if __name__ == "__main__":
    data = pd.DataFrame({
        "x": np.arange(10),
        "y": np.arange(10) ** 2,
        "y2": np.arange(10) ** 1.5,
        "rot": np.zeros(10)
    })
    source = ColumnDataSource(data)

    plot = figure(
        height=200,
        x_range=[data["x"].min() - 1, data["x"].max() + 1],
        y_range=[data["y"].min() - 1, data["y"].max() + 1]
    )
    plot.circle(x="x", y="y", source=source)
    glyph = Pick(
        x="x",
        y="y2",
        rot="rot"
    )
    graphics = plot.add_glyph(source, glyph)

    show(plot)
