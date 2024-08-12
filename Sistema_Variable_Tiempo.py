import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros del sistema
m = 10  # Masa (kg)
c = 1  # Coeficiente de amortiguamiento (kg/s)

# Condiciones iniciales: desplazamiento y velocidad iniciales
y0 = [0.0, 0.0]

# Función que define la constante del resorte variable en el tiempo
def k(t):
    return t

# Función que define la ecuación diferencial
def sistema_masa_resorte_variable(t, y):
    x, v = y
    dxdt = v
    dvdt = (F(t) - c*v - k(t)*x) / m
    return [dxdt, dvdt]

# Fuerza externa aplicada
def F(t):
    return 1.0 

# Tiempo de simulación
t_span = (0, 100)
t_eval = np.linspace(0, 100, 1000)

# Resolver la ecuación diferencial
sol = solve_ivp(sistema_masa_resorte_variable, t_span, y0, t_eval=t_eval)

# Graficar el desplazamiento y la velocidad
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(sol.t, sol.y[0], label='Desplazamiento (x)')
plt.title('Sistema Masa-Resorte-Amortiguador con Resorte Variable')
plt.ylabel('Desplazamiento (m)')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(sol.t, sol.y[1], label='Velocidad (v)', color='orange')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()