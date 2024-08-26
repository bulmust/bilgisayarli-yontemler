---
title: "BDP - Runge-Kutta Yöntemleri - Problem Cevapları"
---

## Problem 1

Aşağıdaki matris denklemlerini yazdığımız rk4 fonksiyonu ile çözün.

$$
\begin{align*}
\frac{d}{dt}
\begin{bmatrix}
\rho_{11}(t) & \rho_{12}(t) \\
\rho_{21}(t) & \rho_{22}(t)
\end{bmatrix}
= 
\begin{bmatrix}
-\rho_{11}(t) & -2\rho_{12}(t) \\
-3\rho_{21}(t) & -4\rho_{22}(t)
\end{bmatrix}
\end{align*}
$$

### Çözüm

```python
################################################
## Modül yolunu varsayılan yol olarak ekleme ve modülü içe aktarma
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
import scipy.integrate as sciInt
# Fonksiyon
def fonkVek(rho, t):
    returnMatrix= np.array([[-rho[0],-2*rho[1]],[-3*rho[2],-4*rho[3]]])
    # Vektör olması gerekiyor. Yani tek boyutlu
    return returnMatrix.flatten()
# Başlangıç değerleri
rho0= np.array([[10.0, 20.0], [30.0, 40.0]]).flatten()
t0=0
tSon=1
n=100
# Çözüm, RK4
tTumRK4, yTum_VekRK4 = bym.add_coz_rk4_sistem(fonkVek, t0, tSon, rho0, n)
# Çiz
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(tTumRK4, yTum_VekRK4[0], label='RK4, $\\rho_{11}$')
ax[0, 0].legend()
ax[0, 1].plot(tTumRK4, yTum_VekRK4[1], label='RK4, $\\rho_{12}$')
ax[0, 1].legend()
ax[1, 0].plot(tTumRK4, yTum_VekRK4[2], label='RK4, $\\rho_{21}$')
ax[1, 0].legend()
ax[1, 1].plot(tTumRK4, yTum_VekRK4[3], label='RK4, $\\rho_{22}$')
ax[1, 1].legend()
plt.show()
```

## Problem 2

`scipy.integrate.solve_ivp` fonksiyonunu kullanarak aşağıdaki denklemi çözün. Çözüm yöntemi olarak `method='RK45'` ve `method='LSODA'` kullanın.

$$
\frac{d}{dx}y(x) = \sin(5x)
$$

Başlangıç koşulu: $y(-3)=4.5$. Çözümü -3 ile 3 arasında çizdirin.

Aynı denklemi sağ taraf $\sin(15x)$ ve $\sin(25x)$ olacak şekilde çözün.

### Çözüm

```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
# Fonksiyon
def fonk15(x,y): #! ÖNCE x SONRA y
    return np.sin(15*x)
def fonk25(x,y): #! ÖNCE x SONRA y
    return np.sin(25*x)
# Başlangıç değerleri
x0Array= np.array([-3, 3]) # [x0, xSon]
y0= np.array([4.5]) # y0 dizi (array) olmalıdır. (float değil)
n= 100
# RK45
xAralik= np.linspace(x0Array[0], x0Array[1], n)
cozum15RK45= solve_ivp(fonk15, x0Array, y0, method='RK45', t_eval=xAralik)
cozum25RK45= solve_ivp(fonk25, x0Array, y0, method='RK45', t_eval=xAralik)
# x değerleri => cozum15RK45.t
# y değerleri => cozum15RK45.y (y bir array olduğu için, y[0])
# LSODA
cozum15LSODA= solve_ivp(fonk15, x0Array, y0, method='LSODA', t_eval=xAralik)
cozum25LSODA= solve_ivp(fonk25, x0Array, y0, method='LSODA', t_eval=xAralik)
# Çiz
fig, ax = plt.subplots(1, 2)
ax[0].plot(cozum15RK45.t, cozum15RK45.y[0], label='RK45, $\\sin(15x)$')
ax[0].plot(cozum15LSODA.t, cozum15LSODA.y[0], label='LSODA, $\\sin(15x)$')
ax[0].legend()
ax[1].plot(cozum25RK45.t, cozum25RK45.y[0], label='RK45, $\\sin(25x)$')
ax[1].plot(cozum25LSODA.t, cozum25LSODA.y[0], label='LSODA, $\\sin(25x)$')
ax[1].legend()
plt.show()
```

## Problem 3

Sönümlü harmonik salınıcının Lagranjiyen'i aşağıdaki gibidir.

$$
L(x,v) = \frac{1}{2}mv^{2} - \frac{1}{2}kx^2
$$

Burada $v$ hız olup konumun $x$ zamana göre birinci türevine eşittir. Lagrange hareket denklemleri aşağıdaki gibi yazılır.

$$
    \left(\frac{d}{dt}\frac{\partial L}{\partial v} \right) - \frac{\partial L}{\partial x} = \frac{\partial F^{dis}}{\partial v}
$$

