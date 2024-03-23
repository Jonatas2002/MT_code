import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from function import MT_Notch_filter
from function import load_data

# Abrindo o Arquivo
Ex, Ey, Hx, Hy, Hz = load_data("example_1h.txt")

# Parametros
fs = 128

# Parametros do filtro
f0 = 60.0  # Frequência a ser removida do sinal (Hz)
Q = 80.0  # Fator de qualidade

b, a = signal.iirnotch(f0, Q, fs)   # Primeiro filtro

# Aplicando o Filtro
Exf = signal.filtfilt(b, a, Ex) # Primeiro Filtro - Sinal filtrado de 60 Hz
Eyf = signal.filtfilt(b, a, Ey) # Primeiro Filtro - Sinal filtrado de 60 Hz
Hxf = signal.filtfilt(b, a, Hx) # Primeiro Filtro - Sinal filtrado de 60 Hz
Hyf = signal.filtfilt(b, a, Hy) # Primeiro Filtro - Sinal filtrado de 60 Hz
Hzf = signal.filtfilt(b, a, Hz) # Primeiro Filtro - Sinal filtrado de 60 Hz

# ----------------------------------------------------------------------------------
title = ["Campo Elétrico - Eixo X", "Campo Elétrico - Eixo Y", "Campo Magnético - Eixo X", "Campo Magnético - Eixo Y", "Campo Magnético - Eixo Z" ]
MT_Notch_filter(title[0], Ex, Exf, fs)
MT_Notch_filter(title[1], Ey, Eyf, fs)
MT_Notch_filter(title[2], Hx, Hxf, fs)
MT_Notch_filter(title[3], Hy, Hyf, fs)
MT_Notch_filter(title[4], Hz, Hzf, fs)