import numpy as np
import matplotlib.pyplot as plt

# Definición de los coeficientes y entrada
r1 = 10
r2 = 10
v = 10

def u(t):
    return v * np.sin(2 * np.pi * t)

def desplazamiento(t):
    return u(t+90)
# Ecuación diferencial
def model(t):
    return desplazamiento(t) *(- r2 / r1)

# Parámetros de la simulación
t = np.linspace(0, 2, 200)

# Gráfica de los resultados
plt.plot(t, u(t), label='Señal de Entrada')
plt.plot(t, model(t), label='Señal de Salida')
plt.xlabel('Tiempo t')
plt.ylabel('Respuesta y(t)')
plt.title('Sistema con desplazamiento e inversión')
plt.legend()
plt.grid()
plt.show()