---
title:  "BDP - Euler Yöntemi - Problem Çözümleri"
---

## Problem 1

1. Basit bir RC devresi ele alalım. Bu devrede voltaj kaynağı olmasın, kondansatör $t=0$ s'de $V_{0}=10$ V gerilime sahip olsun. Devrede $R=220$ k $\Omega$ direnci ve $C=10$ $\mu$ F kondansatörü olsun. Devre bu haldeyken devreyi tamamlayalım. Devrenin voltajı-zaman grafiğini Euler yöntemi kullanarak çiziniz.

$$
C\frac{dV}{dt}+\frac{V}{R}=0
$$

Analitik çözüm: $V(t) = V_{0}e^{-t/RC}$

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
# Başlangıç Değerleri
V_0=10 # Volt
R= 220000 # Ohm 
C= 10*1e-6 # Farad (micro=1e-6)
# Denklemin Sağ Tarafı
def f(V, t):
    return -V/(C*R)
# Başlangıç Değerleri
x0= 0
xSon= 10
n= 10
# Çöz
xTum, yTum= bym.add_coz_euler(f, x0, xSon, V_0, n)
# Çiz
plt.plot(xTum, yTum, 'o-', color='r', label= 'Euler')
plt.plot(xTum, V_0*(np.exp(-xTum/(R*C))), 'k-', label= 'Analitik')
plt.title('Soru 1.1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
plt.close()
```

## Problem 2

Thoryum-234'ün yarılanma ömrü $\tau=24.1$ gündür. $N_{0}=150$ g saf Thoryum-234 izotopu $100$ gün bekletilmektedir. İçerisinde kalan içerisinde kalan Thoryum-234 miktarı-zaman grafiğini Euler metodu kullanarak çiziniz. 

$$
\frac{dN}{dt}= -\frac{\ln 2}{\tau}N
$$

Analitik çözüm: $N(t) = N_{0}e^{-t(\ln 2/\tau)}$

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
# Başlangıç Değerleri
N_0= 150
tau=24.1
# Denklemin Sağ Tarafı
def f(N, t):
    return -(np.log(2)/tau)*N
# Başlangıç Değerleri
t0=0
tSon= 100
n= 10
# Çöz
tTum, NTum= bym.add_coz_euler(f, t0, tSon, N_0, n)
# Çiz
plt.plot(tTum, NTum, 'o-', color='r', label= 'Euler')
plt.plot(tTum, N_0*(np.exp(-(np.log(2)/tau)*tTum)), 'k-', label= 'Analitik')
plt.title('Soru 1.2')
plt.xlabel('t')
plt.ylabel('N')
plt.legend()
plt.grid()
plt.show()
plt.close()
```