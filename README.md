# Console Graphing Calculator

A tool to manipulate linear equations in the console

## Table of Contents

* **[Graph Properties](https://github.com/psurge1/graphing_calculator#graph-properties)**
   * [Properties Function](https://github.com/psurge1/graphing_calculator#properties-function)
   * [Slope](https://github.com/psurge1/graphing_calculator#slope)
   * [Y Intercept](https://github.com/psurge1/graphing_calculator#y-intercept)
   * [X Intercept](https://github.com/psurge1/graphing_calculator#x-intercept)
* **[Other Related Functions](https://github.com/psurge1/graphing_calculator#other-related-functions)**
   * [Point X Function](https://github.com/psurge1/graphing_calculator#point-x-function)
   * [Point Y Function](https://github.com/psurge1/graphing_calculator#point-y-function)
   * [Console Plot Function](https://github.com/psurge1/graphing_calculator#console-plot-function)
   * [Equation Function](https://github.com/psurge1/graphing_calculator#equation-function)
* **[Other](https://github.com/psurge1/graphing_calculator#other)**

## Graph Properties

### Properties Function

```python
self.properties()
```

returns the slope, y intercept, x intercept, and scale (if applicable) of the given linear equation (string)

#### Example:

```python
a = linear('y=42x+2/9')
print (a.properties())
```
```
y = 42.0x + 0.2222222222222222
Slope: 42.0
Y-int: 0.2222222222222222
X-int: -0.005291005291005291
```

### Slope

```python
self.m
```
```python
self.slope
```

returns the slope of the given linear equation (float)

#### Example:

```python
a = linear('y=4x-2')
print (a.m)
```
```
4.0
```

### Y Intercept

```python
self.b
```

```python
self.y_intercept
```

returns the y intercept of the given linear equation (float)

#### Example:

```python
a = linear('y=2x+12')
print (a.b)
```
```
12.0
```

### X Intercept

```python
self.x_intercept
```

returns the x intercept of the given linear equation (float)

#### Example:

```python
a = linear('y=2x+12')
print (a.x_intercept)
```
```
-6.0
```

‎

## Other Related Functions

### Point X Function

```python
self.point_x(y)
```

returns the corresponding x value as a float

#### Parameters:

##### y (float)

#### Example:

```python
a = linear('y=4x-2')
x = point_x(2) #y = 2
print (x)
```
```
1.0
```

‎

### Point Y Function

```python
self.point_y(x)
```

returns the corresponding y value (float)

#### Parameters:

##### x (float)

#### Example:

```python
a = linear('y=4x-2')
y = point_y(3) #x = 3
print (y)
```
```
10.0
```

‎

### Console Plot Function

```python
self.console_plot(len_x, len_y, plot_fmt, scale, description)
```

saves the plot of the given linear equation in a variable (str)
to display the graph in the console, print the variable in an f string

For Example:
```python
a = linear('y=2x+1')
graph = a.console_plot(len_x, len_y, plot_fmt, scale, description)
print(f'{graph}')
```

#### Parameters:

##### len_x (int) _(default = 10)_

###### width of the x axis in units of '_ '

##### len_y (int) _(default = 10)_

###### height of the y axis in units of '|'

##### plot_fmt (str)

###### - 'plus' is '+' _(default)_
###### - 'point' is '.'
###### - 'carot' is '^'
###### - 'asterisk' is '*'

##### scale (int) _(default = 1)_

###### number of units per whole number on the graph

##### description (bool) _(default = False)_

###### prints the following properties under the graph:
###### - slope
###### - y intercept
###### - x intercept
###### - scale (if applicable)

#### Examples:

```python
a = linear('y=2/3x+2')
graph = a.console_plot(len_x=10,len_y=10,description=True)
print (f'{graph}')
```
```
|
|                  +
|              + +
|            +
|        + +
|      +
|  + +
|+
|
| _ _ _ _ _ _ _ _ _ _
y = 0.6666666666666666x + 2.0
Slope: 0.6666666666666666
Y-int: 2.0
X-int: -3.0
Graph Scale: 1
```

‎

```python
a = linear('y=2x+1')
graph = a.console_plot(len_x=20,len_y=20,scale=2,plot_fmt='carot')
print (f'{graph}')
```
```
|
|                                ^
|
|
|
|                        ^
|
|
|
|                ^
|
|
|
|        ^
|
|
|
|^
|
| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
```

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

#### Example:

```python
a = linear('y=4x-2')
print (a.equation(form='standard'))
```
```
-4.0x + y = -2.0
```

‎

## Other

### raw_equation
```python
self.raw_equation
```
 returns the given linear equation with no spaces (str)
 
 #### Example:

```python
a = linear('y = 4x + 2')
print (a.raw_equation)
```
```
'y=4x+2'
```

‎

### standard_equation
```python
self.standard_equation
```
returns the standard form of the given linear equation (list)

#### Example:

```python
a = linear('y=12x-2')
print (a.standard_equation)
```
```
[-12.0, 'x', ' ', '+', ' ', 'y', ' ', '=', ' ', '-', -2.0]
```

‎

### slope_intercept_equation
```python
self.slope_intercept_equation
```
returns the slope intercept form of the given linear equation (list)

#### Example:

```python
a = linear('y=12x-2')
print ()
```
```
['y', ' ', '=', ' ', 12.0, 'x', ' ', '-', ' ', -2.0]
```

‎

### sign
```python
self.sign
```
returns the sign of the y intercept (str)

#### Example:

```python
a = linear('y=2x-2')
print (a.sign)
```
```
'-'
```

‎

### x_factor
```python
self.x_factor
```
returns the number of '_ ' units for each whole x unit on the graph (int)
Note: self.x_factor can only be used after self.console_plot() as self.x_factor is only applicable to that function
 
 #### Example:
 
 ```python
a = linear('y=4x-1')
a.console_plot(scale=2)
print (a.x_factor)
```
```
4
```

‎

### y_factor
```python
self.y_factor
```
returns the number of spaces for each whole y unit on the graph (int)
Note: self.y_factor can only be used after self.console_plot() as self.y_factor is only applicable to that function

#### Example:

```python
a = linear('y=5x+2')
a.console_plot(scale=3)
print ()
```
```
3
```
