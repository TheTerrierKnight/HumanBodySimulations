import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 0.21  # Inspired oxygen fraction
alpha = 1.2  # Haldane constant for CO2
V_T = 0.5  # Tidal volume (L)
f = 0.2  # Breathing frequency (Hz)
T = 1 / f  # Breathing period (s)
R_aw = 1.5  # Resistance of the airways (cmH2O.s.L^-1)
C_st = 0.06  # Compliance of the chest wall (L.cmH2O^-1)
C_lung = 0.1  # Compliance of the lung (L.cmH2O^-1)
P_atm = 101325  # Atmospheric pressure (Pa)

# Time vector
t = np.linspace(0, T, int(T * 100))

# Airway pressure
P_aw = 0
for i in range(len(t) - 1):
    if t[i] < T / 2:
        P_aw += R_aw * V_T * f * np.heaviside(t[i + 1] - t[i] - 1 / (4 * f), 0)
    else:
        P_aw -= R_aw * V_T * f * np.heaviside(t[i + 1] - t[i] - 1 / (4 * f), 0)

# Alveolar pressure
P_A = P_aw + (P_atm - P_aw) * np.exp(-(t - T / 2) / np.sqrt(C_lung * R_aw))

# Chest wall volume
V_chest = C_st * (P_atm - P_A)

# Lung volume
V_lung = C_lung * P_A

# Inspired oxygen concentration
F_IO2 = R * (P_atm - P_A) / (R * (P_atm - P_A) + (1 - R) * P_A)

# CO2 production
V_CO2 = 0.00025  # L/min

# Arterial oxygen concentration
P_aO2 = F_IO2 * (P_atm - P_A)

# Arterial CO2 concentration
P_aCO2 = alpha * V_CO2 / V_T / f

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

axs[0, 0].plot(t, np.full_like(t, P_aw), label='Airway pressure')
axs[0, 0].set_xlabel('Time (s)')
axs[0, 0].set_ylabel('Pressure (cmH2O)')
axs[0, 0].legend()

axs[0, 1].plot(t, np.full_like(t, P_A), label='Alveolar pressure')
axs[0, 1].set_xlabel('Time (s)')
axs[0, 1].set_ylabel('Pressure (cmH2O)')
axs[0, 1].legend()

axs[1, 0].plot(t, np.full_like(t, V_chest), label='Chest wall volume')
axs[1, 0].set_xlabel('Time (s)')
axs[1, 0].set_ylabel('Volume (L)')
axs[1, 0].legend()

axs[1, 1].plot(t, np.full_like(t, V_lung), label='Lung volume')
axs[1, 1].set_xlabel('Time (s)')
axs[1, 1].set_ylabel

plt.show()