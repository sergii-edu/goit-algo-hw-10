from scipy import integrate
from tabulate import tabulate

from helpers.draw_plot import draw_plot
from helpers.monte_carlo_simulation import monte_carlo_simulation


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа

experiment_sizes = [1000, 5000, 10000, 20000, 50000]


def main():
    # Обчислення інтеграла за допомогою методу Монте-Карло
    results = []
    for num_experiments in experiment_sizes:
        average_area = monte_carlo_simulation(f, a, b, num_experiments)
        results.append([num_experiments, average_area])
    headers = ["Кількість експериментів", "Площа по методу Монте Карло"]
    print(tabulate(results, headers=headers), "\n")

    # Обчислення інтеграла за допомогою функції quad
    quad_result = integrate.quad(f, a, b)
    print(f"Значення інтеграла: {quad_result[0]}")

    # Побудова графіка
    draw_plot(f, a, b)


if __name__ == "__main__":
    main()
