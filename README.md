# Nuclear Fuel Energy Analysis

## Overview

This project performs a computational analysis of energy output from key nuclear fuels: Uranium-235, Plutonium-239, and Thorium-232. The goal is to compare their energy density and evaluate their suitability for nuclear power generation.

## Objectives
* Compute energy output (TJ/kg) for different nuclear fuels
* Compare efficiency based on energy density
* Visualize differences using graphical representation

## Theory
Energy released in nuclear fission is converted from MeV to Joules and scaled using Avogadro’s number to determine total energy per kilogram of fuel.

## Methodology
* Defined energy per fission for each fuel
* Converted MeV → Joules
* Calculated atoms per kg using atomic mass
* Computed total energy output
* Visualized results using Python

## Results

### Energy Output (Approx.)

* U-235 ≈ 82 TJ/kg
* Pu-239 ≈ 88 TJ/kg
* Th-232 ≈ 79 TJ/kg

## Visualization

![Energy Plot](nuclear-fuel-analysis- /results.png)

## Key Insights

* Pu-239 provides the highest energy output among the studied fuels
* U-235 is widely used due to stability and availability
* Th-232 shows strong potential for future thorium-based reactors

## Tools Used
* Python
* NumPy
* Matplotlib

## How to Run

```bash
pip install -r requirements.txt
python src/main.py
```


## Applications
* Nuclear fuel comparison studies
* Reactor design considerations
* Energy system modeling

## Future Work
* Include reactor efficiency modeling
* Add neutron economy analysis
* Extend to fuel burnup calculations

## Author

Shivang Arora
Energy Engineering Student | Nuclear Energy Enthusiast

