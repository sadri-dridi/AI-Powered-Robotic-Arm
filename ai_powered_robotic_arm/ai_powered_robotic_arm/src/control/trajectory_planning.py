import numpy as np

def cubic_spline(start, end, num_points=100):
    t = np.linspace(0, 1, num_points)
    a = 2 * (start - end)
    b = -3 * (start - end)
    return a * t**3 + b * t**2 + start
