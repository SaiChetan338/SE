import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a*(time ** 2) + b * time + c
    return temperature

def main():

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    time_values = np.linspace(0, 10, 100)
    temperature_values = quadratic_model(time_values, a, b, c)
    

    plt.figure(figsize=(10, 6))
    plt.plot(time_values, temperature_values, label=f'a={a}, b={b}, c={c}')
    
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Quadratic Model With User Input')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
