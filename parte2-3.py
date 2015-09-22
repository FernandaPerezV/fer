#Este programa realiza la integral con el metodo de los trapecios la integral del 
#en longitud de onda.

import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from math import pi
from astropy import constants as const

#cargamos los datos
datos=np.loadtxt('sun_AM0.dat')
x=datos[:,0]*u.nm
y=datos[:,1]*u.W*((u.m)**-2)*((u.nm)**-1)


wavel=x.to('um')
flujo=y.to('erg / (s cm2 um)')
n=len(wavel)

integral=0
for i in range(n-1):
 dx=wavel[i+1]-wavel[i]
 sumy=flujo[i]+flujo[i+1]
 integral+=0.5*dx*sumy

print ("(cte solar) integral del espectro en longitud de onda=", integral)



#Ahora calculamos la luminosidad total del sol (energia por unidad de tiempo) tomando como 
#conocida la distancia de la tierra al sol (1 unidad astronómica).

A=1*u.AU
a=(A**2).to('cm2')
luminosidad=4*np.pi*a*integral



print ('luminosidad total del sol=', luminosidad)

#
# union programa parte 3
#
#
T=5778*u.K

def f(y):
 return ((np.tan(y))**3)* (1+(np.tan(y))**2) / ( np.exp(np.tan(y))-1)


n=input('escoja n par positivo y menor a 1600, n=') #aquí se escoge n par mayor a cero
x0=0.0001
xf=pi/2

dx = (xf-x0)/n
x = x0
suma = 0

for i in range(n/2):
 suma += f(x) + 4.*f(x+dx) + f(x+2*dx)
 x += 2*dx

integral=(dx/3.)*suma
integralPlanck=( (2*pi*const.h/const.c**2) * ((const.k_B*(5778*u.K)/const.h)**4) ) * integral
print('energia por unidad de tiempo y area de un cuerpo negro (con Teff_sol=5778K)=', integralPlanck.to('erg / (s cm2)'))


cte_b= (integralPlanck/(T**4)).to('erg/(s cm2 K4)')

R_sol=( luminosidad / (4*np.pi*cte_b*(T**4)) )**(0.5)
                 
R=R_sol.to('km')

print('Radio efectivo sol=', R)







