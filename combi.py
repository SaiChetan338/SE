import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    """
    Quadratic model function to calculate temperature based on time and coefficients.
    """
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
   
    a_hard = 0.1
    b_hard = -1
    c_hard = 2

    print("Enter coefficients for user input:")

    try:
        a_user = float(input("Enter coefficient a: "))
        b_user = float(input("Enter coefficient b: "))
        c_user = float(input("Enter coefficient c: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    time_values = np.linspace(0, 10, 50)

    temperature_values_hard = quadratic_model(time_values, a_hard, b_hard, c_hard)
    temperature_values_user = quadratic_model(time_values, a_user, b_user, c_user)

    plt.figure(figsize=(10, 6))
    plt.plot(time_values, temperature_values_hard, label='Hard-Coded Coefficients (a=0.1, b=-1, c=2)', linestyle='-', color='blue')
    plt.plot(time_values, temperature_values_user, label=f'User Input Coefficients (a={a_user}, b={b_user}, c={c_user})', linestyle='--', color='red')
    
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Quadratic Model Comparison')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
