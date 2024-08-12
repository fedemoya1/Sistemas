import numpy as np
import matplotlib.pyplot as plt

def u(t):
    return np.sin(2*np.pi*3*t)

# Parámetros de la simulación
t = np.linspace(0, 2, 200)

# Gráfica de los resultados
plt.plot(t, u(t+np.pi/2), label='Señal desplazada')
plt.plot(t, u(t), label='Señal de Entrada')
plt.xlabel('Tiempo t')
plt.ylabel('Respuesta y(t)')
plt.title('Señal con desplazamiento en el tiempo')
plt.legend()
plt.grid()
plt.show()
