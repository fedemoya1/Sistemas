import numpy as np
import matplotlib.pyplot as plt

# Definición de los coeficientes y entrada
def entradas(t):
    signal1 = np.sin(2 * np.pi * 2 * t)
    signal2 = 3 * np.sin(2 * np.pi * 3 * t)
    signal3 = 5 * np.sin(2 * np.pi * 5 * t)
    return signal1 + signal2 + signal3

# Ecuación diferencial
def Entradas_Sumadas(t):
    return entradas(t)

# Parámetros de la simulación
t = np.linspace(0, 5, 300)

# Gráfica de los resultados
plt.figure(figsize=(10,8))

plt.subplot(4, 1, 1)
plt.plot(t, np.sin(2 * np.pi * 2 * t))
plt.title('y = sin(4*pi*t); t > 0')
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t, 3 * np.sin(2 * np.pi * 3 * t))
plt.title('y = 3* sin(6*pi*t); t > 0')
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t, 5 * np.sin(2 * np.pi * 5 * t))
plt.title('y = 5*sin(10*pi*t); t > 0')
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t, Entradas_Sumadas(t), label='Señal de Salida')
plt.title('y = sin(4*pi*t); t > 0')
plt.grid(True)
plt.xlabel('Tiempo t')
plt.ylabel('Respuesta y(t)')
plt.title('Sistema con entradas sumadas')

plt.tight_layout()
plt.legend()
plt.grid()
plt.show()