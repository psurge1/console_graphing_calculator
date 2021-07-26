# Graphing Calculator



## Table of Contents



## Graph Properties

### Properties Function
```python
self.properties()
```

returns the slope, y intercept, x intercept, and scale (if applicable) of the given linear equation

### Slope

```python
self.m
```

returns the slope of the given linear equation

### Y Intercept

```python
self.b
```

```python
self.y_intercept
```

returns the y intercept of the given linear equation

### X Intercept

```python
self.x_intercept
```

returns the x intercept of the given linear equation

## Other Related Functions

### Point X Function

```python
self.point_x(y)
```

returns the corresponding x value

#### Y (float)

### Point Y Function

```python
self.point_y(x)
```

returns the corresponding y value

#### X (float)

### Graph Plot Function

```python
self.console_plot(len_x,len_y,plot_fmt,scale,description)
```

#### len_x (int)

width of the x axis in units of '_ '

#### len_y (int)

height of the y axis in units of '|'

#### plot_fmt (str)

- 'plus' --> '+'
- 'point' --> '.'
- 'asterisk' --> '*'
- 'carot' -- > '^'

#### description (bool)

prints the following properties under the graph:
- slope
- y intercept
- x intercept
- scale (if applicable)

### Equation Function

```python
self.equation(form)
```

returns the given linear equation

#### form 
- 'point slope' _(default)_
- 'standard'

## Other

```python
self.raw_equation
```
 - str

```python
self.standard_equation
```
 - list

```python
self.slope_intercept_equation
```
- list

```python
self.sign
```
 - str (slope intercept sign)

```python
self.x_factor
```
 - int (number of spaces for each whole x unit)

```python
self.y_factor
```
 - int (number of spaces for each whole y unit)
