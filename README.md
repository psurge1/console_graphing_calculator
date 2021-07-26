# Graphing Calculator



## Table of Contents



## Properties

```python
self.properties()
```

returns the slope, y intercept, x intercept, and scale (if applicable) of the given equation

### Slope

```python
self.m
```

### Y Intercept

```python
self.b
```

```python
self.y_intercept
```

### X Intercept

```python
self.x_intercept
```

### Other Related Functions

```python
self.point_x(y)
```

```python
self.point_y(x)
```

## Graph Plot

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

## Other

```python
self.equation(form)
```

 - string (returns the equation)
form - string ('point slope', 'standard')


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
