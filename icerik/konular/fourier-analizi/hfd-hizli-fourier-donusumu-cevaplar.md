---
title: "HFD - Hızlı Fourier Dönüşümü - Problem Cevapları"
---

## Problem 1

Açısal frekansı 5, genliği 10 olan bir cosinüs sinyali ve açısal frekansı 10, genliği 5 olan bir sinüs sinyalinin toplamını çizdirin. Örneklem oranı $100$, $t=[0,6)$ aralığında olsun. Sinyalin HFD'sini hesaplayın ve doğru frekanslar için çizdirin.

### Çözüm

```python
import numpy as np
#import scipy.fft as spfft
import matplotlib.pyplot as plt
# Örnekleme sayısı
orneklemOrani = 100 # 2**13
# Zaman
orneklemAraligi = 1.0/orneklemOrani
t = np.arange(0, 6, orneklemAraligi)
#toplamSure= 1
#t= np.linspace(0, toplamSure, orneklemOrani* toplamSure)
N= len(t)
# Açısal Frekans
frekans= 5
frekans2= 10
# Sinyal
sinyal= 10* np.cos((2 * np.pi) *frekans* t)\
    + 5*np.sin((2 * np.pi) *frekans2* t)
# Hızlı Fourier Dönüşümü
X= np.fft.fft(sinyal)
# X= spfft.fft(sinyal)
# Frekans
frek= np.fft.fftfreq(N, 1/orneklemOrani)
#frek= spfft.fftfreq(N, 1/orneklemOrani)
# Çiz
plt.stem(frek, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
plt.xlim(-15, 15)
plt.show()
```

## Problem 2

Bir sinyalin frekans uzayını kullanarak örneklem miktarını arttıralım. Bunun için örnek bir sinyal oluşturacağız. Bu sinyalin örneklem sayısını frekans uzayında arttırıp efektif olarak interpolasyon yapacağız. 

1. Bir sinyal oluşturun. Bu sinyal, $0$ ile $8\pi$ arasında, her $\pi/2$ aralığında bir örnekleme ile alınmış olsun.
2. Sinyal $\sin(t) + 0.3\sin(0.2t)$ şeklinde olsun.
3. Bu sinyalin HFD'sini hesaplayın.
4. Bu sinyalin frekans bileşenlerini bulun.
5. Bu sinyalin örneklem sayısını $64$ kat artırın.
6. Yeni örneklem sayısına göre frekans bileşenlerini bulun.
7. Yeni bir hfd sinyal değişkeni oluşturun. Bu yeni hfd sinyal değişkeni yeni örneklem sayısından oluşan frekans boyutunda olacaktır.
8. Eski hfd sinyalinin 0. bileşenini yeni hfd sinyal değişkeninin 0. bileşenine atayın.
9. Eski hfd sinyalinin pozitif (`[1:N//2+1]`) bileşenlerini ve negatif (`[-N//2+1:]`) bileşenlerini yeni hfd sinyal değişkenine atayın.
10. Eski ve yeni hfd sinyallerini çizdirin.
11. Yeni hfd sinyalini ters Fourier dönüşümü yaparak zaman uzayına çevirin.
12. Orijinal ve interpolasyon yapılmış sinyalleri çizdirin.

```python
import numpy as np
import matplotlib.pyplot as plt

# Orjinal sinyal
zaman = np.arange(0, np.pi*8, np.pi/2)
sinyal = np.sin(zaman)+ 0.3*np.sin(0.2*zaman)

# Örnek sayısı
N = len(zaman)

# HFD
sinyal_fft = np.fft.fft(sinyal)
frek = np.fft.fftfreq(N, d=zaman[1]-zaman[0])

# Yeni örnek sayısı
N_yeni = N * 64

# Yeni frekans
frek_yeni = np.fft.fftfreq(N_yeni, d=(zaman[1]-zaman[0])/64)

# Interpolate in frequency domain
sinyal_fft_interp = np.zeros_like(frek_yeni, dtype=np.complex64)
sinyal_fft_interp[0] = sinyal_fft[0]  # DC component
sinyal_fft_interp[1:N//2+1] = sinyal_fft[1:N//2+1] #/ 2  # Positive frequencies
sinyal_fft_interp[-N//2+1:] = sinyal_fft[-N//2+1:] #/ 2  # Negative frequencies

# Plot FFT of interpolated signal with original signal
fig, ax = plt.subplots(2, 1)
ax[0].stem(frek_yeni, np.abs(sinyal_fft_interp), 'r', markerfmt=" ",basefmt="-r", label='Interpolasyon')
ax[1].stem(frek, np.abs(sinyal_fft), 'b', markerfmt=" ", basefmt="-b", label='Orjinal')
plt.show()
plt.close()

# Perform inverse Fourier transform and scale
sinyal_interp = np.fft.ifft(sinyal_fft_interp)* 64

# Plot original and interpolated signals
plt.plot(zaman, sinyal, 'bo-', label='Orjinal Sinyal')
plt.plot(np.linspace(0, np.pi*8, N_yeni), np.real(sinyal_interp), 'r-', label='Interpole Sinyal')
plt.xlabel('Zaman')
plt.ylabel('Genlik')
plt.legend()
plt.grid(True)
plt.show()
```

