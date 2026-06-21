"""
CPSC 250 - Week 4 Lecture 1 Demonstration Code
NumPy, Plotting, and Simple Polynomial Fits

This file contains runnable versions of the code examples from
week4a_numpy_polyfit.tex.  It is organized to follow the lecture flow.
"""

import numpy as np
import matplotlib.pyplot as plt


def section(title: str) -> None:
    """Print a simple section divider."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def pause_for_plot() -> None:
    """Show a plot and wait until the window is closed."""
    plt.tight_layout()
    plt.show()


def demo_creating_arrays() -> None:
    section("Creating a NumPy Array")

    num_list = [1, 2, 3, 4, 5]
    values = np.array(num_list)
    print(values)

    other_values = np.array([5, 6, 7, 8, 9])
    print(other_values)


def demo_lists_vs_arrays() -> None:
    section("Arrays Behave Differently from Lists")

    numbers = [1, 2, 3]
    print("numbers as list:", numbers)
    print("Python list * 2:")
    print(numbers * 2)

    print()

    numbers = np.array([1, 2, 3])
    print("numbers as array:", numbers)
    print("NumPy array * 2:")
    print(numbers * 2)


def demo_special_arrays() -> None:
    section("Special Arrays")

    zeros = np.zeros(5)
    ones = np.ones(5)

    print("zeros:")
    print(zeros)

    print("\nones:")
    print(ones)

    x = np.arange(0, 10, 1)
    print("\narange:")
    print(x)

    x = np.linspace(0, 10, 5)
    print("\nlinspace (5 points):")
    print(x)

    x = np.linspace(0, 10, 6)
    print("\nlinspace (6 points):")
    print(x)


def demo_vectorized_operations() -> None:
    section("Vectorized Operations")

    x_values = [-2, -1, 0, 1, 2]
    y_values = []

    for x in x_values:
        y_values.append(x**2)

    print("List/loop version:")
    print(y_values)

    x = np.array([-2, -1, 0, 1, 2])
    y = x**2

    print("\nNumPy vectorized version:")
    print(y)


def demo_vectorized_physics() -> None:
    section("Vectorized Physics Example")

    t = np.linspace(0, 10, 101)

    x0 = 5.0
    v0 = 52.0
    a = -9.8

    x = x0 + v0 * t + 0.5 * a * t**2

    print("First five time values:")
    print(t[:5])

    print("\nFirst five position values:")
    print(x[:5])

    plt.figure()
    plt.plot(t, x, 'o',label="Position")
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    plt.title("Position vs Time")
    plt.legend()
    pause_for_plot()


def demo_numpy_summary_functions() -> None:
    section("Useful NumPy Functions")

    data = np.array([72, 75, 79, 81, 78, 74])

    print("data:", data)
    print("min:", np.min(data))
    print("max:", np.max(data))
    print("mean:", np.mean(data))
    print("standard deviation:", np.std(data))


def demo_basic_scatter_plot() -> None:
    section("Plotting with Matplotlib")

    x = np.array([1, 2, 3, 4, 5])
    y = np.array([3, 5, 7, 8, 11])

    plt.figure()
    plt.scatter(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    pause_for_plot()


def demo_labeled_plot() -> None:
    section("Adding Labels and a Title")

    x = np.array([1, 2, 3, 4, 5])
    y = np.array([3, 5, 7, 8, 11])

    plt.figure()
    plt.scatter(x, y, label="Data")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Example Data")
    plt.legend()
    pause_for_plot()


def demo_polyfit_line() -> None:
    section("Simple Fitting with np.polyfit")

    x = np.array([1, 2, 3, 4, 5])
    y = np.array([3, 5, 7, 8, 11])

    m, b = np.polyfit(x, y, 1)

    print("slope =", m)
    print("intercept =", b)
    print(f"Best-fit line: y = {m:.3f}x + {b:.3f}")

    y_fit = m * x + b

    plt.figure()
    plt.scatter(x, y, label="Data")
    plt.plot(x, y_fit, label="Best-fit line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Data with Linear Fit")
    plt.legend()
    pause_for_plot()


def demo_smoother_fit_line() -> None:
    section("A Smoother Fit Line")

    x = np.array([1, 2, 3, 4, 5])
    y = np.array([3, 5, 7, 8, 11])

    m, b = np.polyfit(x, y, 1)

    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = m * x_fit + b

    plt.figure()
    plt.scatter(x, y, label="Data")
    plt.plot(x_fit, y_fit, label="Best-fit line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Data with Smooth Linear Fit")
    plt.legend()
    pause_for_plot()


def demo_distance_vs_time() -> None:
    section("Example: Distance vs Time")

    time = np.array([0, 1, 2, 3, 4, 5])
    distance = np.array([1.2, 3.1, 5.4, 7.0, 9.3, 11.1])

    m, b = np.polyfit(time, distance, 1)

    print("slope =", m)
    print("intercept =", b)
    print(f"Estimated velocity: {m:.3f} m/s")

    time_fit = np.linspace(min(time), max(time), 100)
    distance_fit = m * time_fit + b

    plt.figure()
    plt.scatter(time, distance, label="Measurements")
    plt.plot(time_fit, distance_fit, label="Best-fit line")
    plt.xlabel("Time (s)")
    plt.ylabel("Distance (m)")
    plt.title("Distance vs Time")
    plt.legend()
    pause_for_plot()


def demo_quadratic_polyfit() -> None:
    section("Higher-Degree Polynomial Fits")

    x = np.array([1, 2, 3, 4, 5])
    y = np.array([3, 5, 7, 8, 11])

    coefficients = np.polyfit(x, y, 1)

    print("Linear coefficients:")
    print(coefficients)
    print("These correspond to y = ax + b")
    print()

    a, b = coefficients
    x_fit_linear = np.linspace(min(x), max(x), 100)
    y_fit_linear = a * x_fit_linear + b

    coefficients = np.polyfit(x, y, 2)

    print("Quadratic coefficients:")
    print(coefficients)
    print("These correspond to y = ax^2 + bx + c")
    print()

    a, b, c = coefficients
    x_fit_quad = np.linspace(min(x), max(x), 100)
    y_fit_quad = a * x_fit_quad**2 + b * x_fit_quad + c

    coefficients = np.polyfit(x, y, 3)
    print("Cubic coefficients:")
    print(coefficients)
    print("These correspond to y = ax^3 + bx^2 + cx + d")

    a, b, c, d = coefficients
    x_fit_cube = np.linspace(min(x), max(x), 100)
    y_fit_cube = a * x_fit_quad**3 + b * x_fit_quad**2 + c*x_fit_quad + d

    plt.figure()
    plt.scatter(x, y, label="Data")
    plt.plot(x_fit_quad, y_fit_quad, label="Quadratic line")
    plt.plot(x_fit_linear, y_fit_linear, label="Linear fit")
    plt.plot(x_fit_cube, y_fit_cube, label="Cubic fit")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Example Quadratic Fit")
    plt.legend()
    pause_for_plot()


def main() -> None:
    #demo_creating_arrays()
    #demo_lists_vs_arrays()
    #demo_special_arrays()
    #demo_vectorized_operations()
    #demo_vectorized_physics()
    #demo_numpy_summary_functions()
    #demo_basic_scatter_plot()
    #demo_labeled_plot()
    #demo_polyfit_line()
    #demo_smoother_fit_line()
    #demo_distance_vs_time()
    demo_quadratic_polyfit()


if __name__ == "__main__":
    main()
