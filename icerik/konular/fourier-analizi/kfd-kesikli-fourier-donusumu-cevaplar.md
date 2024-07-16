---
title: "KFD - Kesikli Fourier Dönüşümü - Problem Cevapları"
---

## Problem 1

Açısal frekansı 5, genliği 10 olan bir cosinüs sinyali ve açısal frekansı 10, genliği 5 olan bir cosinüs sinyalinin toplamını çizdirin Örneklem oranı $100$, $t=[0,6)$ aralığında olsun. Sinyalin KFD'sini alın ve bu değerleri pozitif/negatif frekanslara göre çizdirin.

### Çözüm

```python
################################################
import os
import sys
# Bu dosyanın bulunduğu dizini al
current_dir = os.path.abspath('')
# 3 üst dizine çık
module_dir = os.path.join(os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir)), 'moduller')
# moduller dizinini yol olarak ekle
sys.path.append(module_dir)
# bilYonMod.py modülünü içe aktar
import bilYonMod as bym
################################################

import numpy as np
import matplotlib.pyplot as plt
# Örneklem orani
orneklemOrani = 100
# Örneklem aralığı
orneklemAraligi = 1.0/orneklemOrani
t= np.arange(0, 6, orneklemAraligi)
# Toplam örneklem sayısı
N= t.size
# Açısal frekans
# Dalganın frekansı
acisalFrekans= 5
acisalFrekans2= 10
genlik= 10
genlik2= 5
# Çiz
sinyal= genlik* np.cos(acisalFrekans* t) + genlik2* np.cos(acisalFrekans2* t)
plt.plot(t, sinyal, 'b', label= f'${genlik} \cos({acisalFrekans} t) + {genlik2} \cos({acisalFrekans2} t)$')
plt.ylabel("Genlik")
plt.xlabel("Zaman (s)")
plt.legend()
plt.show()
plt.close()
# KFD
X = bym.fourier_kfd(sinyal)
# Frekans
if N%2 == 0:
    maksFrek= N/ 2
    frekCoz=maksFrek/ (N/2)
    XPoz= X[:int(N/2)]
    XNeg= X[int(N/2):]
else:
    maksFrek= (N-1)/ 2
    frekCoz=maksFrek/ ((N-1)/2)
    XPoz= X[:int((N-1)/2)]
    XNeg= X[int((N+1)/2):]
frekPoz= np.arange(0, maksFrek, frekCoz)
frekNeg= np.arange(-maksFrek, 0, frekCoz)
X= np.fft.fft(sinyal)
frek= np.fft.fftfreq(N, orneklemAraligi)
plt.stem(frek, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
plt.xlim(-acisalFrekans-10, acisalFrekans+10)
plt.show()
plt.close()
# Genlik ve Faz Değerlerini Çiz
plt.stem(frekPoz, np.abs(XPoz)/(N/2), 'b', label= 'Pozitif Genlik', markerfmt=" ", basefmt="-b")
plt.stem(frekNeg, np.abs(XNeg)/(N/2), 'r', label= 'Negatif Genlik', markerfmt=" ", basefmt="-r")
plt.ylabel("Genlik")
plt.xlabel("Frekans (Hz)")
plt.xlim(-acisalFrekans-10, acisalFrekans+10)
plt.legend()
plt.show()
plt.close()
```

## Problem 3

Zamandan bağımsız Schrödinger denklemini boşluk için çözdüğümüzde Gaussian dalga paketini elde ederiz. Konum uzayındaki dalga fonksiyonu aşağıdaki gibidir [@web2024Mar-4, @web2024Mar-5].

$$ \psi(x, t=0) = <x | \psi(0)>= e^{-\frac{(x^{2}- \mu)}{4\sigma_{x}^{2}}+i k_{0} x}$$

Burada $\mu$ paketin merkezini yani ortalama (mean) değeridir. $\sigma_{x}$ ise $x$ uzayındaki standart sapmayı yani belirsizliği verir. $k_{0}= p/\hbar$ ise paketin momentumunu verir.

