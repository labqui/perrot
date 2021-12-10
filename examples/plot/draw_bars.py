#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import pero
import perrot

# prepare data
categories = ("one", 'two', "three", "four", "five")
y_data1 = (5, 10, 7, 3, 4)
y_data2 = (7, 5, 9, 1, 5)
y_data3 = (2, 1, 3, 5, 4)

width = 0.2
spacing = 0.05

# init ordinal x-axis
x_axis = perrot.plot.OrdinalAxis(
    position = pero.BOTTOM,
    margin = 0,
    labels = categories,
    major_tick_size = 0,
    level = 1)

# init plot
plot = perrot.plot.Plot(
    x_axis = x_axis,
    y_axis_title = "count",
    x_grid_show_major_lines = False)

# init labels
label = lambda d: str(d[1])
tooltip = lambda d: "%s (%s)" % (d[1], d[0])

# add series
series1 = perrot.plot.VBars(
    title = "Series 1",
    x = categories,
    top = y_data1,
    width = width,
    x_offset = -(width+spacing),
    x_mapper = x_axis.mapper,
    show_labels = True,
    label_text = label,
    tooltip_text = tooltip)

series2 = perrot.plot.VBars(
    title = "Series 2",
    x = categories,
    top = y_data2,
    width = width,
    x_mapper = x_axis.mapper,
    show_labels = True,
    label_text = label,
    tooltip_text = tooltip)

series3 = perrot.plot.VBars(
    title = "Series 3",
    x = categories,
    top = y_data3,
    width = width,
    x_offset = width+spacing,
    x_mapper = x_axis.mapper,
    show_labels = True,
    label_text = label,
    tooltip_text = tooltip)

plot.plot(series1, x_axis=x_axis)
plot.plot(series2, x_axis=x_axis)
plot.plot(series3, x_axis=x_axis)

# show plot
plot.zoom()
plot.view("VBars Series")
