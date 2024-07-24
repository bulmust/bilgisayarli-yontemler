---
title: "Sayısal İntegral - Problem Cevapları"
---

## Problem 1

Aşağıda verilen integrali Simpsons yöntemi ile 100 adımda hesaplayın. $I$ sonucunu ekrana yazdırın.

$$
    I=\sum_{i=1}^{100}\int_{0}^{i} x^{2} dx
$$

### Çözüm

```python
import numpy as np
import scipy.integrate as scInteg
def f5(x):
    return x**2

integralSonuc= 0
orneklemSayisi= 100
for i in range(1,101):
    # scipy.integrate.simpson metodu örneklem için çalışıyor. 
    # Fonksiyonu direkt olarak almıyor.
    orneklem= f5(np.linspace(0,i,orneklemSayisi))
    integralSonuc += scInteg.simpson(orneklem, np.linspace(0,i,orneklemSayisi))
print(f"(5. Soru)\nSonuc= {integralSonuc}")
```