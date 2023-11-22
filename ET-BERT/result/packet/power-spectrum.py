import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

# 16進数のバイナリデータ（文字列）を16進数整数に変換
hex_data = "0123456789ABCDEF"  # 16進数データの例
binary_data = bytes.fromhex(hex_data)
integer_data = np.frombuffer(binary_data, dtype=np.uint8)

# パワースペクトルの計算
N = len(integer_data)  # データポイントの数
sampling_rate = 1  # サンプリングレート
t = np.arange(0, N) / sampling_rate  # 時刻軸

# フーリエ変換
yf = fft(integer_data)
xf = np.fft.fftfreq(N, 1 / sampling_rate)  # 周波数軸

# パワースペクトルの計算
power_spectrum = np.abs(yf) ** 2 / N

# グラフのプロット
plt.figure()
plt.plot(xf, power_spectrum)
plt.title("Power Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.grid()
plt.show()
plt.savefig("sin.png")