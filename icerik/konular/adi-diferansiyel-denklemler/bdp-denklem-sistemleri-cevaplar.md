---
title: "BDP - Denklem Sistemleri - Problem Cevapları"
---

## Problemi 1

Lorenz atraktörünün denklemini Euler yöntemiyle çözünüz. Sabitler için $\rho=28$, $\sigma=10$ ve $\beta=8/3$ alınız. Başlangıç koşullarını: $x_{0}=1$, $y_{0}=1$ ve $z_{0}=1$ olarak alınız. En iyi sonucu görebilmek için $t=0-10$ aralığında ve $n= 1000$ adımda yapınız. 3 boyutlu grafik çizilirse ünlü şekil ortaya çıkacaktır.

$$
\frac{dx}{dt}=\sigma(y-x)
$$

$$
\frac{dy}{dt}=x(\rho-z)-y
$$

$$
\frac{dz}{dt}=xy-\beta z
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
# Başlangıç Koşulları
rho= 28
sigma= 10
beta= 8/3
def f(yVec, t):
    # yVec= [x, y, z]
    x= yVec[0]; y= yVec[1]; z= yVec[2]
    return np.array([sigma*(y-x), x*(rho-z)-y, x*y-beta*z])
# Başlangıç Koşulları
x0= 0
xSon= 10
n= 1000
y0Vek=np.array([1,1,1])
# Çöz
xTum, yVekTum= bym.add_coz_euler_sistem(f, x0, xSon, y0Vek, n)
# 2D Çiz
plt.plot(xTum, yVekTum[0,:], 'o-', color='r', label= 'x(t)')
plt.plot(xTum, yVekTum[1,:], 'o-', color='g', label= 'y(t)')
plt.plot(xTum, yVekTum[2,:], 'o-', color='b', label= 'z(t)')
plt.xlabel('t')
plt.legend()
plt.grid()
plt.show()
plt.close()
# 3D çiz
ax = plt.figure().add_subplot(projection='3d')
ax.plot(yVekTum[0,:], yVekTum[1,:], yVekTum[2,:], color='k')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.grid()
plt.show()
plt.close()
```

## Problem 2

Lotka-Volterra Modelini Euler yöntemiyle çözünüz. Sabitler için $a=1.5$, $b=1$, $c=3$ ve $d=1$ alınız. Başlangıç koşulu olarak 10 tavşan ($x_{0}$) ve 5 vaşak ($y_{0}$) alınız. En iyi sonucu görebilmek için $t=0-20$ aralığında ve $n= 1000$ adımda yapınız.
*Bu model av-avcı popülasyonunu veya tavşan-vaşak popülasyonu simülasyonudur.*

$$
\frac{dx}{dt}=ax-bxy
$$

$$
\frac{dy}{dt}=-cy+dxy
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
# Başlangıç Koşulları
a= 1.5
b= 1
c= 3
d= 1
def f(yVec, t):
    # yVec= [x, y]
    x= yVec[0]; y= yVec[1]
    return np.array([a*x- b*x*y, -c*y+ d*x*y])
# Başlangıç Koşulları
x0= 0
xStop= 20
n= 1000
y0Vec=np.array([10,5])
# Çöz
xAll, yVecAll= bym.add_coz_euler_sistem(f, x0, xStop, y0Vec, n)
# 2D Çiz
plt.plot(xAll, yVecAll[0,:], color='r', label= 'x (Tavşan)')
plt.plot(xAll, yVecAll[1,:], '--', color='g', label= 'y (Vaşak)')
plt.xlabel('t')
plt.legend()
plt.grid()
plt.show()
plt.close()
```
