#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import numpy
import pero

import perrot

# prepare data
count = int(1e4)
x1_data = numpy.linspace(200, 1400, count)
y1_data = x1_data ** 2
x2_data = x1_data - x1_data ** 3 / 10 + 0.3
y2_data = y1_data - x1_data ** 2 / 10 + 0.5

# init plot
plot = perrot.plot.Plot(
    x_axis_title="x-value",
    y_axis_title="random")

# add series
series = perrot.plot.Lines(
    x1=x1_data,
    y1=y1_data,
    x2=x2_data,
    y2=y2_data,
    anchor=pero.START,
    start_head='o',
    start_head_size=8,
    end_head='|>',
    end_head_size=11,
    title="Lines")

plot.plot(series)

# show plot
plot.zoom()
plot.view("Lines Series")
