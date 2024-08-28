"""
This script estimates expectation values for the position
x for four given wave functions. It also plots them.

Inputs:
   PsiFunk - The expression for the unnormalized wave function.
   L       - The extension of the spatial grid 
   N       - The number of grid points

Inputs are hard coded initialy, and the function in question is 
selected by commenting in and out the adequate lines.
"""

# Import libraries (numpy and matplotlib)
import numpy as np
from matplotlib import pyplot as plt


a = 1
b = 2


# Unnormalzied wave functions (Comment in and out as fit)
def  PsiFunk(x):
  # Psi_A:
  return 1/(1+(x-3)**2)**(3/2)
  # Psi_B:
  #return np.exp(-x**2)
  # Psi_C:
  #return np.exp(-x**2)
  # Psi_D:
  #return (x+1j)*np.exp(-(x-3j-2)**2/10)

# Numerical grid parameters
L = 20
N = 10000

# Set up grid
x = np.linspace(-L/2, L/2, N)
h = x[1]-x[0]
Psi = PsiFunk(x)                 # Vector with function values

# Normalization
Norm = np.sqrt(np.trapz(np.abs(Psi)**2, dx = h))
print(Norm)
Psi = Psi/Norm  #multiplying c with psi to make the infinite integral = 1

# Calculate mean position and write result to screen
#3
index_of_max_Psi=np.argmax(np.abs(Psi))
x_max_Psi = x[index_of_max_Psi]
print(f'Most likely position: {x_max_Psi:.4f}')

#4
MeanX = np.trapz(x*np.abs(Psi)**2, x)
print(f'Mean position: {MeanX:.4f}' )

Prob = np.trapz((x>a)*(x<b)*np.abs(Psi)**2, x)
print(f'Probability: {Prob*100:.2f} %')


Psi_D_Deriv = np.zeros(N, dtype=complex)             # Allocate and declare
# End points (assume Psi = 0 outside the interval)
Psi_D_Deriv[0] =  (Psi[1])/(h**2)
Psi_D_Deriv[N-1] = -Psi[N-1]/(h**2)
# Estimate the derivative with the midpoint rule
for n in range(1,N-1):
  Psi_D_Deriv[n] = (Psi[n-1]-2*Psi[n]+Psi[n+1])/(h**2)

Mean_P_X = -np.trapz(np.abs(Psi)*np.abs(Psi_D_Deriv), x)
print(Mean_P_X)


















# Make plot
plt.figure(1)
plt.clf()
plt.plot(x, np.abs(Psi)**2, '-', color='black', label = r'$|\Psi|^2$')
plt.xlabel('x')

# Check if Psi is complex and, if so, plot real and imaginary contributions
if np.max(np.abs(np.imag(Psi)))>1e-7:     
  plt.plot(x, np.real(Psi)**2, '--', color = 'blue', 
           label = r'$(Re \; \Psi)^2$')
  plt.plot(x, np.imag(Psi)**2, '-.', color='red', label = r'$(Im \; \Psi)^2$')
  plt.legend()

plt.grid()
plt.show()









