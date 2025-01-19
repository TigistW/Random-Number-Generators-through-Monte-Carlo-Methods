# Monte Carlo Integration Web App

This Streamlit web application provides an interactive interface for performing numerical integration and error analysis using Monte Carlo methods. Users can estimate the value of π, evaluate 1D and 2D integrals, and analyze errors through visualization tools.

## Features

- **Estimation of π**
  - Estimate the value of π using Monte Carlo methods.
  - Visualize convergence and error analysis.
- **1D Numerical Integration**
  - Select predefined functions and calculate integrals using Monte Carlo methods.
  - View convergence plots and error analysis.
  - Visualize the integration process.
- **2D Numerical Integration**
  - Perform 2D Monte Carlo integration for selected functions.
  - Error analysis and convergence visualization.
  - Interactive plots for better understanding.
- **Error Analysis**
  - Compare theoretical vs. exact errors for 1D and 2D integration.
  - Visualize error trends over different sample sizes.

## Installation

To run the web application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/TigistW/Random-Number-Generators-through-Monte-Carlo-Methods.git
   cd monte-carlo-integration
   ```

2. Install the required dependencies:
```
- `streamlit`
- `numpy`
- `matplotlib`

```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the web app in your browser at `http://localhost:8501`.
2. Use the sidebar to navigate through the available sections:
   - "Estimation of π": Perform and visualize π estimation.
   - "1D Numerical Integration": Select a function and evaluate the integral.
   - "2D Numerical Integration": Perform 2D Monte Carlo integration.
   - "Error Analysis": Analyze integration error trends.
3. Adjust parameters like number of points, function selection, and integration ranges.
4. Click the appropriate buttons to run simulations and view results.

## Dependencies

The project requires the following Python libraries:

- `streamlit`
- `numpy`
- `matplotlib`

## File Structure

```
.
├── app.py                   # Main Streamlit application script
├── estimates.py             # Functions for Monte Carlo simulations
├── error_analysis.py        # Error analysis functions
├── README.md                # Documentation
```

## Author

[Tigist Wondimeh](https://github.com/TigistW)

