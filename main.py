"""
Nuclear Fuel Energy Analysis

This module calculates the energy released per kilogram of various nuclear fuels
during fission reactions and provides visualization of the results.
"""

from typing import Dict, List
import numpy as np
import matplotlib.pyplot as plt

# === Constants ===

# Energy released per fission (MeV)
FUEL_ENERGY_DATA: Dict[str, int] = {
    "U-235": 200,
    "Pu-239": 210,
    "Th-232": 190,
}

# Convert MeV to Joules (1 MeV = 1.602e-13 J)
MEV_TO_JOULES = 1.602e-13

# Avogadro's number (atoms/mol)
AVOGADRO_NUMBER = 6.022e23

# Atomic masses (g/mol)
ATOMIC_MASS: Dict[str, int] = {
    "U-235": 235,
    "Pu-239": 239,
    "Th-232": 232,
}

# Energy conversion factor (Joules to Terajoules)
TERAJOULES_CONVERSION = 1e12


# === Core Functions ===

def energy_per_kg(fuel: str) -> float:
    """
    Calculate the total energy released per kilogram of nuclear fuel.
    
    Args:
        fuel (str): The name of the nuclear fuel (e.g., "U-235", "Pu-239").
    
    Returns:
        float: Energy in TJ/kg (Terajoules per kilogram).
    
    Raises:
        ValueError: If the fuel type is not recognized.
    
    Example:
        >>> energy_per_kg("U-235")
        82345.67
    """
    if fuel not in FUEL_ENERGY_DATA:
        raise ValueError(
            f"Unknown fuel: {fuel}. Available fuels: {list(FUEL_ENERGY_DATA.keys())}"
        )
    
    # Energy per fission in Joules
    energy_mev = FUEL_ENERGY_DATA[fuel]
    energy_joules_per_fission = energy_mev * MEV_TO_JOULES
    
    # Number of atoms per kilogram
    moles_per_kg = 1000 / ATOMIC_MASS[fuel]
    atoms_per_kg = moles_per_kg * AVOGADRO_NUMBER
    
    # Total energy in Joules per kilogram
    total_energy_joules = atoms_per_kg * energy_joules_per_fission
    
    # Convert to Terajoules
    return total_energy_joules / TERAJOULES_CONVERSION


def calculate_all_fuels() -> tuple[List[str], List[float]]:
    """
    Calculate energy output for all available nuclear fuels.
    
    Returns:
        tuple: A tuple containing (fuel_names, energies) lists.
    
    Example:
        >>> fuels, energies = calculate_all_fuels()
        >>> for fuel, energy in zip(fuels, energies):
        ...     print(f"{fuel}: {energy:.2f} TJ/kg")
    """
    fuels = list(FUEL_ENERGY_DATA.keys())
    energies = [energy_per_kg(fuel) for fuel in fuels]
    return fuels, energies


def print_results(fuels: List[str], energies: List[float]) -> None:
    """
    Print nuclear fuel energy analysis results in a formatted table.
    
    Args:
        fuels (List[str]): List of fuel names.
        energies (List[float]): List of energy values in TJ/kg.
    """
    print("\n" + "=" * 50)
    print("Nuclear Fuel Energy Analysis Results")
    print("=" * 50)
    print(f"{'Fuel Type':<15} {'Energy (TJ/kg)':<20}")
    print( "-" * 50)
    
    for fuel, energy in zip(fuels, energies):
        print(f"{fuel:<15} {energy:>18.2f}")
    
    print("=" * 50 + "\n")


def visualize_results(
    fuels: List[str],
    energies: List[float],
    save_path: str = None,
    show_plot: bool = True,
) -> None:
    """
    Create a bar chart visualization of fuel energy output.
    
    Args:
        fuels (List[str]): List of fuel names.
        energies (List[float]): List of energy values in TJ/kg.
        save_path (str, optional): Path to save the figure. If None, no save occurs.
        show_plot (bool): Whether to display the plot. Default is True.
    
    Example:
        >>> fuels, energies = calculate_all_fuels()
        >>> visualize_results(fuels, energies, save_path="fuel_energy.png")
    """
    plt.figure(figsize=(10, 6))
    bars = plt.bar(fuels, energies, color=["#FF6B6B", "#4ECDC4", "#45B7D1"])
    
    # Add value labels on top of bars
    for bar, energy in zip(bars, energies):
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{energy:.2f}",
            ha="center",
            va="bottom",
            fontweight="bold",
        )
    
    plt.xlabel("Fuel Type", fontsize=12, fontweight="bold")
    plt.ylabel("Energy (TJ/kg)", fontsize=12, fontweight="bold")
    plt.title("Energy Output of Nuclear Fuels", fontsize=14, fontweight="bold")
    plt.grid(axis="y", alpha=0.3, linestyle="--")
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Plot saved to: {save_path}")
    
    if show_plot:
        plt.show()


# === Main Execution ===

def main() -> None:
    """Main entry point for the nuclear fuel analysis."""
    try:
        # Calculate energy for all fuels
        fuels, energies = calculate_all_fuels()
        
        # Display results
        print_results(fuels, energies)
        
        # Visualize results
        visualize_results(fuels, energies, show_plot=True)
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        raise


if __name__ == "__main__":
    main()