## Problem 3

Zamandan bağımsız Schrödinger denklemini boşluk için çözdüğümüzde Gaussian dalga paketini elde ederiz. Konum uzayındaki dalga fonksiyonu aşağıdaki gibidir.

$$ \psi(x, t=0) = <x | \psi(0)>= e^{-\frac{(x- \mu)^{2}}{4\sigma_{x}^{2}}+i k_{0} x}$$

Burada $\mu$ paketin merkezini yani ortalama (mean) değeridir. $\sigma_{x}$ ise $x$ uzayındaki standart sapmayı yani belirsizliği verir. $k_{0}= p/\hbar$ ise paketin momentumunu verir.

1. **[5 Puan]** Yukarıda verilen dalga paketinin konum uzayındaki **olasılık yoğunluğunu** çizdirin. Formülde $\mu = 0$, $\sigma_{x} = 0.1$ ve $k_{0} = 10$ olarak alın. Konumu $x = -1$ ile $x = 1$ arasında on bin parçaya ayırarak alabilirsiniz.
2. **[10 Puan]** Elde ettiğiniz dalga paketinin Fourier dönüşümünü ve frekansları hesaplayın. 
3. **[5 Puan]** Fourier dönüşümünden elde ettiğiniz Gaussian dalga paketinin momentum uzayındaki **olasılık yoğunluğunu** çizdirin.
4. **[5 Puan]** Aynı işlemi $\sigma_x=0.001$ için tekrar edin. Konum uzayındaki olasılık fonksiyonunu ve momentum uzayındaki olasılık fonksiyonunu nasıl değişti? `print()` fonksiyonu ile açıklayın.
5. **[5 Puan]** Yukarıdaki işlem ile Heisenberg belirsizlik ilkesi arasında nasıl bir bağlantı vardır? `print()` fonksiyonu ile açıklayın.

### Çözüm

import numpy as np
import matplotlib.pyplot as plt

```python
import numpy as np
import matplotlib.pyplot as plt

# Sabitler
mu= 0
k0= 10
# Konum uzayının sınırlarını
x= np.linspace(-1 , 1, 10000)

for sigma_x in [0.1, 0.001]:
    # Fonksiyon
    psi_x= np.exp(-(x-mu)**2 / (4* sigma_x**2))* np.exp(1j * k0* x)

    # Çiz
    plt.figure(figsize=(10,5))
    plt.plot(x, np.abs(psi_x)**2, label='$|\psi(x,0)|^2$')
    plt.xlabel("Konum [a.u.]")
    plt.ylabel("Olasılık yoğunluğu")
    plt.legend()
    plt.show()
    plt.close()

    # FFT
    #psi_k= np.fft.fftshift(np.fft.fft(psi_x))
    #f0req=np.fft.fftshift(np.fft.fftfreq(len(psi_x) , x[1]-x[0]))
    psi_k= np.fft.fft(psi_x)
    freq=np.fft.fftfreq(len(psi_x) , x[1]-x[0])

    # Çiz
    plt.figure(figsize=(10,5))
    plt.plot(freq, np.abs(psi_k)**2, label='$|\psi(k,0)|^2$')
    plt.xlabel("Frekans [a.u.]")
    plt.ylabel("Olasılık yoğunluğu")
    plt.legend()
    plt.show()
    plt.close()
```