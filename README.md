# Modified/improved Euler's Method 
Implementation of algorithm solving differential equation using Modified Euler's Method.

### Used
* Python
* Numpy 
* Pandas

### Usage
* change or replace the `differential_equation` function for the specific one to solve it using Modified Euler's Method
* execute `modified_euler_method` function with specific parameters:
  - `differential_equation` function
  - initial x value
  - initial y value
  - range start value
  - range stop value
  - range interval step
* get output value as plot, dataframe and CSV file

### Example
Solving `x + x * y + y + 1` differential equation with initial condition `y(-1)=1` in range `[-1,1]` with step `0.25`. 
```python 
def differential_equation(x: float, y: float) -> float:
    """
    Any differential equation
    Args:
        x (int): argument
        y (int): y argument
    Returns:
        float: equation output
    """
    return x + x * y + y + 1
```

```python
mem = modified_euler_method(differential_equation, -1., 1., -1., 1., 0.25)
```


