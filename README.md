# Graphing Calculator

A tool to manipulate linear equations in the console

‎

## Table of Contents

- [Graph Properties](https://github.com/psurge1/graphing_calculator#graph-properties)
    [Properties Function]()
    [Slope]()
    [Y Intercept]()
    [X Intercept]()
- [Other Related Functions](https://github.com/psurge1/graphing_calculator#other-related-functions)
    [Point X Function]()
    [Point Y Function]()
    [Console Plot Function]()
    [Equation Function]()
- [Other](https://github.com/psurge1/graphing_calculator#other)

‎

## Graph Properties

### Properties Function

```python
self.properties()
```

returns the slope, y intercept, x intercept, and scale (if applicable) of the given linear equation (string)

### Slope

```python
self.m
```

returns the slope of the given linear equation (float)

### Y Intercept

```python
self.b
```

```python
self.y_intercept
```

returns the y intercept of the given linear equation (float)

### X Intercept

```python
self.x_intercept
```

returns the x intercept of the given linear equation (float)

‎

## Other Related Functions

### Point X Function

```python
self.point_x(y)
```

returns the corresponding x value as a float

#### Parameters:

##### y (float)

‎

### Point Y Function

```python
self.point_y(x)
```

returns the corresponding y value (float)

#### Parameters:

##### x (float)

‎

### Console Plot Function

```python
self.console_plot(len_x, len_y, plot_fmt, scale, description)
```

plots the given linear equation in the console (str)

#### Parameters:

##### len_x (int) _(default = 10)_

###### width of the x axis in units of '_ '

##### len_y (int) _(default = 10)_

###### height of the y axis in units of '|'

##### plot_fmt (str)

###### - 'plus' --> '+' _(default)_
###### - 'point' --> '.'
###### - 'asterisk' --> '*'
###### - 'carot' -- > '^'

##### scale (int) _(default = 1)_

###### number of units per whole number on the graph

##### description (bool) _(default = False)_

###### prints the following properties under the graph:
###### - slope
###### - y intercept
###### - x intercept
###### - scale (if applicable)

‎

### Equation Function

```python
self.equation(form)
```

returns the given linear equation (str)

#### Parameters:

##### form 
###### - 'point slope' _(default)_
###### - 'standard'

‎

## Other

```python
self.raw_equation
```
 returns the given linear equation with no spaces (str)

```python
self.standard_equation
```
returns the standard form of the given linear equation (list)

```python
self.slope_intercept_equation
```
returns the slope intercept form of the given linear equation (list)

```python
self.sign
```
returns the sign of the y intercept (str)

```python
self.x_factor
```
 returns the number of '_ ' units for each whole x unit on the graph (int)

```python
self.y_factor
```
returns the number of spaces for each whole y unit on the graph (int)
