import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from estimates import convergence_of_integral, error_analysis, estimate_pi, exact_integral_1, exact_integral_2D, monte_carlo_integration_1, monte_carlo_integration_2, plot_circle_and_points, plot_pi_convergence, predefined_functions, visualize_1D_integration, predefined_2D_functions, visualize_2D_integration
from error_analysis import monte_carlo_error_analysis_1D, monte_carlo_error_analysis_2D, plot_error
# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Select a task:",
    ("Estimation of π", "1D Numerical Integration", "2D Numerical Integration", "Error Analysis")
)

if section == "Estimation of π":
    st.header("Estimation of π Using Monte Carlo Methods")
    N_pi = st.slider("Number of Random Points (N)", min_value=100, max_value=100000, step=1000, value=10000)
    if st.button("Estimate π"):
        pi_estimate, x, y, inside_circle = estimate_pi(N_pi)
        st.write(f"Estimated π: {pi_estimate}")
        st.write(f"Actual π: {np.pi}")
        plot_circle_and_points(x, y, inside_circle, N_pi)
        
    st.header("π Convergence and Error Visualization")
    min_N = st.number_input("Minimum N:", value=10, min_value=1, max_value=100000)
    max_N = st.number_input("Maximum N:", value=10000, min_value=1, max_value=1000000)
    step_N = st.number_input("Step size for plot:", value=100, min_value=100, max_value=1000)
    
    N_values = [i for i in range(int(min_N), int(max_N) + 1, int(step_N))]
    if st.button("Plot Convergence and Error"):
        plot_pi_convergence(N_values)
        
elif section == "1D Numerical Integration":
    st.header("1D Integration-Monte Carlo Methods")
    selected_function = st.selectbox("Select a function to integrate:", list(predefined_functions.keys()))
    
    a_1 = st.number_input("Start of the range (a)", value=0.0)
    b_1 = st.number_input("End of the range (b)", value=1.0)
    N_1 = st.slider("Number of Random Points (N)", min_value=10, max_value=100000, step=1000, value=1000)
    
    if st.button("Calculate 1D Integral"):
        integral_1, _, _ = monte_carlo_integration_1(predefined_functions[selected_function], a_1, b_1, N_1)
        st.write(f"Estimated 1D Integral: {integral_1}")
        
    st.header("1D Integral Convergence and Error Visualization")
    selected_function = st.selectbox("Select a func to integrate:",list(predefined_functions.keys()))
    a = st.number_input("Start of the range (a):", value=0.0)
    b = st.number_input("End of the range (b):", value=1.0)
    min_N = st.number_input("Minimum N:", value=10, min_value=1, max_value=100000)
    max_N = st.number_input("Maximum N:", value=10000, min_value=1, max_value=1000000)
    step_N = st.number_input("Step size for plot:", value=100, min_value=1, max_value=1000)
    
    N_values = [i for i in range(int(min_N), int(max_N) + 1, int(step_N))]
    
    if st.button("Run Simulation"):
        f = predefined_functions[selected_function]
        estimates = []
        errors = []

        # Exact integral for comparison
        exact_value = exact_integral_1(f, a, b)

        # Calculate integral estimates and errors
        for N in N_values:
            estimate, x,y = monte_carlo_integration_1(f, a, b, N)
            estimates.append(estimate)
            errors.append(abs(estimate - exact_value))

        # Plot convergence of the integral estimates
        convergence_of_integral(N_values, estimates, exact_value)
        error_analysis(N_values, errors)
        st.write(f"Estimated 1D Integral: {estimates[-1]}")
        visualize_1D_integration(x, y,a_1, b_1, f, N, estimates)

