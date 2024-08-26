---
title: "SDP - Atış Yöntemi - Problem Cevapları"
---

## Problem 1

Aşağıdaki denklemi atış yöntemi ile çözün.

$$
y''(t)=t, \quad y(0)=1, \quad y(3)=9
$$

1. Elde ettiğiniz çözümü yani $y(t)$ fonksiyonunu çizdirin.
2. Bu denklemi analitik olarak çözün ve çözümü de çizdirin.

### Çözüm

```python
import numpy as np
import scipy.integrate as scInteg
import scipy.optimize as scOpt
import matplotlib.pyplot as plt

# Diff. Denk:
# y'' = t , y(0)=1 , y(3)=9

# Fonksiyon:
def fonk_SDP(t, y):
    return np.array([y[1], t])
# Başlangıç Koşulları:
t0=0.
tStop=3.
y0= 1.     # y(0) = 1
yStop= 9.  # y(3) = 9
# Theta fonksiyonu:
def thetaFonk(u):
    cozum = scInteg.solve_ivp(fonk_SDP, [t0, tStop], [y0, u])
    yCozum = cozum.y[0]
    # Çözümün son değeri => yCozum[-1]
    # yStop =>  y(3) = 9
    return yCozum[-1]- yStop
# Aynı şekilde theta fonksiyonunun kökünü bulalım.
v0= scOpt.ridder(thetaFonk, 0, 50)

# Gercek Cozum:

cozum = scInteg.solve_ivp(fonk_SDP, [t0, tStop], [y0, v0])#, t_eval=x_eval)

plt.plot(cozum.t, cozum.y[0], 'or')
# Analitik Çözüm
# y''= t y(0)=1 y(3)=9
# y'= t^2/2  + C1
# y= t^3/6  + C1 t + C2
# y(0)=1 => C2=1
# y(3)=9 => 9=27/6 + 3C1 + 1=9 => C1=27/18

#=> y(t)= t^3/6 + 21t/18 + 1
x_eval= np.linspace(0, 3, 100)
plt.plot(x_eval, x_eval**3/6 + 21*x_eval/18 + 1, 'k')
plt.show()
```

## Problem 2

Aşağıdaki diferansiyel denklemi atış yöntemini kullanarak çözün. Adım aralığını $h=0.05$ alın. Analitik sonuçla karşılaştırın.

$$
y''(t) = t^{3}+t+5, \quad y(0)=1, \quad y(6)=545.8
$$

### Çözüm

```python
import numpy as np
import scipy.integrate as scInteg
import scipy.optimize as scOpt
import matplotlib.pyplot as plt
# Fonksiyon
def fonk(t, yVek): #! t önce
    return np.array([yVek[1], t**3+ t+ 5.])
# Başlangıç Koşulları:
t0=0.
tStop=6.
y0= 1.     # y(0) = 1
yStop= 545.8  # y(6) = 545.8
# Adım aralığı
h=0.05
adet= int((tStop-t0)/h)+1
tTum=np.linspace(t0, tStop, adet)
# Theta fonksiyonu:
def thetaFonk(u):
    cozum = scInteg.solve_ivp(fonk, [t0, tStop], [y0, u], t_eval=tTum)
    yCozum = cozum.y[0]
    return yCozum[-1]- yStop
# theta fonksiyonunun kökünü bulalım.
v0= scOpt.ridder(thetaFonk, 0., 6)
print(v0)
# Son kez bdp çözümü yapalım.
cozum = scInteg.solve_ivp(fonk, [t0, tStop], [y0, v0], t_eval=tTum)
# Analitik Cozum
yAnalitik= (tTum**5)/20 + (tTum**3)/6 + (5*tTum**2)/2 + 5*tTum + 1
plt.plot(cozum.t, cozum.y[0], 'o-', label='Atış Yöntemi', color='r')
plt.plot(tTum, yAnalitik, label='Analitik', color='k')
plt.legend()
plt.show()
```

## Problem 3

1. Aşağıdaki diferansiyel denklemi atış (shooting) yöntemini kullanarak çözün. 
2. Çözümün grafiğini çizdirin. Sayısal çözüm noktalarını kırmızı nokta olarak belirleyin. 

$$
\frac{d^{2}y(x)}{dx^{2}}+ \frac{dy(x)}{dx} = -4 \text{ ,}
$$

Sınır koşulları: $y(0)=0$, $y(3)=9$. 

*Bu soruyu çözerken kökü $-30$ ile $30$ arasında arayın.*

3. Aşağıda verilen analitik çözümü de aynı grafikte çizdirin.

$$
y(x) = \frac{\left(-4x + 21e^{3 - x} + e^{3}(4x - 21)\right)}{1 - e^3} \text{ .}
$$

### Çözüm

```python
import numpy as np
import scipy.integrate as scInteg
import scipy.optimize as scOpt
import matplotlib.pyplot as plt
# Diff. Denk:
# y'' + y'= -4 , y(0)=0 , y(3)=9
# Fonksiyon
def fonk_SDP(t, y):
    # y[0] => y
    # y[1] => y'= v
    # y' = y[1]
    # v' = -4- y[1]
    return np.array([y[1], -4- y[1]])
# Başlangıç Koşulları
t0=0.
tStop=3.
y0= 0.    # y(0) = 0
yStop= 9. # y(3) = 9
# Theta fonksiyonu
def thetaFonk(u):
    cozum = scInteg.solve_ivp(fonk_SDP\
        , [t0, tStop], [y0, u])
    yCozum = cozum.y[0]
    return yCozum[-1]- yStop
# Aynı şekilde theta fonksiyonunun kökünü bulalım.
v0= scOpt.ridder(thetaFonk, -30, 30)
# Gerçek Çözüm
xTum= np.linspace(0, 3, 100)
cozum = scInteg.solve_ivp(fonk_SDP\
    ,[t0, tStop], [y0, v0], t_eval=xTum)
# Analitik Çözüm
cozumAnalitik= (-4* xTum+ 21* np.exp(3 - xTum) + (np.e**3)*(4* xTum -21))\
        /(1 - (np.e**3))
# Çiz
plt.plot(cozum.t, cozum.y[0], 'or')
plt.plot(xTum, cozumAnalitik, 'k')
plt.show()
# ----------------------------------------
# Analitik Çözüm
# y'' + y'= -4
# y(x)= e^{kx}
# y'' + y'= 0 => k^{2} + k = 0 => k1= -1, k2= 0
# y(x)= C1 e^{-x} + C2
# 
# y_p(x) = a1 x
# 0 + a1 = -4 => a1= -4
# y_p(x) = -4 x
#
# y(x)= C1 e^{-x} + C2 - 4 x
#
# y(0)= 1 => C1 + C2        = 1
# y(3)= 9 => C1 e^{-3} + C2 = 3
#
# y(x) = -(e^3 (21 - 4 x) - 21 e^(3 - x) + 4 x)/(1 - e^3)
# ----------------------------------------
```

