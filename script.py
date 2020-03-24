import pandas as pd
import os
from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.layouts import row
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import Legend
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from bokeh.plotting import figure, show, output_file, output_notebook
from bokeh.palettes import Spectral11, colorblind, Inferno, BuGn, brewer
from bokeh.models import HoverTool, value, LabelSet, Legend, ColumnDataSource,LinearColorMapper,BasicTicker, PrintfTickFormatter, ColorBar
import datetime
import os
import bokeh.palettes as palettes


data = pd.read_csv("DataTable201.csv", parse_dates=['Time'])
data.head()
data.Time.min(), data.Time.max()
data.PMin.value_counts()
data['Year'] = data.Time.apply(lambda x: x.year)
data['Month'] = data.Time.apply(lambda x: x.month)
data['Day'] = data.Time.apply(lambda x: x.day)
data['Hour'] = data.Time.apply(lambda x: x.hour)
data['Minute'] = data.Time.apply(lambda x: x.minute)
data['Second'] = data.Time.apply(lambda x: x.second)
data.head()
temp_df = data.groupby(['Day']).sum().reset_index()
temp_df
# time = temp_df["Day"].values
# pmin = temp_df["PMin"].values
# print(time)
# print(pmin)

# output to static HTML file
output_file("pmin.html")

# create a new plot with a title and axis labels
plo = figure(title="pmin", x_axis_label='time', y_axis_label='pmin')

# add a line renderer with legend and line thickness
# plo.line(time, pmin, legend="Temp.", line_width=2)

# show the results
show(plo)
df = data = pd.read_csv("DataTable201.csv", parse_dates=['Time'])
df['Time'] = pd.to_datetime(df['Time'], format='%m/%d/%Y%H%M')
df


time = df["Time"].values
pmin = df["PMin"].values
pmout = df["PMout"].values
AVP_BR1_PM25 = df["AVP_BR1_PM25"].values
AVP_BR1_PM10 = df["AVP_BR1_PM10"].values
AVP_BR1_CO2 = df["AVP_BR1_CO2"].values
AVP_BR1_T = df["AVP_BR1_T"].values
AVP_BR1_RH = df["AVP_BR1_RH"].values
AVP_IN1_PM25 = df["AVP_IN1_PM25"].values
AVP_IN1_PM10 = df["AVP_IN1_PM10"].values
AVP_IN1_CO2 = df["AVP_IN1_CO2"].values
AVP_IN1_T = df["AVP_IN1_T"].values
AVP_IN1_RH = df["AVP_IN1_RH"].values
AVP_IN2_PM25 = df["AVP_IN2_PM25"].values
AVP_IN2_PM10 = df["AVP_IN2_PM10"].values
AVP_IN2_T = df["AVP_IN2_T"].values
AVP_IN2_RH = df["AVP_IN2_RH"].values
BR1_T = df["BR1_T"].values
BR1_RH = df["BR1_RH"].values
BS_T = df["BS_T"].values
BS_RH = df["BS_RH"].values
IN1_T = df["IN1_T"].values
IN1_RH = df["IN1_RH"].values
OUT_T = df["OUT_T"].values
OUT_RH = df["OUT_RH"].values
OUT2_T = df["OUT2_T"].values
OUT2_RH = df["OUT2_RH"].values
ANM_AS10 = df["ANM_AS10"].values
ANM_BA3 = df["ANM_BA3"].values
ANM_CDR = df["ANM_CDR"].values
ANM_EF1 = df["ANM_EF1"].values
ANM_RHD = df["ANM_RHD"].values
MTR_CDR = df["MTR_CDR"].values
STA_BR1 = df["STA_BR1"].values
STA_DFR = df["STA_DFR"].values
STA_DP1 = df["STA_DP1"].values
IBU_CLB = df["IBU_CLB"].values
IBU_CLF = df["IBU_CLF"].values
IBU_CRB = df["IBU_CRB"].values
IBU_CRF = df["IBU_CRF"].values
IBU_OVN = df["IBU_OVN"].values
output_file("pm.html")
plo = figure(title="PMin & PMOut", x_axis_label='Time', y_axis_label='PM', x_axis_type='datetime')
plo.line(time, pmin, legend="PMin", line_width=2, color ='red')
plo.line(time, pmout, legend="PMout.", line_width=2, color ='blue')
show(plo)
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
    output_file("pm10.html")
    plo = figure(title="PM10", x_axis_label='Time', y_axis_label='PM10', x_axis_type='datetime')
    plo.line(time, AVP_BR1_PM10, legend="AVP_BR1_PM10", line_width=2, color ='red')
    plo.line(time, AVP_IN1_PM10, legend="AVP_IN1_PM10.", line_width=2, color ='blue')
    plo.line(time, AVP_IN2_PM10, legend="AVP_IN2_PM10.", line_width=2, color ='green')
    show(plo)


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
        print("Graph Produced for Python2")
    output_file("GraphOutput" + ".html", title="Simulation Output Graphs")
    return p


def get_components(plot):
    return components(plot)

def column_join(plots):
    return column(*plots)

def row_join(plots):
    return row(*plots)

def display_plot(plots):
    show(column(*plots))