elif section == "2D Numerical Integration":
    st.header("2D Numerical Integration Using Monte Carlo Methods")
    selected_function = st.selectbox("Select a function to integrate:", list(predefined_2D_functions.keys()))
    
    a_2D = st.number_input("Start of the range for both dimensions (a)", value=0.0)
    b_2D = st.number_input("End of the range for both dimensions (b)", value=1.0)
    N_2D = st.slider("Number of Random Points (N)", min_value=100, max_value=100000, step=1000, value=10000)
    if st.button("Calculate 2D Integral"):
        integral_2D = monte_carlo_integration_2(predefined_2D_functions[selected_function], a_2D, b_2D, N_2D)
        st.write(f"Estimated 2D Integral: {integral_2D}")


    st.header("2D Integral Convergence and Error Visualization")
    selected_function_2D = st.selectbox("Select a 2D function to integrate:", list(predefined_2D_functions.keys()))

    # Input parameters
    a_2 = st.number_input("Start of the range for both:", value=0.0)
    b_2 = st.number_input("End of the range for both:", value=1.0)
    
    min_N_2 = st.number_input("Minimum N:", value=100, min_value=1, max_value=100000)
    max_N_2 = st.number_input("Maximum N:", value=10000, min_value=1, max_value=1000000)
    step_N_2 = st.number_input("Step size for plot:", value=100, min_value=1, max_value=1000)
    N_values_2D = [i for i in range(int(min_N_2), int(max_N_2) + 1, int(step_N_2))]

    if st.button("Run 2D Simulation"):
        # Retrieve the selected function
        f_2D = predefined_2D_functions[selected_function_2D]

        # Compute the exact integral
        exact_value_2D = exact_integral_2D(f_2D, a_2, b_2)
        st.write(f"Exact 2D Integral: {exact_value_2D}")

        # Monte Carlo simulation
        estimates_2D = []
        errors_2D = []
        for N in N_values_2D:
            estimate_2D = monte_carlo_integration_2(f_2D, a_2, b_2, N)
            estimates_2D.append(estimate_2D)
            errors_2D.append(abs(estimate_2D - exact_value_2D))

        # Convergence plot
        st.subheader("Convergence of 2D Integral Estimation")
        convergence_of_integral(N_values_2D, estimates_2D, exact_value_2D)

        # Error plot
        st.subheader("Error Analysis")
        error_analysis(N_values_2D, errors_2D)
        
        # Visualize the 2D function and Monte Carlo points
        st.subheader("2D Function Visualization with Monte Carlo Points")
        visualize_2D_integration(f_2D, a_2, b_2, N)


        # Final result
        st.write(f"Estimated 2D Integral with N={N_values_2D[-1]}: {estimates_2D[-1]}")

elif section == "Error Analysis":
    st.header("1D Error Analysis for Monte Carlo Methods")
    selected_function = st.selectbox("Select a 1D function:", list(predefined_functions.keys()))
    a = st.number_input("Start of the range (a):", value=0.0)
    b = st.number_input("End of the range (b):", value=1.0)
    min_N = st.number_input("Minimum N:", value=10, min_value=1, max_value=100000)
    max_N = st.number_input("Maximum N:", value=10000, min_value=1, max_value=1000000)
    step_N = st.number_input("Step size for plot:", value=100, min_value=1, max_value=1000)
    
    N_values = [i for i in range(int(min_N), int(max_N) + 1, int(step_N))]

    if st.button("Run Error Analysis"):
        f = predefined_functions[selected_function]
        estimates = []
        theoretical_errors = []
        exact_errors = []
        exact_value = exact_integral_1(f, a, b)
        for N in N_values:
            estimate, theoretical_error, _ = monte_carlo_error_analysis_1D(f, a, b, N)
            estimates.append(estimate)
            theoretical_errors.append(theoretical_error)
            exact_errors.append(abs(estimate - exact_value))

        # Error plot
        st.subheader("Theoretical vs. Exact Error")
        plot_error(N_values, theoretical_errors, exact_errors)

        # Final results
        st.write(f"Estimated Integral with N={N_values[-1]}: {estimates[-1]}")
        st.write(f"Exact Integral: {exact_value}")
        st.write(f"Theoretical Error Bound: {theoretical_errors[-1]}")
        st.write(f"Exact Error: {exact_errors[-1]}")
        
        
    st.header("2D Error Analysis for Monte Carlo Methods")
    selected_function = st.selectbox("Select a 2D function:", list(predefined_2D_functions.keys()))
    a = st.number_input("Start (a):", value=0.0)
    b = st.number_input("End (b):", value=1.0)
    min_N = st.number_input("Minimum Value of N:", value=10, min_value=1, max_value=100000)
    max_N = st.number_input("Maximum Value N:", value=10000, min_value=1, max_value=1000000)
    step_N = st.number_input("Step size for the plot:", value=100, min_value=1, max_value=1000)
    
    N_values = [i for i in range(int(min_N), int(max_N) + 1, int(step_N))]

    if st.button("Run 2D Error Analysis"):
        f = predefined_2D_functions[selected_function]
        estimates = []
        theoretical_errors = []
        exact_errors = []
        exact_value = exact_integral_2D(f, a, b)
        for N in N_values:
            estimate, theoretical_error, _ = monte_carlo_error_analysis_2D(f, a, b, N)
            estimates.append(estimate)
            theoretical_errors.append(theoretical_error)
            exact_errors.append(abs(estimate - exact_value))

        st.subheader("Theoretical vs. Exact Error")
        plot_error(N_values, theoretical_errors, exact_errors)

        st.write(f"Estimated Integral with N={N_values[-1]}: {estimates[-1]}")
        st.write(f"Exact Integral: {exact_value}")
        st.write(f"Theoretical Error Bound: {theoretical_errors[-1]}")
        st.write(f"Exact Error: {exact_errors[-1]}")

        