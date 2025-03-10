import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def read_coefficients(file_path):
    coefficient_sets = []
    with open(file_path, 'r') as file:
        for line in file:
            a, b, c = map(float, line.strip().split(','))
            coefficient_sets.append((a, b, c))
    return coefficient_sets

def main():
    file_path = 'filein.txt'
    coefficient_sets = read_coefficients(file_path)

    for idx, (a, b, c) in enumerate(coefficient_sets):
        time_values = np.linspace(0, 10, 50)
        temperature_values = quadratic_model(time_values, a, b, c)
        label = f'Set {idx + 1}: a={a}, b={b}, c={c}'
        plt.plot(time_values, temperature_values, label=label)

    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Multiple Set From File')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
