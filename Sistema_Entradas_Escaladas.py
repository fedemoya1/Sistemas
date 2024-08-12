import numpy as np
import matplotlib.pyplot as plt

# Definición de los coeficientes y entrada
r1 = 20
r2 = 10
v = 10

def u(t):
    return v * np.sin(2 * np.pi * t)

# Ecuación diferencial
def model(t):
    return u(t) *(1 + r2 / r1)

# Parámetros de la simulación
t = np.linspace(0, 2, 200)

# Gráfica de los resultados
plt.plot(t, u(t), label='Señal de Entrada')
plt.plot(t, model(t), label='Señal de Salida')
plt.xlabel('Tiempo t')
plt.ylabel('Respuesta y(t)')
plt.title('Sistema con entrada escalada')
plt.legend()
plt.grid()
plt.show()