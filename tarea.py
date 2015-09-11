import numpy as np
import matplotlib.pyplot as plt


datos=np.loadtxt('sun_AM0.dat')
x=datos[:,0]
y=datos[:,1]
wavel=x*(10**-3)
flujo=y*(10**10)
plt.plot(wavel,flujo)
plt.xlim(0.,6.)
plt.xlabel('Longitud de onda $[\mu m]$')
plt.ylabel('Flujo $[erg$ $ s^{-1} cm{-3}]$')
plt.title('Espectro solar, flujo v/s longitud de onda')
plt.grid(True)
plt.savefig('fig1')
plt.show()

