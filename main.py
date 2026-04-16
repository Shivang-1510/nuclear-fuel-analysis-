import numpy as np
import matplotlib.pyplot as plt

# Energy released per fission (MeV)
fuel_data = {
    "U-235": 200,
    "Pu-239": 210,
    "Th-232": 190
}

# Convert MeV to Joules (1 MeV = 1.602e-13 J)
MEV_TO_J = 1.602e-13

# Avogadro's number
NA = 6.022e23

# Atomic masses (g/mol)
atomic_mass = {
    "U-235": 235,
    "Pu-239": 239,
    "Th-232": 232
}

def energy_per_kg(fuel):
    energy_mev = fuel_data[fuel]
    energy_joule = energy_mev * MEV_TO_J
    
    atoms_per_kg = (1000 / atomic_mass[fuel]) * NA
    total_energy = atoms_per_kg * energy_joule
    
    return total_energy / 1e12  # Convert to TJ

# Calculate energy for each fuel
fuels = list(fuel_data.keys())
energies = [energy_per_kg(f) for f in fuels]

# Print results
for f, e in zip(fuels, energies):
    print(f"{f}: {e:.2f} TJ/kg")

# Plot results
plt.figure()
plt.bar(fuels, energies)
plt.xlabel("Fuel Type")
plt.ylabel("Energy (TJ/kg)")
plt.title("Energy Output of Nuclear Fuels")
plt.show()
