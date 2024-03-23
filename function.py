import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    # Carrega os dados do arquivo
    s = np.loadtxt(file_path)
    
    # Extrai os canais elétricos e magnéticos
    Ex = s[0:1000, 0]
    Ey = s[0:1000, 1]
    Hx = s[0:1000, 2]
    Hy = s[0:1000, 3]
    Hz = s[0:1000, 4]
    
    return Ex, Ey, Hx, Hy, Hz

def MT_Notch_filter(title, signal, signal_filter, fs):

    # Trasnformada de Fourier
    nt = len(signal)
    dt = 1/fs
    ts = nt / fs  # tempo em segundos
    t = np.linspace (0, ts, nt)
    freq = np.fft.fftfreq(nt, dt)
    mascara = freq > 0
        
    Y_signal = np.fft.fft(signal)  # Cálculo da transformada do sinal final
    Amp_signal = 2.0 * np.abs(Y_signal / nt)
    
    Y_filter = np.fft.fft(signal_filter)  # Cálculo da transformada do sinal final
    Amp_filter = 2.0 * np.abs(Y_filter / nt)

    fig, ax = plt.subplots(ncols=2, nrows=2, num= title, figsize=(14, 6))
    ax[0, 0].set_title('Time Domain', fontsize=15)
    ax[0, 0].plot(t, signal)
    ax[0, 0].set_xlabel("Time [s]", fontsize=12)
    ax[0, 0].set_ylabel(r"$E_x(t)$", fontsize=12)

    ax[0, 1].set_title("Fast Fourier Transform - FFT", fontsize=15)
    ax[0, 1].plot(freq[mascara], Amp_signal[mascara])
    ax[0, 1].set_xlabel("Frequency [Hz]", fontsize=12)
    ax[0, 1].set_ylabel(r"$|E_x(f)|$", fontsize=12)

    ax[1, 0].set_title('Time Domain', fontsize=15)
    ax[1, 0].plot(t, signal_filter)
    ax[1, 0].set_xlabel("Time [s]", fontsize=12)
    ax[1, 0].set_ylabel(r"$E_x(t)$", fontsize=12)

    ax[1, 1].set_title("Fast Fourier Transform - FFT", fontsize=15)
    ax[1, 1].plot(freq[mascara], Amp_filter[mascara])
    ax[1, 1].set_xlabel("Frequency [Hz]", fontsize=12)
    ax[1, 1].set_ylabel(r"$|E_x(f)|$", fontsize=12)

    fig.tight_layout()
    plt.show()

