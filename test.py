import os
os.environ["BOKEH_MINIFIED"] = "false"
os.environ["BOKEH_PRETTY"] = "true"

import pandas as pd

from ptplot import PTPlot
from ptplot.animation import Animation
from ptplot.facet import Facet
from ptplot.hover import Hover
from ptplot.nfl import Aesthetics, Field
from ptplot.plot import Positions, Tracks

from bokeh.plotting import show


if __name__ == "__main__":
    player_tracking_data = pd.read_csv(
        "notebooks/2018_CLE_2018122305_1246.tsv",
        sep="\t", parse_dates=["time"]
    )
    player_tracking_data.loc[player_tracking_data["displayName"] == "ball", "teamAbbr"] = "ball"
    player_tracking_data.loc[player_tracking_data["displayName"] == "ball", "jerseyNumber"] = ""

    # plot = (
    #     PTPlot(data=player_tracking_data, pixel_height=400) +
    #     Field(pixels_per_yard=10)
    #     + Tracks("x", "y", "displayName")
    #     + Positions(
    #         "x", "y", name="positions",
    #         number="jerseyNumber"  # , frame_filter="frame == 195"
    #     )
    #     + Aesthetics(team_ball_mapping="teamAbbr", home_away_mapping="homeTeamFlag > 0.99", ball_identifier="ball")
    #     + Animation("frame")
    #     + Hover([("name", "@displayName")], "positions", ["displayName"])
    #
    # )


    plot = (
        PTPlot(data=player_tracking_data, pixel_height=500) +
        Field()#, vertical_orientation=True)
        #+ Tracks("110 - x", "53.3 - y", "displayName", line_width=3)
        + Positions(
            "110 - x", "53.3 - y", name="positions",
            number="jerseyNumber",
            orientation="o - 180",  # , frame_filter="frame == 195"
            line_width=3
        )
        + Aesthetics(team_ball_mapping="teamAbbr", home_away_mapping="homeTeamFlag > 0.99", ball_identifier="ball")
        #+ Animation("frame", 10)
        #+ Hover([("name", "@displayName")], "positions", ["displayName"])
        #+ Facet("teamAbbr", num_col=2)

    )
    drawn_plot = plot.draw()
    show(drawn_plot)