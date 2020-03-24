import pandas as pd
import os
from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.layouts import row
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import Legend


import bokeh.palettes as palettes



def generate_plot(x_axis, array_of_y_axes, array_of_line_titles, datetime_format,
                  plot_title, x_axis_label, y_axis_label, override_default_x_axis_formatting=False, x_axis_type ="datetime", plot_width=450, plot_height=400, toolbar_location= 'right',
                  TOOLS="pan,wheel_zoom,box_zoom,reset, save, hover", x_range=None, y_range=None, x_axis_visible=True, legend_location='top_right'):
    p = figure(plot_width = plot_width, plot_height=plot_height, x_axis_type=x_axis_type, tools=TOOLS, toolbar_location=toolbar_location, x_range=x_range, y_range=y_range)
    p.y_range.start = 0

    p.title.text = plot_title
    p.xaxis.axis_label = x_axis_label
    p.yaxis.axis_label = y_axis_label
    p.xaxis.visible = x_axis_visible

    if not override_default_x_axis_formatting:
        x_axis = pd.to_datetime(
            arg=x_axis,
            format=datetime_format
        )
    colors = palettes.viridis(len(array_of_y_axes))
    index = 0


    legend_items = []

    for y_axis, line_color, legend_name in zip(array_of_y_axes, colors, array_of_line_titles):
        lines = {
            'x':x_axis,
            'y':y_axis
        }
        df = pd.DataFrame(data=lines)
        line = p.line(df['x'], df['y'], line_width=2, alpha=0.8, color=line_color, legend=legend_name)
        index += 1
        legend_items.append((legend_name, [line]))


    p.legend.location = legend_location
    try:
        p.legend.click_policy = "hide"
    except:
        print("Graph Produced for Python2") #Find a fix to this problem where cannnot hide lines in py 2.7

    output_file("GraphOutput" + ".html", title="Simulation Output Graphs")

    return p


def get_components(plot):
    return components(plot)

def column_join(plots):
    return column(*plots)

def row_join(plots):
    return row(*plots)

def display_plot(plots):
    """
    Plots the CO2 Concentrations of all conducted simulations with respect to time from the start date of
    simulation
    """

    show(column(*plots))
