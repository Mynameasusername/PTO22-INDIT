import numpy as np
import matplotlib.pyplot as plt
import math

# Genauigkeit vom Benutzer eingeben lassen
genauigkeit = float(input("Bitte geben Sie die Genauigkeit in Grad ein: "))

# Grad von 0 bis 360 in Schritten entsprechend der Genauigkeit erstellen
x = np.arange(0, 360, genauigkeit)

# Grad in Radiant umwandeln
x_rad = np.deg2rad(x)

# Sinuswerte berechnen
y = np.sin(x_rad)

# Plot erstellen
plt.plot(x, y)
plt.title('Sinusfunktion')
plt.xlabel('Grad')
plt.ylabel('Sinus')
plt.grid(True)

# Gradgenauigkeit anzeigen
plt.xticks(np.arange(0, 360, genauigkeit))

# Plot anzeigen
plt.show()