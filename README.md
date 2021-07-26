# Graphing Calculator



## Table of Contents



## Functions

self.slope()

``Use `code` in your Markdown file.``

self.y_int() - float

self.x_int() - float

self.point_x(y) - float (given a y value, finds the x value)
y - int or float

self.point_y(x) - float (given an x value, finds the y value)
x - int or float

self.equation(form) - string (returns the equation)
form - string ('point slope', 'standard')

self.console_plot(len_x,len_y,plot_fmt,scale,description) - string
(plots a customizeable graph)
len_x - int (width of the x axis in '_ '
len_y - int (height of the y axis in '|'
plot_fmt - str (point symbol: 'plus':'+','point':'.','asterisk':'*','carot':'^')
description - bool (show the properties of the graph)

self.properties() - str (returns the slope, y intercept, x intercept, and scale if applicable of the equation)

## Other

self.raw_equation - str

self.standard_equation - list

self.slope_intercept_equation - list

self.sign - str (slope intercept sign)

self.m - float (slope)

self.b - float (y intercept)

self.y_intercept - float

self.x_intercept - float

self.x_factor - int (number of spaces for each whole x unit)

self.y_factor - int (number of spaces for each whole y unit)
