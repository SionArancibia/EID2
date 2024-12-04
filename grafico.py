# Reimportando las librerías debido al reinicio del entorno
import matplotlib.pyplot as plt
import numpy as np

# Datos experimentales
tiempo_exp = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])  # minutos
temperatura_exp = np.array([65, 55, 47, 46, 45, 45, 44, 46, 44, 45])  # °C

# Datos ajustados (teóricos finales)
temperatura_teorica_final = np.array([65, 56.65, 50.99, 47.32, 45.09, 43.94, 43.60, 43.89, 44.67, 45.85])

# Datos teóricos de la tabla dada
tiempo_tabla = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])  # minutos
temperatura_teorica_tabla = np.array([65, 55, 47.1, 40.9, 36.1, 32.2, 29.2, 26.8, 24.9, 23.4])  # °C

# Graficar los valores experimentales vs. los ajustados y los teóricos de la tabla
plt.figure(figsize=(10, 6))

# Datos experimentales
plt.plot(tiempo_exp, temperatura_exp, 'o-', label='Datos Experimentales', color='blue')

# Datos ajustados
plt.plot(tiempo_exp, temperatura_teorica_final, 's-', label='Teóricos con EDO extendida (k1 y k2 optimizados)', color='green')

# Datos teóricos de la tabla
plt.plot(tiempo_tabla, temperatura_teorica_tabla, 'd--', label='Teóricos con EDO tradicional', color='red')

# Configuración del gráfico
plt.title('Comparativa Resultados teóricos / experimentales de la Ley de enfriamiento de Newton')
plt.xlabel('Tiempo (min)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.show()
