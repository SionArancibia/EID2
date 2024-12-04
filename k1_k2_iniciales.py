import numpy as np

from scipy.integrate import solve_ivp

import pandas as pd



# Parámetros del modelo

k1 = 0.106  # min^-1

k2 = -0.0585  # min^-2

Tamb = 18  # Temperatura ambiente en °C



# Condiciones iniciales

T0 = 65  # Temperatura inicial en °C

dTdt0 = -5  # Derivada inicial en °C/min



# Tiempo de medición experimental

tiempo_exp = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])  # minutos

temperatura_exp = np.array([65, 55, 47, 46, 45, 45, 44, 46, 44, 45])  # °C



# Sistema de ecuaciones diferenciales de primer orden

def edo_sistema(t, y):

    T, dTdt = y

    d2Tdt2 = -k1 * dTdt - k2 * (T - Tamb)

    return [dTdt, d2Tdt2]



# Resolver el sistema de ecuaciones

sol = solve_ivp(

    edo_sistema,

    t_span=(tiempo_exp[0], tiempo_exp[-1]),

    y0=[T0, dTdt0],

    t_eval=tiempo_exp,

    method='RK45'

)



# Resultados teóricos

temperatura_teorica = sol.y[0]



# Crear tabla de comparación

tabla_comparacion = pd.DataFrame({

    "Tiempo (min)": tiempo_exp,

    "Temperatura Experimental (°C)": temperatura_exp,

    "Temperatura Teórica (°C)": temperatura_teorica

})


print(tabla_comparacion)