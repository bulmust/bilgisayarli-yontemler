---
title: "SDP - Sonlu Farklar Yöntemi - Problem Cevapları"
---

## Problem 1

Aşağıdaki diferansiyel çözebilir misinz?

$$
\frac{\hbar^{2}}{2 m}\frac{d^{2}}{dx^{2}}\psi(x) = E\psi(x), \qquad \psi(x=0)=0, \qquad \psi(x=L)=0 \text{.}
$$

Çözümü $n=1$ ve $n=2$ için bulmaya çalışın. Hem bulduğunuz enerji değerlerini hem de dalga fonksiyonunun karesini (olasılık yoğunluğunu, $|\psi(x)|^{2}$) çizdirin. $x$ değerleri $0$ ile $L$ arasında $N=100$ adet olsun.

Denklemdeki katsayıları aşağıdaki gibi alın.

1. $\hbar=1$
2. $m=1$ kg
3. $L=2$

Enerji özdeğerinin gerçek değeri aşağıdaki gibi olmalıdır.

$E=\frac{\pi^{2}\hbar^{2}}{2mL^{2}}n^{2}$ J.

Dalga fonksiyonunun analitik çözümü aşağıdaki gibi olmalıdır. 

$$
\psi(x)=\sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)
$$

::: {.callout-tip}
Bu problem bir özdeğer problemidir. Diferansiyel operatörü $\left(\frac{d^{2}}{dx^{2}}\right)$ doğrusal operatörü matris şeklinde yazmalısınız. Bu matrisi sonlu farklar yönteminde yazdık.
:::

### Çözüm

REF: [Bu linkten değiştirilerek adapte edilmiştir](https://github.com/louishrm/Infinite-Square-Well/blob/main/squarewell.ipynb)

```python
import numpy as np
import matplotlib.pyplot as plt
# Sabitler
h_bar = 1
m = 1 
L = 2
# Nokta Sayısı
N = 1000
# x değerleri
x = np.linspace(0, L, N+1)
# Adım aralığı
h = L / (N + 1)
# Enerji seviyesi
n=1
# Analitik çözüm
psi_analitik = np.sqrt(2/L)*np.sin(n*np.pi*x/L)
E_analitik = lambda n: (np.pi**2 * h_bar**2 / (2 * m * L**2)) * n**2
# Diferansiyel Operatörünün Matris Formu
# y''(x) = (y(x+h) - 2y(x) + y(x-h)) / h^2
# Son değeri almıyoruz.
M = np.diag(-2*np.ones(N-1)) + np.diag(np.ones(N-2),1)+ np.diag(np.ones(N-2),-1)
# Hamiltonian
H = -h_bar**2/(2*m)* 1/(h)**2 * M
# Özdeğer (E) ve özvektörler (psi)
E, psi = np.linalg.eigh(H)
# Psi değerlinin transpozunu alalım.
psi = psi.T
# Normalize Et
def integral(f, axis=0):
    return np.sum(f*h, axis=axis)
# Normalizasyon Katsayısı
norms = integral(psi**2)
# Normalize psi
psi = psi/np.sqrt(norms)
# Enerji Özdeğerlerini yazdır
print(f"E(n=1) Sayısal  [J]: {E[n-1]:.2e}")
print(f"E(n=1) Analitik [J]: {E_analitik(n):.2e}")
# Çiz
plt.plot(x[1:-1], np.abs(psi[n-1])**2, 'o-', label = f'$|\\psi(n={n})|^{2}$ Sayısal')
plt.plot(x, psi_analitik**2, label = f'$|\\psi(n={n})|^{2}$ Analitik')
plt.legend()
plt.show()
```

## Problem 2

Aşağıdaki diferansiyel denklemi sonlu farklar yöntemini kullanarak çözün. Analitik sonuçla karşılaştırın.

$$
y''(t) = t^{3}+t+5, \quad y(0)=1, \quad y(6)=545.8
$$

### Çözüm

```python
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt
# Fonksiyon
def fonk(t):
    return t**3+t+5
# Sınır Değerleri
y_t0=1
y_t6=548.8
# Adım aralığı
h=0.03
# Tum t değerleri
t0=0
tSon=6
adet= int((tSon-t0)/h)+1
tTum=np.linspace(t0, tSon, adet)
# Yerine koyduğumuzda oluşan denklemler
ilkDenklemSagTaraf=fonk(h)*(h**2)-y_t0
sonDenklemSagTaraf=fonk(tSon-h)*(h**2)-y_t6
araDenklemlerSagTaraf=np.array(ilkDenklemSagTaraf)
for i in range(1, adet-3):
    araDenklemlerSagTaraf= np.append(araDenklemlerSagTaraf, fonk(tTum[i+1])*(h**2))
# Son denklemi ekle
sonucMatrisi= np.append(araDenklemlerSagTaraf,sonDenklemSagTaraf)
# Katsayı Matrisi
katsayiMat= np.zeros((adet-2, adet-2))
for i in range(adet-2):
    katsayiMat[i, i]= -2
    if not i == adet-3:
        katsayiMat[i, i+1]= 1
    if not i == 0:
        katsayiMat[i, i-1]= 1
# Çöz
cozum=solve(katsayiMat, sonucMatrisi)
# İlk Çözümü Ekle
cozum=np.insert(cozum, 0, y_t0)
# Son Çözümü Ekle
cozum=np.append(cozum, y_t6)
# Analitik Çözüm
yAnalitik= (tTum**5)/20 + (tTum**3)/6 + (5*tTum**2)/2 + 5*tTum + 1
# Çiz
plt.plot(tTum, cozum, 'o-', label='Sonlu Farklar', color='r')
plt.plot(tTum, yAnalitik, label='Analitik', color='k')
plt.legend()
plt.show()
```