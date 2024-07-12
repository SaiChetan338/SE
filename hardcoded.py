import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time):
    a = 0.1
    b = -1
    c = 2

    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    time_values = np.linspace(0, 10, 50)
    temperature_values = quadratic_model(time_values)
    
    a = 0.1
    b = -1
    c = 2
    
    plt.plot(time_values, temperature_values, label=f'Hard Coded a={a}, b={b}, c={c}')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Hard Coded')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