output_file("intemp.html")
plo = figure(title="Indoor Temperature", x_axis_label='Time', y_axis_label='Temperature', x_axis_type='datetime')
plo.line(time, AVP_BR1_T, legend="AVP_BR1_T", line_width=2, color ='red')
plo.line(time, AVP_IN1_T, legend="AVP_IN1_T.", line_width=2, color ='blue')
plo.line(time, AVP_IN2_T, legend="AVP_IN2_T.", line_width=2, color ='green')
plo.line(time, BR1_T, legend="BR1_T", line_width=2, color ='purple')
plo.line(time, BS_T, legend="BS_T.", line_width=2, color ='orange')
plo.line(time, IN1_T, legend="IN1_T.", line_width=2, color ='yellow')
show(plo)
output_file("pm25.html")
plo = figure(title="PM25", x_axis_label='Time', y_axis_label='PM10', x_axis_type='datetime')
plo.line(time, AVP_BR1_PM25, legend="AVP_BR1_PM25", line_width=2, color ='red')
plo.line(time, AVP_IN1_PM25, legend="AVP_IN1_PM25.", line_width=2, color ='blue')
plo.line(time, AVP_IN2_PM25, legend="AVP_IN2_PM25", line_width=2, color ='green')
show(plo)
output_file("outtemp.html")
plo = figure(title="Outdoor Temperature", x_axis_label='Time', y_axis_label='Temperature', x_axis_type='datetime')
plo.line(time, OUT_T, legend="OUT_T", line_width=2, color ='red')
plo.line(time, OUT2_T, legend="OUT2_T", line_width=2, color ='blue')
show(plo)
output_file("ibo.html")
plo = figure(title="iButtons", x_axis_label='Time', y_axis_label='Temperature', x_axis_type='datetime')
plo.line(time, IBU_CLB, legend="IBU_CLB", line_width=2, color ='red')
plo.line(time, IBU_CLF, legend="IBU_CLF", line_width=2, color ='blue')
plo.line(time, IBU_CRB, legend="IBU_CRB", line_width=2, color ='green')
plo.line(time, IBU_CRF, legend="IBU_CRF", line_width=2, color ='purple')
plo.line(time, IBU_OVN, legend="IBU_OVN", line_width=2, color ='orange')
show(plo)
output_file("inrh.html")
plo = figure(title="Indoor Relative Humidity", x_axis_label='Time', y_axis_label='RH', x_axis_type='datetime')
plo.line(time, AVP_BR1_RH, legend="AVP_BR1_RH", line_width=2, color ='red')
plo.line(time, AVP_IN1_RH, legend="AVP_IN1_RH", line_width=2, color ='blue')
plo.line(time, AVP_IN2_RH, legend="AVP_IN2_RH", line_width=2, color ='green')
plo.line(time, BR1_RH, legend="BR1_RH", line_width=2, color ='purple')
plo.line(time, BS_RH, legend="BS_RH", line_width=2, color ='orange')
plo.line(time, IN1_RH, legend="IN1_RH", line_width=2, color ='yellow')
show(plo)
output_file("outrh.html")
plo = figure(title="Outdoor Relative Humidity", x_axis_label='Time', y_axis_label='Temperature', x_axis_type='datetime')
plo.line(time, OUT_T, legend="OUT_RH", line_width=2, color ='red')
plo.line(time, OUT2_T, legend="OUT2_RH", line_width=2, color ='blue')
show(plo)
output_file("co2.html")
plo = figure(title="CO2", x_axis_label='Time', y_axis_label='PMCO2', x_axis_type='datetime')
plo.line(time, AVP_BR1_CO2, legend="AVP_BR1_CO2", line_width=2, color ='red')
plo.line(time, AVP_IN1_CO2, legend="AVP_IN1_CO2", line_width=2, color ='blue')
show(plo)
output_file("anm.html")
plo = figure(title="Anomometer", x_axis_label='Time', y_axis_label='Speed', x_axis_type='datetime')
plo.line(time, ANM_AS10, legend="ANM_AS10", line_width=2, color ='red')
plo.line(time, ANM_BA3, legend="ANM_BA3", line_width=2, color ='blue')
plo.line(time, ANM_CDR, legend="ANM_CDR", line_width=2, color ='green')
plo.line(time, ANM_EF1, legend="ANM_EF1", line_width=2, color ='purple')
plo.line(time, ANM_RHD, legend="ANM_RHD", line_width=2, color ='orange')
show(plo)
output_file("mtr.html")
plo = figure(title="Motor", x_axis_label='Time', y_axis_label='Speed', x_axis_type='datetime')
plo.line(time, MTR_CDR, legend="MTR_CDR", line_width=2, color ='red')
show(plo)
output_file("sta.html")
plo = figure(title="Door Status", x_axis_label='Time', y_axis_label='Status', x_axis_type='datetime')
plo.line(time, STA_BR1, legend="STA_BR1", line_width=2, color ='red')
plo.line(time, STA_DFR, legend="STA_DFR", line_width=2, color ='blue')
plo.line(time, STA_DP1, legend="STA_DP1", line_width=2, color ='green')
show(plo)
print("mean")
print(data.mean())
print("median")
print(data.median())
print("mode")
print(data.mode())
print("0.25")
print(data.quantile(q=0.25))
print("0.75")
print(data.quantile(q=0.75))
