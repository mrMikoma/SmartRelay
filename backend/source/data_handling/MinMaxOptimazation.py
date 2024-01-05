from scipy.optimize import linprog
import numpy as np

def offTime():
    print("Starting optimization...\n")
    # Constants
    hours = 24
    T_min = 18  # Minimum comfortable temperature
    T_max = 22  # Maximum comfortable temperature
    H_max = 10  # Maximum heating capacity

    # Cost and temperature data (example values)
    costs = [2, 3, 2, 4, 5, 6, 8, 10, 12, 15, 18, 20, 25, 23, 22, 18, 15, 14, 12, 10, 8, 7, 5, 4]
    temperatures = [18, 17, 16, 16, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 22, 21, 20, 19, 18, 18, 18, 18, 18, 18]

    # Convert lists to NumPy arrays
    costs = np.array(costs)
    temperatures = np.array(temperatures)

    # Coefficients for the objective function
    c = costs

    result = ""

    try:
        # Coefficients for the temperature constraint
        A_temp = [[0] * (t - 1) + [-1, 1] + [0] * (hours - t) for t in range(1, hours + 1)]
        b_temp = [T_max - T_min] * hours

        # Coefficients for the heating capacity constraint
        A_capacity = [[0] * t + [1] + [0] * (hours - t - 1) for t in range(hours)]
        b_capacity = [H_max] * hours

        # Solve the linear programming problem
        result = linprog(c, A_ub=A_temp + A_capacity, b_ub=b_temp + b_capacity, method='highs')



        # Display the result
        if result.success:
            print("Optimal heating schedule:")
            for t, amount in enumerate(result.x, start=1):
                print(f"Hour {t}: {amount:.2f} units of heating")
            print(f"Total cost: {result.fun:.2f}")
        else:
            print("Optimization failed.")

    except Exception as e:
        print(f"An error occurred: {e}")

