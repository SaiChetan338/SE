import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a*(time ** 2) + b * time + c
    return temperature

def main():

    coefficient_sets = [
        (0.1, -1, 2),
        (0.2, 2, 5),
        (0.15, 4, 3)
    ]

    for idx, (a, b, c) in enumerate(coefficient_sets):
        time_values = np.linspace(0, 10, 50)
        temperature_values = quadratic_model(time_values, a, b, c)
        label = f'Set {idx + 1}: a={a}, b={b}, c={c}'
        plt.plot(time_values, temperature_values, label=label)

    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Multiple Set')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
