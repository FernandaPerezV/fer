import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u


datos=np.loadtxt('sun_AM0.dat')
x=datos[:,0]*u.nm
y=datos[:,1]*u.W*((u.m)**-2)*((u.nm)**-1)
wavel=x.to('um')
flujo=y.to('erg / (s cm2 um)')
plt.plot(wavel,flujo)
plt.xlim(0.,6.)
plt.xlabel('Longitud de onda $[\mu m]$')
plt.ylabel('Flujo $[erg$ $ s^{-1} cm^{-2} \mu m^{-1}]$')
plt.title('Espectro solar, flujo v/s longitud de onda')
plt.grid(True)

plt.savefig('parte1.png',bbox_inches='tight')
plt.show()