Yukarıda verilen formülden diferansiyel denklem setini oluşturun. Burada $F^{dis}=-\frac{1}{2}bv^{2}$ sönümleyici kuvvettir. $t=0-50$ arasındaki değerler için ve $n=1000$ adımda, 
   - Runge-Kutta-4 (veya 5(4) mertebe için Runge-Kutta methodu) yöntemi ile çözün.
   - x ile t'nin oluşturduğu grafiği çizdirin.


Başlangıç koşulları ve sabitler aşağıdaki gibidir.

- $m=1$ kg
- $k=1$ N/m
- $b=0.1$ Ns/m
- $x(t=0)=1$ m
- $v(t=0)=0$ m/s

### Çözüm

```python
import numpy as np
import scipy.integrate as scInteg
# Fonksiyon
def f6(t,yVek): #! t önce
    x= yVek[0]
    v= yVek[1]
    return np.array([v,(-(k/m)*x)-(b*v)])
# Başlangıç koşulu
m= 1
k= 1
b= 1e-1
yVec=np.array([1,0])
t0= 0
tStop= 50
# Çöz
solution=scInteg.solve_ivp(f6,[t0,tStop],yVec, method='RK45')
# Çiz
plt.plot(solution.t,solution.y[0], label='RK45')
plt.legend()
```

## Problem 4

Aşağıdaki diferansiyel denklemi Runge Kutta 4(5) yöntemini kullanarak çözün. Analitik sonuçla karşılaştırın.

$$
y''(t) = t^{3}+t+5, \quad y(0)=1, \quad y'(0)=5
$$

### Çözüm

```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scInteg
# Fonksiyon
def fonk(t, yVek): #! t önce
    return np.array([yVek[1], t**3+ t+ 5.])
# Başlangıç değerleri
N= 100
yVek0= np.array([1., 5.]) # [y(0), y'(0)]
t0= 0.
tSon= 6.
tTum= np.linspace(t0, tSon, N)
# Çöz
cozum= scInteg.solve_ivp(fonk, [t0, tSon], yVek0, method='RK45', t_eval=tTum)
# Analitik çözüm
yAnalitik= (tTum**5)/20 + (tTum**3)/6 + (5*tTum**2)/2 + 5*tTum + 1
# Çiz
plt.plot(cozum.t, cozum.y[0], 'o-' , label='RK45', color='r')
plt.plot(tTum, yAnalitik, label='Analitik', color='k')
plt.legend()
plt.show()
plt.close()
```

## Problem 5

Düşey düzlemde $l=1$ m uzunluğunda bir ipin ucunda birim kütleli bir cisim salınsın. Bu cisim denge noktasından $\theta(t=0s)=\pi/9$ rad açı ile harekete başlıyor. $g=9.81$ m/$s^{2}$. Cisim bırakıldığı anda açısal hızı $\omega(t=0s)=0$ rad/s. Bu cismin hareket denklemini $t=(0,10)$ arasında 

1. Euler yöntemiyle çözün.
2. RK4 (veya RK45 veya LSODA) yöntemiyle çözün.
3. Analitik çözümü de dikkate alın ve tüm çözümleri üst üste bindirerek çizdirin.
 
*Euler metodunda adım sayısını $n=10000$ alın.*

$$
\frac{d^{2}\theta}{dt^{2}}=-\frac{g}{l}\sin \theta
$$

Analitik çözüm: $\theta(t) = A\cos(t\sqrt{g/l})+B\sin(t\sqrt{g/l})$

### Çözüm

```python
################################################
## Modül yolunu varsayılan yol olarak ekleme ve modülü içe aktarma
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
import scipy.integrate as scInteg
# Global değişkenler
l=1
g=9.81
# Fonksiyon
def f(yVec,t):
    # yVec= [x, v]
    x= yVec[0]
    v= yVec[1]
    return np.array([v, -g/l*np.sin(x)])
# Fonksiyon
def f_scipy(t, yVec):
    # yVec= [x, v]
    x= yVec[0]
    v= yVec[1]
    return np.array([v, -g/l*np.sin(x)])
# Başlangıç koşulları
x0= 0
xSon= 10
n= 10000
y0Vek=np.array([np.pi/9,0])
# Çöz
xTum, yVekTum= bym.add_coz_euler_sistem(f, x0, xSon, y0Vek, n)
xTumScipy= np.linspace(x0, xSon, n)
cozum= scInteg.solve_ivp(f_scipy, [x0, xSon], y0Vek, t_eval= xTumScipy)
# Çiz
plt.plot(xTum, yVekTum[0,:], 'o-', color='r', label= 'Euler')
plt.plot(cozum.t, cozum.y[0], 'o-', color='b', label= 'Scipy')
plt.plot(xTum, y0Vek[0]*np.cos(np.sqrt(g/l)*xTum), 'k-', label= 'Analitik')
plt.xlabel('t')
plt.legend()
plt.grid()
plt.show()
plt.close()
```