1. Yukarıda verilen dalga paketini konum uzayında olasılık yoğunluğunu çizdirin. Formülde $\mu = 0$, $\sigma_{x} = 0.1$ ve $k_{0} = 10$ olarak alın.
2. Elde ettiğiniz dalga paketinin Fourier dönüşümünü hesaplayın. 
   1. HFD sonucunu `np.fft.fftshift` fonksiyonu ile kaydırın. Bu işlem $k$ uzayının $-k_{max}$ ile $k_{max}$ arasında yapın. Bunun için `np.fft.fftshift(np.fft.fft(veri))` kullanabilirsiniz.
   2. Fourier dönüşümünü $\frac{2\pi}{L}$ ile normalize edin.
   3. Fourier dönüşümünün frekansını belirleyin. Bunun için `np.fft.fftshift(np.fft.fftfreq(L, dx))` formülünü kullanabilirsiniz.
3. Fourier dönüşümünden elde ettiğiniz Gaussian dalga paketinin momentum uzayındaki olasılık yoğunluğunu çizdirin.
4. Tüm işlemi $\sigma_x=0.01$ için tekrar edin. Konum uzayındaki olasılık fonksiyonu ve momentum uzayındaki olasılık fonksiyonunu nasıl değişti?
5. Aynı işlemi $\sigma_x=0.001$ için tekrar edin. Konum uzayındaki olasılık fonksiyonu ve momentum uzayındaki olasılık fonksiyonunu nasıl değişti?
6. Yukarıdaki işlem ile Heisenberg belirsizlik ilkesi arasında nasıl bir bağlantı var mıdır?

### Çözüm

```python
import numpy as np
import matplotlib.pyplot as plt
# Sabitler
hbar = 1  # İndirgenmiş Planck Sabiti
sigma_x = [0.1,0.01, 0.001]  # Dalga Paketinin Standart Sapması
k0 = 10  # Ortalama Dalga Vektörünün Momentum Uzayındaki Değeri
# Konum Uzayının sınırları
x = np.linspace(-1, 1, 10000)
dx = x[1] - x[0] # İnfinitesimal uzay aralığı
for it_sigma in sigma_x:
    # Gaussian dalga paketinin konum uzayındaki formülü
    A_x = 1 / np.sqrt(it_sigma * np.sqrt(np.pi))
    #psi_x = A_x * np.exp(-(x - 0)**2 / (4 * sigma**2)) * np.exp(1j * k0 * x)
    psi_x = np.exp(-(x - 0)**2 / (4 * it_sigma**2)) * np.exp(1j * k0 * x)
    ## Gaussian dalga paketinin momentum uzayındaki formülü
    # A_p = np.sqrt(it_sigma / (np.pi * hbar))
    # p = np.linspace(-1500, 1500, 1000)
    # psi_p = A_p* np.exp(-it_sigma**2 * (p - k0)**2 / (2 * hbar**2)) * np.exp(-1j * p * x[0] / hbar)
    # # Konum uzayındaki dalga paketinin Fourier dönüşümünü al
    # dk = 2 * np.pi / (len(x) * dx) # İnfinitesimal momentum aralığı Burada dk = 2pi/L, L değeri x aralığının uzunluğudur
    # k = np.arange(len(x)) * dk - np.pi / dx # Momentum uzayının sınırları
    psi_k = np.sqrt(2 * np.pi / len(x)) * np.fft.fftshift(np.fft.fft(psi_x))
    frek= np.fft.fftshift(np.fft.fftfreq(len(x), dx))
    # Çiz
    # Konum uzayındaki Gaussian dalga paketi
    plt.plot(x, (np.abs(psi_x)**2), label='$|\\psi_{x}|^{2}$')
    plt.xlabel('Konum (a.u.)')
    plt.ylabel('Dalga Fonksiyonu (a.u.)')
    plt.title(f'Konum uzayındaki Gaussian dalga paketi, $\\sigma={it_sigma}$')
    plt.legend()
    plt.xlim(-0.5, 0.5)
    plt.show()
    plt.close()
    # Momentum uzayındaki Gaussian dalga paketi
    # plt.plot(p, np.abs(psi_p)**2, label='$|\\psi_{p}|^{2}$')
    # plt.xlabel('Momentum (a.u.)')
    # plt.ylabel('Olasılık (a.u.)')
    # plt.title('Momentum uzayındaki Gaussian dalga paketi, $\\sigma={it_sigma}$'')
    # plt.legend()
    # plt.xlim(-50, 50)
    # plt.show()
    # plt.close()
    # Hızlı Fourier dönüşümü
    plt.plot(frek, np.abs(psi_k)**2, label='$|\\psi_{k}|^{2}$')
    plt.xlabel('Momentum (a.u.)')
    plt.ylabel('Olasılık (a.u.)')
    plt.title(f'Hızlı Fourier dönüşümü, $\\sigma={it_sigma}$')
    plt.xlim(-500, 500)
    plt.legend()
    plt.show()
    plt.close()
```

