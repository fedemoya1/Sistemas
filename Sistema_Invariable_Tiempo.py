import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Parámetros
r = 1 # 1 ohm
c = 1 # 1 Faradio
v = 12 # Voltaje de entrada 12 volts

tau = r*c

t = np.linspace(0, 10, 100)

def model(V, t, tau, V_in):
    dVdt = (V_in - V) / (tau)
    return dVdt

# Condiciones iniciales
V0 = 0  # Voltaje inicial en el capacitor

# Resolver ODE
V = odeint(model, V0, t, args=(tau, v))

# Gráfica del resultado
plt.plot(t, V, label='Voltaje del Capacitor')
plt.xlabel('Tiempo t')
plt.ylabel('Respuesta V(t)')
plt.title('Circuito RC con Voltaje de entrada Constante')
plt.legend()
plt.grid()
plt.show()