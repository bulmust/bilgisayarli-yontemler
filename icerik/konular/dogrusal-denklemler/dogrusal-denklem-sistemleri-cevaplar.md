---
title: "Doğrusal Denklem Sistemleri - Problem Cevapları"
---

## Problem 1

Aşağıda verilen denklem sistemini Gauss eleme yöntemi ile çözünüz. Çözüm elde ederken Eq(i) - $\lambda$ $\times$ Eq(j) $\rightarrow$ Eq(i) işlemini kullanmak zorundasınız.

$$
\begin{bmatrix}    1 & 2\\ 3 & 4    \end{bmatrix}\begin{bmatrix}    x_{1} \\ x_{2}   \end{bmatrix}= \begin{bmatrix}    8 \\ 10    \end{bmatrix}
$$

### Çözüm

Eq(2) - $3 \times$ Eq(1) $\rightarrow$ Eq(2)

Katsayı matrisi ve sonuç matrisi aşağıdaki gibi olacaktır.

$$
\begin{bmatrix}    1 & 2\\ 0 & -2    \end{bmatrix}\begin{bmatrix}    x_{1} \\ x_{2}    \end{bmatrix}= \begin{bmatrix}    8\\-14    \end{bmatrix}
$$

Katsayı matrisi üst üçgen matrise dönüştürülmüştür. Geri yerine koyma metodu uygulayacağız.

$$
\begin{align*}
    x_{2} &= \frac{-14}{-2} = 7\\
    x_{1} + 2x_{2} &= 8 \rightarrow x_{1}= -6
\end{align*}
$$

Çözüm vektörü

$$
\begin{bmatrix}    x_{1} \\ x_{2}    \end{bmatrix} = \begin{bmatrix}    -6 \\ 7    \end{bmatrix}
$$

olur.

## Problem 2

Aşağıda verilen denklem sistemini Doolittle'ın LU ayrıştırma yöntemi ile çözünüz.

$$
\begin{bmatrix}    1 & 2\\ 3 & 4    \end{bmatrix}\begin{bmatrix}    x_{1} \\ x_{2}   \end{bmatrix}= \begin{bmatrix}    12 \\ 14    \end{bmatrix}
$$

### Çözüm

Doolittle'ın LU ayrıştırma yöntemi aşağıdaki gibi yazılır.

$$
\begin{bmatrix}A_{11} & A_{12}\\ A_{21} & A_{22} \end{bmatrix} = \begin{bmatrix}1 & 2\\ 3 & 4\end{bmatrix} \\
    \begin{bmatrix}1 & 0\\ L_{21} & 1\end{bmatrix} \begin{bmatrix}U_{11} & U_{12}\\ 0 & U_{22}\end{bmatrix} = \begin{bmatrix}1 & 2\\ 3 & 4\end{bmatrix}\\
    \begin{bmatrix}U_{11} & U_{12}\\ L_{21}U_{11} & L_{21}U_{12} + U_{22}\end{bmatrix} = \begin{bmatrix}1 & 2\\ 3 & 4\end{bmatrix}
$$

L ve U'nun bileşenleri

$$
U_{11} = 1\text{,} \qquad U_{12} = 2\text{,} \qquad L_{21} = \frac{3}{1} = 3\text{,} \qquad U_{22} = 4 - 3 \times 2 = -2
$$

L ve U matrisleri aşağıdaki gibidir.

$$
L=\begin{bmatrix}1 & 0\\ 3 & 1\end{bmatrix} \qquad \text{,} \qquad U=\begin{bmatrix}1 & 2\\ 0 & -2\end{bmatrix}
$$

Çözümü elde edebilmek için $ \vec{y} $ vektörünü tanımlayalım.

$$
LU \vec{x} =\vec{b} \quad \Rightarrow \quad L\vec{y} = \vec{b} \quad \Rightarrow \quad U\vec{x} = \vec{y}
$$

Önce $\vec{y}$ vektörünü bulalım.

$$
\begin{bmatrix}1 & 0\\ 3 & 1\end{bmatrix} \begin{bmatrix}y_{1} \\ y_{2}\end{bmatrix} = \begin{bmatrix}12\\14\end{bmatrix} \\
y_{1} = 12\\
3y_{1}+y_{2} = 14 \rightarrow y_{2} = -22
$$

Ardından $U\vec{x} = \vec{y}$ bağıntısını kullanarak çözümü elde edelim.

$$
\begin{bmatrix}1 & 2\\ 0 & -2\end{bmatrix} \begin{bmatrix}x_{3} \\ x_{4}\end{bmatrix} = \begin{bmatrix}12\\-22\end{bmatrix} \\
\qquad\\
x_{4} = \frac{-22}{-2} \rightarrow x_{4} = 11\\
x_{3} + 2x_{4} = 12 \rightarrow x_{3} = -10
$$

Çözüm vektörü

$$
\begin{bmatrix}x_{3}\\x_{4}\end{bmatrix} = \begin{bmatrix}-10\\11\end{bmatrix}
$$

olur.

## Problem 3

Aşağıda yazılan denklem sistemini Doolittle'ın LU ayrıştırma yöntemiyle çözünüz ve $ \theta_{x}, \theta_{y}, \theta_{z} $'nin değerlerini elde ediniz.

$$
\begin{align*}
    \theta_{x}-\theta_{y}+2\theta_{z}=&7\\
    -\theta_{x}+2\theta_{y}-\theta_{z}=&0\\
    \theta_{y}-\theta_{z}=&-1
