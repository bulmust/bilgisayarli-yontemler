---
title: "Dogrusal Denklemler ve Çözümleri - Problem Cevapları"
---

## Problem 1

Aşağıda verilen denklem sistemlerini **LU ayrıştırma** yöntemiyle çözün. 

- Hem **L** hem de **U** matrislerini ekrana yazdırın.
- Çözümü ($x_{1,2,3}$ ve $y_{1,2,3}$) ekrana yazdırın.

Denklem sistemi:

$$
\begin{bmatrix}
    1 & 3 & 5 \\ 7 & 9 & 11 \\ 13 & 15 & 42
\end{bmatrix}\begin{bmatrix}
    x_1 & y_{1}\\ x_2 & y_{2}\\ x_3 & y_{3}
\end{bmatrix}=\begin{bmatrix}
    1 & 3 \\ 2 & 7 \\ 42 & 12
\end{bmatrix}
$$

### Çözüm

```python
import numpy as np
import scipy.linalg as spLin
coeffMat= np.array([[1,3,5],[7,9,11],[13,15,42]])
bVec= np.array([[1,2,42],[3,7,12]])

P,L,U=spLin.lu(coeffMat)
print(f"(3. Soru)\n L= {L}\nU= {U}\n"); del L,U
print(f"Sonuc (x1,x2,x3)= {spLin.solve(coeffMat, bVec[0])}")
print(f"Sonuc (y1,y2,y3)= {spLin.solve(coeffMat, bVec[1])}")
```