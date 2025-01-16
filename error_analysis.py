
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def monte_carlo_error_analysis_1D(f, a, b, N):
    x_samples = np.random.uniform(a, b, N)
    f_values = f(x_samples)
    integral = (b - a) * np.mean(f_values)
    sigma = np.std(f_values)
    error_bound = (b - a) * sigma / np.sqrt(N) 
    return integral, error_bound, f_values

def monte_carlo_error_analysis_2D(f, a, b, N):
   
    x_samples = np.random.uniform(a, b, N)
    y_samples = np.random.uniform(a, b, N)
    f_values = f(x_samples, y_samples)
    area = (b - a) * (b-a)
    integral = area * np.mean(f_values)
    sigma = np.std(f_values)
    error_bound = area * sigma / np.sqrt(N)
    return integral, error_bound, f_values


def plot_error(N_values, theoretical_errors, exact_errors, title="Error Analysis"):

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(N_values, theoretical_errors, label="Theoretical Error", linestyle='--', color='orange')
    ax.plot(N_values, exact_errors, label="Exact Error", linestyle='-', color='blue')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel("Number of Points (N)")
    ax.set_ylabel("Error")
    ax.set_title(title)
    ax.legend()
    ax.grid()
    plt.tight_layout()
    st.pyplot(fig)