\end{align*}
$$

### Çözüm

Matris form aşağıdaki gibi olur. [5 Puan]

$$
\begin{bmatrix}
    1 & -1 & 2\\
    -1 & 2 & -1\\
    0 & 1 & -1
\end{bmatrix}
\begin{bmatrix}
    \theta_{x}\\
    \theta_{y}\\
    \theta_{z}
\end{bmatrix}
=
\begin{bmatrix}
    7\\
    0\\
    -1
\end{bmatrix}
$$

LU ayrıştırma yöntemiyle L ve U matrisleri bulunur. [10 Puan]

$$
L= \begin{bmatrix}    1 & 0 & 0 \\ l_{21} & 1 & 0 \\ l_{31} & l_{32} & 1    \end{bmatrix} \qquad \text{,} \qquad U= \begin{bmatrix}    u_{11} & u_{12} & u_{13} \\ 0 & u_{22} & u_{23} \\ 0 & 0 & u_{33}    \end{bmatrix}
$$

olmak üzere $A$ matrisi aşağıdaki gibi yazılır.

$$
A= \begin{bmatrix}    u_{11} & u_{12} & u_{13} \\ l_{21}u_{11} & l_{21}u_{12}+u_{22} & l_{21}u_{13}+u_{23} \\ l_{31}u_{11} & l_{31}u_{12}+l_{32}u_{22} & l_{31}u_{13}+l_{32}u_{23}+u_{33}    \end{bmatrix}
$$

$$
u_{11}= 1 \qquad \text{,} \qquad u_{12}= -1 \qquad \text{,} \qquad u_{13}= 2
$$

$$
l_{21}= -1 \qquad \text{,} \qquad u_{22}= 1 \qquad \text{,} \qquad u_{23}= 1
$$

$$
l_{31}= 0 \qquad \text{,} \qquad l_{32}= 1 \qquad \text{,} \qquad u_{33}= -2
$$

O halde U ve L matrisleri aşağıdaki gibi olur.

$$
L= \begin{bmatrix}    1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 1 & 1    \end{bmatrix} \qquad \text{,} \qquad U= \begin{bmatrix}    1 & -1 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & -2    \end{bmatrix}
$$

U ve L matrislerini kullanarak denkelm sistemi çözülür. [5 Puan]

$$
A\theta = b \qquad \Rightarrow \qquad LU\theta = b
$$

$$
L(U\theta) = b
$$

$$
L\alpha= b \qquad
$$

$$
\begin{bmatrix}    1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 1 & 1    \end{bmatrix} \begin{bmatrix}    \alpha_{1} \\ \alpha_{2} \\ \alpha_{3}    \end{bmatrix} = \begin{bmatrix}    7 \\ 0 \\ -1    \end{bmatrix}
$$

$$
\alpha_{1}= 7 \qquad \text{,} \qquad \alpha_{2}= 7 \qquad \text{,} \qquad \alpha_{3}= -8
$$

$$
U\theta = \alpha
$$

$$
\begin{bmatrix}    1 & -1 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & -2    \end{bmatrix} \begin{bmatrix}    \theta_{x} \\ \theta_{y} \\ \theta_{z}    \end{bmatrix} = \begin{bmatrix}    7 \\ 7 \\ -8    \end{bmatrix}
$$

$$
\theta_{z}= 4 \qquad \text{,} \qquad \theta_{y}= 3 \qquad \text{,} \qquad \theta_{x}= 2
$$

## Problem 4

Aşağıdaki $ A\vec{x}=\vec{b} $ doğrusal denklem sistemini istediğiniz sayısal yöntem ile çözün. 

Çözümü yani $ \vec{x} $ vektörünün elemanlarını ekrana yazdırın.

$$
\begin{bmatrix}    4&1&3&2&1&1\\0&3&1&0&-1&1\\0&1&2&0&-1&1\\0&-1&1&6&-1&1\\0&1&0&0&-6&1\\0&0&0&0&0&7    \end{bmatrix}\begin{bmatrix}    x_{0}\\ x_{1}\\ x_{2}\\y_{0}\\y_{1}\\y_{2}    \end{bmatrix}= \begin{bmatrix}    19\\3\\3\\-1\\-36\\35    \end{bmatrix}
$$

*Not: Çözümünüzde $\dots e^{-16}$ gibi sayılar çıktıysa bu 0 demektir.*

### Çözüm

```python
import numpy as np

A=np.array([[4,1,3,2,1,1],[0,3,1,0,-1,1],[0,1,2,0,-1,1],[0,-1,1,6,-1,1],[0,1,0,0,-6,1],[0,0,0,0,0,7]]) # [5 Puan]
b=np.array([19,3,3,-1,-36,35]) # [5 Puan]

# Sistemin Çözümü
x = np.linalg.solve(A, b) # [10 Puan]
print('Soru 2\n',x) #x=[0,1,2,0,7,5]

# Alternatif Yol 1
#x = np.linalg.inv(A).dot(b)
#print('Soru 2\n',x)

# Alternatif Yol 2
#import fiz365 as fiz
#x = fiz.gaussElimin(A, b)
#print('Soru 2\n',x)

# Alternatif Yol 3
#import fiz365 as fiz
#x = fiz.LUsolve(A, b)
#print('Soru 2\n',x)

# Alternatif Yol 4
#import fiz365 as fiz
#x = fiz.fiz.gaussPivot(A, b)
#print('Soru 2\n',x)
```