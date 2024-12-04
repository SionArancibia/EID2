from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import numpy as np

#https://medium.com/@bldevries/simply-solving-differential-equations-using-python-scipy-and-solve-ivp-f6185da2572d

# Datos experimentales
tiempo_exp = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])  # minutos
temperatura_exp = np.array([65, 55, 47, 46, 45, 45, 44, 46, 44, 45])  # °C

# Condiciones iniciales
Tamb = 18  # Temperatura ambiente en °C
T0 = 65  # Temperatura inicial
dTdt0 = -5  # Derivada inicial estimada

# Función para calcular el error cuadrático dado k1 y k2
def error_cuadratico(params):
    k1_opt, k2_opt = params
    
    # Definir el sistema de ecuaciones diferenciales con los parámetros actuales
    def edo_sistema_opt(t, y):
        T, v = y  # v = dT/dt
        dvdt = -k1_opt * v - k2_opt * (T - Tamb)
        return [v, dvdt]
    
    # Resolver el sistema de ecuaciones
    sol_opt = solve_ivp(
        edo_sistema_opt,
        t_span=(0, tiempo_exp[-1]),  # Intervalo de tiempo
        y0=[T0, dTdt0],  # Condiciones iniciales
        t_eval=tiempo_exp,  # Puntos de evaluación
        method='RK45'
    )
    
    # Obtener la temperatura teórica
    temperatura_teorica_opt = sol_opt.y[0]
    
    # Calcular el error cuadrático
    error = np.sum((temperatura_teorica_opt - temperatura_exp)**2)
    return error

# Valores iniciales para la optimización
param_iniciales = [0.1, -0.05]  # Estimaciones iniciales de k1 y k2

# Realizar la optimización
resultado_opt = minimize(
    error_cuadratico,
    param_iniciales,
    bounds=[(0, 1), (-1, 0)],  # Límites razonables para k1 y k2
    method='L-BFGS-B'
)

# Extraer los valores óptimos
k1_opt, k2_opt = resultado_opt.x

# Mostrar resultados
print(f"Valores óptimos: k1 = {k1_opt:.4f}, k2 = {k2_opt:.4f}")

# Resolver el sistema con los parámetros óptimos para obtener la solución ajustada
def edo_sistema_final(t, y):
    T, v = y  # v = dT/dt
    dvdt = -k1_opt * v - k2_opt * (T - Tamb)
    return [v, dvdt]

sol_final = solve_ivp(
    edo_sistema_final,
    t_span=(0, tiempo_exp[-1]),
    y0=[T0, dTdt0],
    t_eval=tiempo_exp,
    method='RK45'
)

# Obtener la solución teórica ajustada
temperatura_teorica_final = sol_final.y[0]

# Mostrar la comparación entre los datos experimentales y teóricos
print("\nComparación de resultados:")
print("Tiempo (min) | Temp. Experimental (°C) | Temp. Teórica Ajustada (°C)")
for t, t_exp, t_teo in zip(tiempo_exp, temperatura_exp, temperatura_teorica_final):
    print(f"{t:12} | {t_exp:22} | {t_teo:27.2f}")
