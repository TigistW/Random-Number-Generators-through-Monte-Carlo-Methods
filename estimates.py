import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.integrate import quad, dblquad
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


predefined_functions = {
    "e^(-x^2)": lambda x: np.exp(-x**2),
    "sin(x)": lambda x: np.sin(x),
    "x^2": lambda x: x**2,
    "cos(x)": lambda x: np.cos(x)
}

predefined_2D_functions = {
    "e^{-(x^2 + y^2)}": lambda x, y: np.exp(-(x**2 + y**2)),
    "sin(x) * cos(y)": lambda x, y: np.sin(x) * np.cos(y),
    "x^2 + y^2": lambda x, y: x**2 + y**2,
    "sin(x + y)": lambda x, y: np.sin(x + y)
}

def estimate_pi(N):
    x = np.random.uniform(0, 1, N)
    y = np.random.uniform(0, 1, N)
    inside_circle = (x**2 + y**2) <= 1
    pi_estimate = 4 * np.sum(inside_circle) / N
    return pi_estimate, x, y, inside_circle

def monte_carlo_integration_1(f, a, b, N):
    x = np.random.uniform(a, b, N)
    integral = (b - a) * np.mean(f(x))
    return integral, x, f(x)

def exact_integral_1(f, a, b):
    result, _ = quad(f, a, b)
    return result

def monte_carlo_integration_2(f, a, b, N):
    x = np.random.uniform(a, b, N)
    y = np.random.uniform(a, b, N)
    integral = (b - a) * (b - a) * np.mean(f(x, y))
    return integral

def plot_circle_and_points(x, y, inside_circle, N):
    
        fig, ax = plt.subplots(figsize=(6, 6))
        theta = np.linspace(0, 2 * np.pi, 1000)
        ax.plot(np.cos(theta), np.sin(theta), label="Unit Circle", color="red")
        ax.scatter(x[inside_circle], y[inside_circle], color="blue", s=1, label="Inside Circle")
        ax.scatter(x[~inside_circle], y[~inside_circle], color="orange", s=1, label="Outside Circle")
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.legend()
        st.pyplot(fig)
        
def plot_pi_convergence(N_values):
    pi_actual = np.pi
    pi_estimates = []
    errors = []
    
    for N in N_values:
        pi_estimate = estimate_pi(N)[0]
        error = abs(pi_estimate - pi_actual)
        pi_estimates.append(pi_estimate)
        errors.append(error)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(N_values, pi_estimates, marker='o', label="Estimated π", linestyle='-', color='blue')
    ax.axhline(y=pi_actual, color='red', linestyle='--', label="Actual π")
    ax.plot(N_values, errors, marker='x', label="Error", linestyle='-', color='orange')

    ax.set_xscale('log')
    ax.set_xlabel("Number of Points (N)")
    ax.set_ylabel("Value/Error")
    ax.set_title("Convergence and Error of π Estimation Using Monte Carlo")
    ax.legend()
    ax.grid()
    st.pyplot(fig)
    
def convergence_of_integral(N_values, estimates, exact_value):
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(N_values, estimates, marker='o', label="Estimated Integral", color='blue')
    ax1.axhline(y=exact_value, color='red', linestyle='--', label="Exact Integral")
    ax1.set_xscale('log')
    ax1.set_xlabel("Number of Points (N)")
    ax1.set_ylabel("Estimated Integral")
    ax1.set_title("Convergence of 1D Integral Estimation")
    ax1.legend()
    ax1.grid()
    st.pyplot(fig1)

def error_analysis(N_values, errors):
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.plot(N_values, errors, marker='x', label="Error", color='orange')
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xlabel("Number of Points (N)")
    ax2.set_ylabel("Error")
    ax2.set_title("Error of 1D Integral Estimation")
    ax2.legend()
    ax2.grid()
    st.pyplot(fig2)

def visualize_1D_integration(x, y,a_1, b_1, f, N, estimates):
    x_curve = np.linspace(a_1, b_1, 500)
    y_curve = f(x_curve)
    # Plot the function and Monte Carlo points
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_curve, y_curve, label="f(x)", color="blue")
    ax.scatter(x, y, color="red", s=5, alpha=0.5, label="Monte Carlo Points")
    ax.fill_between(x_curve, 0, y_curve, color="blue", alpha=0.2, label="Area under f(x)")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(a_1, color="black", linestyle="--", linewidth=0.8)
    ax.axvline(b_1, color="black", linestyle="--", linewidth=0.8)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(f"Monte Carlo Integration\nEstimated Integral ≈ {estimates[-1]:.5f}")
    ax.legend()
    ax.grid()
    st.pyplot(fig)

def exact_integral_2D(f, a, b):
    result, _ = dblquad(f, a, b, lambda x: a, lambda x: b)
    return result
    
def visualize_2D_integration(f, a, b, N):
    x = np.linspace(a, b, 100)
    y = np.linspace(a,b, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.scatter(x, y, f(x,y), color='red', s=5, alpha=0.5, label="Monte Carlo Points")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.set_title('Monte Carlo Integration - 2D')
    ax.legend()
    ax.grid()
    st.pyplot(fig)
    # plt.show()
