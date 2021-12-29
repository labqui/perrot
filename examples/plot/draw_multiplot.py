#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import numpy
import pero

import perrot

sig = 200
sig2 = sig * sig
med = 750.0
# prepare data
x_data = numpy.linspace(100, 1500, 300)
sin_data = numpy.divide(numpy.exp(numpy.divide(-numpy.subtract(x_data, med) ** 2, 2 * sig2)), numpy.sqrt(numpy.pi * 2 * sig2))

# init plots
settings = {
    "x_axis_title": "pi",
    "y_axis_title": "f(x)",
    # "x_rangebar": None,
    # "y_rangebar": None
}

plot1 = perrot.plot.Plot(**settings)
# plot2 = perrot.plot.Plot(**settings)
# plot3 = perrot.plot.Plot(**settings)

# add series
plot1.plot(perrot.plot.Profile(x=x_data, y=sin_data,
                               steps=pero.LINE_STEP_NONE), title="sin(x)", color="b")
plot1.plot(perrot.plot.Lines(
    x1=x_data,
    y1=sin_data * 0,
    x2=x_data,
    y2=sin_data,
    # anchor=pero.START,
    # start_head='o',
    # start_head_size=4,
    # end_head='|>',
    # end_head_size=11,
    title="Lines"))
plot1.zoom()

# make layout
layout = pero.Layout()
layout.add(plot1, 0, 0, col_span=2)
# layout.add(plot2, 1, 0)
# layout.add(plot3, 1, 1)

layout.show()
