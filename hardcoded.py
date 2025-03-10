import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time):
    coefficients = {
        'a': 0.1,
        'b': -1,
        'c': 2
    }

    temperature = coefficients['a'] * (time ** 2) + coefficients['b'] * time + coefficients['c']
    return temperature, coefficients

def main():
    time_values = np.linspace(0, 10, 50)
    temperature_values, coefficients = quadratic_model(time_values)
    
    plt.plot(time_values, temperature_values, label=f'Hard Coded a={coefficients["a"]}, b={coefficients["b"]}, c={coefficients["c"]}')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Quadratic Model')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()

    plt.show()

if __name__ == '__main__':
    main()
