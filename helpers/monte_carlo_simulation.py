import numpy as np


def monte_carlo_simulation(f, a, b, num_experiments):
    x_random = np.random.uniform(a, b, num_experiments)
    y_random = np.random.uniform(0, f(b), num_experiments)

    points_under_curve = y_random < f(x_random)
    area_rect = (b - a) * f(b)

    return area_rect * np.sum(points_under_curve) / num_experiments
