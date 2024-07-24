---
title: "Eğri Uydurma (Fitting) - Problem Cevapları"
---

## Problem 1

1. Aşağıdaki veriyi kullanarak Lagrange interpolasyonu yapın.
2. Aşağıdaki veriyi kullanarak doğrusal (1. derece) en küçük kareler uydurması (fiting) yapın.


- En küçük kareler uydurmaları `numpy` paketinin `polyfit` fonksiyonunu kullanarak yapabilirsiniz.
- İnterpolasyonu ve uydurumayı $x'=(0,6)$ arasındaki noktalar için yapın.
- Veriyi (nokta olarak), Lagrange interpolasyonu ve uydurmaları aynı grafikte çizdirin ve `plt.savefig("soru3\_bilgisayar.png")` kodunu kullanarak kaydedin.


Veri: 

| Koordinat | 1. Nokta | 2. Nokta | 3. Nokta | 4. Nokta | 5. Nokta |
|:---------:|:--------:|:--------:|:--------:|:--------:|:--------:|
| x | $1$ | $2$ | $3$ | $4$ | $5$ |
| y | $-1$ | $1$ | $-2$ | $2$ | $-6$ |

### Çözüm

```python
import numpy as np
import matplotlib.pyplot as plt
import fizik365 as fiz

veri=np.array([[1,-1],[2,1],[3,-2],[4,2],[5,-6]]) # [3 Puan]
xHep=np.linspace(0,6,100) # [2 Puan]
yLag=fiz.lagrange_interpolasyon_dizi(veri[:,0],veri[:,1],xHep) # [10 Puan]
yUydurma1=np.polyfit(veri[:,0],veri[:,1],1) # [10 Puan]

plt.plot(veri[:,0],veri[:,1],'o') # [5 Puan]
plt.plot(xHep,yLag)
plt.plot(xHep,yUydurma1[0]*xHep+yUydurma1[1])
plt.savefig('soru3_bilgisayar.png')
plt.close()
```