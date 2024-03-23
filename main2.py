import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from function import MT_Notch_filter
from function import load_data

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
""" Este código realiza o pré-processamento dos dados magnetotelúricos, atenuando 
    ruídos coerentes conhecidos com o Filtro Notch, neste exemplo, um ruído de 60 Hz. 
    Basta o usuário preencher os parâmetros na 'ÁREA DE USO DO USUÁRIO' para que o 
    código seja executado.
    
    OBS 1: Evite modificar o script para evitar possíveis quebras no código.
    OBS 2: Este código está em desenvolvimento e futuramente será acrescentada 
           uma função para remoção de mais de um ruído."""
    
# ÁREA DE USO DO USUARIO:
DATA                = "Input/example_1h.txt"  # Input data
SAMPLING_RATE       = 128  # em Hz
FREQUENCY_REMOVED   = 60.0 # em Hz
QUALITY_FACTOR      = 80.0

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

""" !!!!! NÃO ALTERAR O CÓDIGO A PARTIR DESSA LINHA """
# Abrindo o Arquivo
Ex, Ey, Hx, Hy, Hz = load_data(DATA)

# Parametros
fs = SAMPLING_RATE

# Parametros do filtro
f0 = FREQUENCY_REMOVED  # Frequência a ser removida do sinal (Hz)
Q = QUALITY_FACTOR  # Fator de qualidade

b, a = signal.iirnotch(f0, Q, fs)   # Filtro

# Aplicando o Filtro
Exf = signal.filtfilt(b, a, Ex)
Eyf = signal.filtfilt(b, a, Ey) 
Hxf = signal.filtfilt(b, a, Hx) 
Hyf = signal.filtfilt(b, a, Hy) 
Hzf = signal.filtfilt(b, a, Hz)

# ----------------------------------------------------------------------------------
# PLot dos canais
title = ["Campo Elétrico - Eixo X", "Campo Elétrico - Eixo Y", "Campo Magnético - Eixo X", "Campo Magnético - Eixo Y", "Campo Magnético - Eixo Z" ]
MT_Notch_filter(title[0], Ex, Exf, fs)
MT_Notch_filter(title[1], Ey, Eyf, fs)
MT_Notch_filter(title[2], Hx, Hxf, fs)
MT_Notch_filter(title[3], Hy, Hyf, fs)
MT_Notch_filter(title[4], Hz, Hzf, fs)

# Salvando o dado filtrado em txt
dado_filtrado = np.zeros((len(Ex), 5))
dado_filtrado[:,0] = Exf
dado_filtrado[:,1] = Eyf
dado_filtrado[:,2] = Hxf
dado_filtrado[:,3] = Hyf
dado_filtrado[:,4] = Hzf

np.savetxt('Outputs/Dado_Filtrado.txt', dado_filtrado, delimiter='      ', fmt='%.1f')