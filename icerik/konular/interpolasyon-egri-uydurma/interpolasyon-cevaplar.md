---
title: "İnterpolasyon - Problem Cevapları"
---

## Problem 1

En alttaki veriyi kullanarak 
   - Kübik spline interpolasyonu yapın (`scipy.interpolate.CubicSpline`).
   - Doğrusal (1. derece) ve 4. derece en küçük kareler uydurması (fiting) yapın (`numpy.polyfit`).
   - Veriyi (nokta olacak şekilde), interpolasyonu ve uydurmaları (çizgi olacak şekilde) aynı grafikte çizdirin. Grafikte gözüken $y$ eksenini $-5$ ile $5$ arasında sınırlayın grafiği gösterin.
   - İnterpolasyonu ve uydurumayı $x=(0,6)$ arasındaki noktalar için yapın.

Veri: 

| $x$ | 1  | 2 | 3  | 4 | 5  |
|---|----|---|----|---|----|
| $y$ | -1 | 1 | -2 | 2 | -6 |

### Çözüm

```python
import numpy as np
import scipy.interpolate as spInterp
import matplotlib.pyplot as plt

veri= np.array([[1,2,3,4,5],[-1,1,-2,2,-6]])
xHep=np.linspace(0,6,100)
ySpline_f=spInterp.CubicSpline(veri[0],veri[1])
yUydurma1=np.polyfit(veri[0],veri[1],1)
yUydurma4=np.polyfit(veri[0],veri[1],4)

plt.plot(veri[0],veri[1],'o')
plt.plot(xHep,ySpline_f(xHep), label='Spline')
plt.plot(xHep,yUydurma1[0]*xHep+yUydurma1[1], label='1. dereceden')
plt.plot(xHep,yUydurma4[0]*xHep**4+yUydurma4[1]*xHep**3+yUydurma4[2]*xHep**2+yUydurma4[3]*xHep+yUydurma4[4], label='4. dereceden')
plt.legend()
```

## Problem 2

$(x_{0}, y_{0}) = (0, 1)$, $(x_{1}, y_{1}) = (1, 1)$, $(x_{2}, y_{2}) = (3, 7)$ verisini kullanarak Lagrange polinomunu elde edin. Gerekli formüller: 

$P_{2}(x) = \sum_{i=0}^{2}y_{i}l_{i}(x)$

$l_{i}= \prod_{j=0,j\neq i}^{2}\frac{x-x_{j}}{x_{i}-x_{j}}$

### Çözüm

$l_{0}(x)$ terimi [5 Puan]

$$
l_{0}(x) = \frac{(x-x_{1})(x-x_{2})}{(x_{0}-x_{1})(x_{0}-x_{2})}
$$

$$
l_{0}(x) = \frac{(x-1)(x-3)}{(0-1)(0-3)} = \frac{x^{2}-4x+3}{3}
$$

$l_{1}(x)$ terimi [5 Puan]

$$
l_{1}(x) = \frac{(x-x_{0})(x-x_{2})}{(x_{1}-x_{0})(x_{1}-x_{2})}
$$

$$
l_{1}(x) = \frac{(x-0)(x-3)}{(1-0)(1-3)} = \frac{-x^{2}+3x}{2}
$$

$l_{2}(x)$ terimi [5 Puan]

$$
l_{2}(x) = \frac{(x-x_{0})(x-x_{1})}{(x_{2}-x_{0})(x_{2}-x_{1})}
$$

$$
l_{2}(x) = \frac{(x-0)(x-1)}{(3-0)(3-1)} = \frac{x^{2}-x}{6}
$$

Lagrange polinomu [4 Puan]
$$
P_{2}(x) = y_{0}l_{0}(x) + y_{1}l_{1}(x) + y_{2}l_{2}(x)
$$

$$
P_{2}(x) = 1\times\frac{x^{2}-4x+3}{3} + 1\times\frac{-x^{2}+3x}{2} + 7\times\frac{x^{2}-x}{6}
$$

Sonuç [1 Puan]

$$
P_{2}(x)= x^{2}-x+1
$$