import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from scipy.integrate import quad

#calculating luminosity distance for a flat cosmology based on distances to SNe Ia 
#outputs a plot for three cosmologies below

class Luminosity_Distance:
    
    def __init__(self, matter, dark_energy):
        self.dark_energy = dark_energy
        self.matter = matter
        self.redshift = np.linspace(0,5,100)
           
    def integral(self, x):
        self.x = x
        return (1/sqrt(self.matter*(1+self.x)**(3)+self.dark_energy))

    def calculation(self):
        res = []
        for i in self.redshift:
            res.append(quad(self.integral, 0, i))

        integral_results = []
        for i in range(0,len(res)):
            integral_results.append(res[i][0])

        angular_distance = []
        for i in range(0,len(integral_results)):
            calc = integral_results[i]/(1+self.redshift[i])
            angular_distance.append(calc)

        luminosity_distance = []
        for i in range(0, len(angular_distance)):
            calc2 = ((1+self.redshift[i])**2)*angular_distance[i]
            luminosity_distance.append(calc2)

        return luminosity_distance
 
#three cosmologies
matter = [0.3, 1, 0.25]
dark_energy = [0, 0, 0.75]
redshift = np.linspace(0,5,100)

DL_1 = Luminosity_Distance(matter[0], dark_energy[0])
DL_2 = Luminosity_Distance(matter[1], dark_energy[1])
DL_3 = Luminosity_Distance(matter[2], dark_energy[2])

plt.plot(redshift, DL_1.calculation(), color='blue', linestyle='dotted', label='Ωm = 0.3, Ωde = 0')
plt.plot(redshift, DL_2.calculation(), color='blue', label='Ωm = 1,  Ωde = 0')
plt.plot(redshift, DL_3.calculation(), color='blue', linestyle='--', label='Ωm = 0.25, Ωde = 0.75')
plt.xlabel("redshift z")
plt.ylabel("luminosity distance")
plt.legend(loc='best')
plt.show()