## Problem 4

1. `/veri/` klasöründe bulunan `veri-hft-dalga.csv` dosyasını okuyunuz. Dosyaya [bu linkten erişebilirsiniz](../../../veri/veri-hft-dalga.csv). `pd.read_csv` fonksiyonunu kullanabilirsiniz.
2. Bu dosyanın ilk sütuunu `x`, ikinci sütunu `y` olarak atayınız.
3. `x` sütununu x eksenine `y` sütununu y eksenine yerleştirerek bir grafik çizin. Grafikte noktalar kırmızı ve yıldız şeklinde olsun.
4. Aynı grafiği siyah renkli ve çizgi şeklinde tekrar çizin.
5. Bu grafiği kapatın.
6. `scipy.fft.fft` fonksiyonunu kullanarak DFT genliğini çizdirin.
7. Sadece Nyquist frekansına kadar olan genliği çizdirin.
8. DFT verisini `dalga_dft.csv` dosyasına kaydedin.

### Çözüm

```python
################################################
import os
# Bu dosyanın bulunduğu dizini al
current_dir = os.path.abspath('')
# 3 üst dizine çık
veri_dir = os.path.join(os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir)), 'veri')
################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft
# ------------------------------
# Veriyi oluşturmak için gereken script
#sr=100
#ts = 1.0/sr
#x = np.arange(0,1,ts)
#freq = 1.
#y = 3*np.sin(2*np.pi*freq*x)
#freq = 4
#y += np.sin(2*np.pi*freq*x)
#freq = 7
#y += 0.5* np.sin(2*np.pi*freq*x)
#seri= pd.DataFrame(y, index=x, columns=["y"])
#seri.index.name="x"
#seri.to_csv(veri_dir+ "veri-hft-dalga.csv", header=True)
# ------------------------------
df= pd.read_csv(veri_dir+ "/veri-hft-dalga.csv")
plt.plot(df.x, df.y, "r*")
plt.plot(df.x, df.y, "k")
plt.show()
plt.close()

# Plot DFT
c = fft(df.y.to_numpy())
plt.plot(np.abs(c))
plt.ylabel("DFT Genliği |X(frekans)|")
plt.xlabel("Frekans")
plt.show()
plt.close()

# Scipy ile DFT
yf = fft(df.y.to_numpy())
plt.plot(df.x, np.abs(yf))
plt.title("Scipy ile DFT (fft)")
plt.ylabel("DFT Genliği |X(frekans)|")
plt.xlabel("Frekans")
plt.show()

# Temiz Tepeler
plt.stem(df.x[:len(yf)//2], np.abs(yf[:len(yf)//2]))
plt.title("Scipy ile DFT (fft)")
plt.ylabel("DFT Genliği |X(frekans)|")
plt.xlabel("Frekans")
plt.show()

pd.Series(c).to_csv(veri_dir+ "/veri-hft-dalga-hft.csv")
```

## Kaynaklar

1. Python Programming and Numerical Methods, Qingkai Kong, 2018
2. <https://www.ams.org/journals/mcom/1965-19-090/S0025-5718-1965-0178586-1/>