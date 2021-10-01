#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import numpy
import pero
import perrot

# prepare data
data = numpy.random.normal(size=1000)

hist1, bins1 = perrot.plot.calc_histogram(data, 50, cumulative=False)
hist2, bins2 = perrot.plot.calc_histogram(data, 50, cumulative=True)

# normalize cumulative line
hist2 = hist2 / len(data) * 100

# init plot
plot = perrot.plot.Plot(
    x_axis_title = 'random',
    y_axis_title = 'count')

# add additional axis
right_axis = perrot.plot.LinAxis(
    title = '%',
    position = pero.RIGHT,
    z_index = 1,
    margin = 0)

plot.add(right_axis)

# add bars
series = perrot.plot.Bars(
    top = hist1,
    left = bins1[:-1],
    right = bins1[1:],
    bottom = 0,
    anchor = pero.TOP,
    margin = (0.05, 0, 0, 0))

plot.plot(series)

# add cumulative
series = perrot.plot.Profile(
    x = bins2[1:],
    y = hist2,
    line_width = 2,
    steps = pero.BEFORE,
    margin = 0,
    color = "o")

plot.plot(series, y_axis=right_axis)

# show plot
plot.zoom()
plot.view("Histogram")
