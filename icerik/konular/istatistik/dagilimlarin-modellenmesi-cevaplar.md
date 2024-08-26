---
title: Dağılımlarin Modellenmesi - Problem Cevapları
---

## Problem 1

Heisenberg belirsizlik ilkesi aşağıdaki gibi verilir.

$$\sigma_{x} \sigma_{p} \geq \frac{\hbar}{2}$$

Burada $\sigma_{x}$, x'teki belirsizliği yani standart sapmayı verir. Bu eşitliği beklenen değerler cinsinden matematiksel olarak yazın.

### Çözüm

$$\sigma_{x} = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}$$

$$\sigma_{p} = \sqrt{\langle p^2 \rangle - \langle p \rangle^2}$$

$$\sigma_{x}\sigma_{p}= \sqrt{\langle x^2 \rangle - \langle x \rangle^2} \sqrt{\langle p^2 \rangle - \langle p \rangle^2}$$

$$\sigma_{x}\sigma_{p}= \sqrt{\langle x^2 \rangle \langle p^2 \rangle - \langle x^2 \rangle \langle p \rangle^2 - \langle x \rangle^2 \langle p^2 \rangle + \langle x \rangle^2 \langle p \rangle^2}$$

## Problem 2

Öğrendiğiniz tüm dağılımları bir fonksiyon olarak yazın.

- Eksponansiyel dağılım için $\lambda=0.1,1,2$ alın ve grafiğini çizdirin.
- Normal dağılım için $(\mu,\sigma)= (0,1),(0,2), (0,3)$ alın ve grafiğini çizdirin. Aynı şekilde $(\mu,\sigma)= (-2,1),(0,1), (2,1)$ alın ve grafiğini çizdirin.
- Poisson dağılımı için $\lambda=0.1,1,2$ alın ve grafiğini çizdirin.
- Maxwell-Boltzman dağılımı için $a=1,2,5$ alın ve grafiğini çizdirin. 3 Boyutlu Maxwell-Boltzman hız dağılımı formülünü kullanarak 1Mol He, Ne ve Ar atomlarının hız dağılımını çizdirin.
- Bose-Einstein dağılım için $(\mu [eV], T [K]) = (0,5), (0,100), (0,273)$ alın ve grafiğini çizdirin. Ayrı bir grafikte $(\mu [eV], T [K]) = (0,273), (0.01,273), (0.05,273)$ alın ve çizdirin.
- Fermi-Dirac dağılımı için $(\mu [eV], T [K]) = (0.5,5), (0.5,100), (0.5,273)$ alın ve grafiğini çizdirin. Ayrı bir grafikte $(\mu [eV], T [K]) = (0.5,273), (0.55,273), (0.85,273)$ alın ve çizdirin.

### Çözüm

```python
import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0,5,100)
lambda0= 0.1
lambda1= 1
lambda2= 2
plt.plot(x, lambda0*np.exp(-lambda0*x), 'b', label='$\\lambda=0.1$')
plt.plot(x, lambda1*np.exp(-lambda1*x), 'k', label='$\\lambda=1$')
plt.plot(x, lambda2*np.exp(-lambda2*x), 'r', label='$\\lambda=2$')
plt.title("Exponential Dağılım")
plt.legend()
plt.ylabel("PDF(x)")
plt.xlabel("x")
```

```python
import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-8,8,100)
mu= 0
sigma= 1
plt.plot(x, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((x-mu)/sigma)**2), 'b', label='$\\sigma=1$, $\\mu=0$')
sigma= 2
plt.plot(x, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((x-mu)/sigma)**2), 'k', label='$\\sigma=2$, $\\mu=0$')
sigma= 3
plt.plot(x, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((x-mu)/sigma)**2), 'r', label='$\\sigma=3$, $\\mu=0$')
plt.title("Normal Dağılım")
plt.ylabel("PDF(x)")
plt.xlabel("x")
plt.legend()
plt.show()
plt.close()

mu= 0
sigma= 1
plt.plot(x, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((x-mu)/sigma)**2), 'b', label='$\\sigma=1$, $\\mu=0$')
mu= 2
plt.plot(x, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((x-mu)/sigma)**2), 'k', label='$\\sigma=1$, $\\mu=2$')
mu= -2
plt.plot(x, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((x-mu)/sigma)**2), 'r', label='$\\sigma=1$, $\\mu=-2$')
plt.title("Normal Dağılım")
plt.ylabel("PDF(x)")
plt.xlabel("x")
plt.legend()
plt.show()
plt.close()
```

```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.special

x= np.arange(0,10)
lambda0= 0.1
lambda1= 1
lambda2= 2

plt.title("Poission Dağılım")
plt.plot(x, lambda0**x* np.exp(-lambda0)/scipy.special.factorial(x), '*-r', label='$\\lambda=0.1$')
plt.plot(x, lambda1**x* np.exp(-lambda1)/scipy.special.factorial(x), '*-b', label='$\\lambda=1$')
plt.plot(x, lambda2**x* np.exp(-lambda2)/scipy.special.factorial(x), '*-k', label='$\\lambda=2$')
plt.ylabel("PDF(x)")
plt.xlabel("x")
plt.legend()

print(f" 0! = {scipy.special.factorial(0)}")
print(f" 1! = {scipy.special.factorial(1)}")
print(f" 1.5! = {scipy.special.factorial(1.5):.2f}")
print(f" 2! = {scipy.special.factorial(2)}")
print(f" 2.5! = {scipy.special.factorial(2.5):.2f}")
print(f" 3! = {scipy.special.factorial(3)}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x= np.linspace(0,20,100)
a1= 1
a2= 2
a3= 5

plt.title("Maxwell-Boltzmann Dağılımı")
plt.plot(x, (np.sqrt(2/np.pi))* (x**2/a1**3)* np.exp(-x**2/(2*a1**2)), 'r', label=f'$a={a1}$')
plt.plot(x, (np.sqrt(2/np.pi))* (x**2/a2**3)* np.exp(-x**2/(2*a2**2)), 'b', label=f'$a={a2}$')
plt.plot(x, (np.sqrt(2/np.pi))* (x**2/a3**3)* np.exp(-x**2/(2*a3**2)), 'k', label=f'$a={a3}$')
plt.ylabel("PDF(x)")
plt.xlabel("x")
plt.legend()
plt.show()
plt.close()

def maxwellBoltzmannHiz_3d(v_m__s, m_g, T_K):
    #k_J__K= 1.38e-23 # J/K
    k_g_m2__s2_K= 1.38e-23/1.66e-27 # m2/s2/K
    return 4*np.pi* (v_m__s**2)* (m_g/(2*np.pi*k_g_m2__s2_K*T_K))**(3/2)* np.exp(-m_g* (v_m__s**2)/(2*k_g_m2__s2_K*T_K))
    # 
v_m__s= np.linspace(0,2500,1000)
mHe_g= 4.002602* 1.66054e-24* 6.022e23 # 1 Mol He atomunun kütlesi (g)
mNe_g= 20.1797* 1.66054e-24* 6.022e23 # 1 Mol Ne atomunun kütlesi (g)
mAr_g= 39.948* 1.66054e-24* 6.022e23 # 1 Mol Ar atomunun kütlesi (g)

T_K= 298.15 #K (25 °C)
plt.title(f"Maxwell-Boltzmann Dağılımı T={T_K} K")
plt.plot(v_m__s, maxwellBoltzmannHiz_3d(v_m__s, mHe_g, T_K), 'r', label=f'He')
plt.plot(v_m__s, maxwellBoltzmannHiz_3d(v_m__s, mNe_g, T_K), 'b', label=f'Ne')
plt.plot(v_m__s, maxwellBoltzmannHiz_3d(v_m__s, mAr_g, T_K), 'k', label=f'Ar')
plt.ylabel("PDF(v) (Normalize Edilmemiş)")
plt.xlabel("v (m/s)")
plt.legend()
plt.show()
plt.close()

# Beklenen değer ve varyans hesabı
hizDagilimiHe_m_s= maxwellBoltzmannHiz_3d(v_m__s, mHe_g, T_K)
seriHe_hizDagilimi_m_s= pd.Series(hizDagilimiHe_m_s, index=v_m__s)
print(f" He gazı için hız dağılımının beklenen değeri : {seriHe_hizDagilimi_m_s.mean():.2g} m/s")
print(f" He gazı için hız dağılımının standart sapması: {seriHe_hizDagilimi_m_s.std():.2g} m/s")
```

```python
import numpy as np
import matplotlib.pyplot as plt

mu_eV= 0
T_K= 5
T2_K= 100
T3_K= 273
k_eV__K= 8.617333262145e-5
energy_eV= np.linspace(0.0001,0.2,1000)

plt.title("Bose-Einstein Dağılım")
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu_eV)/(T_K*k_eV__K))-1), 'b', label=f'$T={T_K}$ K, $\\mu={mu_eV}$ eV')
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu_eV)/(T2_K*k_eV__K))-1), 'k', label=f'$T={T2_K}$ K, $\\mu={mu_eV}$ eV')
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu_eV)/(T3_K*k_eV__K))-1), 'r', label=f'$T={T3_K}$ K, $\\mu={mu_eV}$ eV')
plt.ylabel("PDF(E) (Normalize Edilmemiş)")
plt.xlabel("E (eV)")
plt.legend()
plt.ylim([-0.1,1.1])
plt.show()
plt.close()

T_K= 273
mu1_eV= 0.01
mu2_eV= 0.05
plt.title("Bose-Einstein Dağılım")
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu_eV)/(T_K*k_eV__K))-1), 'b', label=f'$T={T_K}$ K, $\\mu={mu_eV}$ eV')
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu1_eV)/(T_K*k_eV__K))-1), 'k', label=f'$T={T_K}$ K, $\\mu={mu1_eV}$ eV')
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu2_eV)/(T_K*k_eV__K))-1), 'r', label=f'$T={T_K}$ K, $\\mu={mu2_eV}$ eV')
plt.ylabel("PDF(E) (Normalize Edilmemiş)")
plt.xlabel("E (eV)")
plt.legend()
plt.ylim([-0.1,1])
plt.show()
plt.close()
```

```python
import numpy as np
import matplotlib.pyplot as plt

mu_eV= 0.5
T_K= 5
T2_K= 100
T3_K= 273
k_eV__K= 8.617333262145e-5
energy_eV= np.linspace(0.45,0.65,100)

plt.title("Fermi-Dirac Dağılım")
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu_eV)/(T_K*k_eV__K))+1), 'b', label=f'$T={T_K}$ K, $\\mu={mu_eV}$ eV')
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu_eV)/(T2_K*k_eV__K))+1), 'k', label=f'$T={T2_K}$ K, $\\mu={mu_eV}$ eV')
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu_eV)/(T3_K*k_eV__K))+1), 'r', label=f'$T={T3_K}$ K, $\\mu={mu_eV}$ eV')
plt.ylabel("PDF(E) (Normalize Edilmemiş)")
plt.xlabel("E (eV)")
plt.legend()
plt.show()
plt.close()

T_K= 273
mu1_eV= 0.55
mu2_eV= 0.85
plt.title("Fermi-Dirac Dağılım")
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu_eV)/(T_K*k_eV__K))+1), 'b', label=f'$T={T_K}$ K, $\\mu={mu_eV}$ eV')
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu1_eV)/(T_K*k_eV__K))+1), 'k', label=f'$T={T_K}$ K, $\\mu={mu1_eV}$ eV')
plt.plot(energy_eV, 1/(np.exp((energy_eV-mu2_eV)/(T_K*k_eV__K))+1), 'r', label=f'$T={T_K}$ K, $\\mu={mu2_eV}$ eV')
plt.ylabel("PDF(E) (Normalize Edilmemiş)")
plt.xlabel("E (eV)")
plt.legend()
plt.show()
plt.close()
```

## Problem 3

- Aşağıdaki sorularda eksponansiyel dağılımı $\lambda=2$ için, normal dağılımı $(\mu,\sigma)= (0,1)$ için hesaplayın. 
- Dağılımların hem formülünü kullanarak hem de `scipy.stats` kütüphanesini kullanarak yaratın. $x=1$ ile $x=100$ arasında 1000 nokta için hesaplayın.

1. Normal dağılımların ortalama değerini, varyansını, standart sapmasını hesaplayın ve ekrana yazdırın.
2. Normal ve eksponansiyel dağılımların CDF fonksiyonlarını teorik olarak hesaplayın. Normal dağılım için integral hali ile bırakın. İntegral almak için `scipy.integrate.quad` fonksiyonunu kullanabilirsiniz.
3. Normal ve eksponansiyel dağılımların PDF fonksiyonunu  ve aynı grafikte çizdirin.
4. Normal dağılımda $\mu=0$ için $\sigma=0.25,0.81,1,9$ olan 4 farklı dağılımı aynı grafikte çizdirin.
5. Normal dağılımda $\sigma=3$ için $\sigma=−5,-2.5,0,3,6$ olan 4 farklı dağılımı aynı grafikte çizdirin.

### Çözüm

## Problem 4

Normal (Gaussian) dağılım formülünü kullanarak standart dağılım formülünü ($\mu=0$, $\sigma=1$) elde ediniz.

### Çözüm

## Problem 5

1. Sonsuz kuyu içerisindeki bir parçacığın dalga fonksiyonu aşağıdaki gibidir.

$$\psi(x) = \sqrt{\frac{2}{a}} \sin{\left( \frac{n \pi x}{a} \right)}$$

Burada $a$ kuyunun genişliği, $n$ ise parçacığın enerji seviyesidir.

1. $a = 10$ ve $n = 1$ olarak sabit kabul edilsin. Bu durumda $\psi(x)$ fonksiyonunu konuma göre çizdirin.
2. Olasılık yoğunluğu dalga fonksiyonunun karesi ile verilir. $\psi(x)$ fonksiyonunun karesini çizdirin.
3. Yukarıdaki dalga fonksiyonunu $n=2$ veya $n=3$ için de çizerek gözlemleyin.
4. $n=1$ için olasılık yoğunluğunun standart sapmasını bulun.
5. $n=1$ için olasılık yoğunluğunun ortalamasını bulun.
6. $n=1$ için olasılık yoğunluğunun varyansını bulun.
7. Yukarıda elde ettiğiniz değerler olasılık yoğunluğunun standart sapması oluğunu unutmayın. Yani fizikten bildiğimiz $<x>$ büyüklüğünü hesaplamıyoruz. Bunun için $<x> = \int_{0}^{a} x \psi(x)^{2} dx$ integralini hesaplamamız gerekir. 
8. Kuyu içerisinde bir parçacığın $x=4$ noktasında bulunma olasılığını bulun.
9. Kümülatif yoğunluk fonksiyonunu çizdirin. Bunun için `np.cumsum()` fonksiyonunu kullanın ve elde ettiğiniz cdf dizisini de cdf'in son değerine bölerek $1$'e normalize etmeyi unutmayın.

### Çözüm

```python
# https://www.colby.edu/chemistry/PChem/notes/PrtinboxHeisenbergn.pdf

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

a= 10
x= np.linspace(0, a, 10000)
n=1

psi= np.sqrt(2/a )*np.sin(n*np.pi*x/a)
psi_square= psi**2


plt.plot(x, psi)
plt.ylabel("Dalga Fonksiyonu")
plt.xlabel("Konum")
#plt.show()
plt.close()

plt.plot(x, psi_square, color="red")
plt.ylabel("Olasılık Yoğunluğu")
plt.xlabel("Konum")
plt.show()
plt.close()

print(f"Standart Sapma: {np.std(psi_square)}")
print(f"Ortalama: {np.mean(psi_square)}")
print(f"Varyans: {np.var(psi_square)}")
print(f"Standart Sapma: {np.std(psi_square)}")

index= np.abs(x - 4).argmin()

print(f"Parçacığın x=4 noktasında olma olasılığı: {psi_square[index]}")

psi_square_cdf= np.cumsum(psi_square)

plt.plot(x, psi_square_cdf/psi_square_cdf[-1])
plt.ylabel("Kümülatif Olasılık Yoğunluğu")
plt.xlabel("Konum")
plt.show()
```

## Problem 6

Aşağıdaki dağılımları fonksiyon olarak yazın ve verilen değerler için PDF grafiklerini çizdirin.

- Eksponansiyel dağılım için $\lambda=0.1,1,2$ alın ve grafiğini çizdirin. ($x=[0,5]$)
- Normal dağılım için $(\mu,\sigma)= (0,1),(0,2), (0,3)$ alın ve grafiğini çizdirin. Aynı şekilde $(\mu,\sigma)= (-2,1),(0,1), (2,1)$ alın ve grafiğini çizdirin. ($x=[-8,8]$)
- Poisson dağılımı için $\lambda=0.1,1,2$ alın ve grafiğini çizdirin. Faktöriyel almak için `scipy.special.factorial()` fonksiyonunu kullanın. ($x=[0,10]$)
- 3 Boyutlu Maxwell-Boltzman hız dağılımı formülünü kullanarak 1Mol He, Ne ve Ar atomlarının hız dağılımını çizdirin. Sıcaklığı $T=298.15$ K alın. ($v=[0,2500]$)
- Bose-Einstein dağılım için $(\mu [eV], T [K]) = (0,5), (0,100), (0,273)$ alın ve grafiğini çizdirin. Ayrı bir grafikte $(\mu [eV], T [K]) = (0,273), (0.01,273), (0.05,273)$ alın ve çizdirin. Grafikde y eksenini -0.1 ile 1.1 arasında sınırlayın. ($E=[0.0001,0.2]$)
- Fermi-Dirac dağılımı için $(\mu [eV], T [K]) = (0.5,5), (0.5,100), (0.5,273)$ alın ve grafiğini çizdirin. Ayrı bir grafikte $(\mu [eV], T [K]) = (0.5,273), (0.55,273), (0.85,273)$ alın ve çizdirin. ($E=[0.45,0.65]$)

**Yaralı bilgiler** 

- Avagadro sayısı $N_{A} = 6.022 \times 10^{23}$
- Boltzman sabiti $k = 1.380649 \times 10^{-23} J/K$
- Boltzman sabiti $k = 8313.25 g~ m^{2}~ s^{-2}/K$
- Boltzman sabiti $k = 8.617e-5 \times 10^{-5} eV/K$
- $1 eV = 1.602176634 \times 10^{-19} J$
- Helyumun kütlesi $m_{He} = 4.002602 u$
- Neonun kütlesi $m_{Ne} = 20.1797 u$
- Argonun kütlesi $m_{Ar} = 39.948 u$
- $1 u = 1.66053906660 \times 10^{-23} g$.
- Işık hızı $c = 299792458 m/s$
- Planck sabiti $h = 6.62607015 \times 10^{-34} J s$
- $1 \AA = 10^{-10} m$
- $1 nm = 10^{-9} m$
- $1 \mu m = 10^{-6} m$


### Çözüm

```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.special

def fexp(x, lamb):
    return lamb*np.exp(-lamb*x)
def fnorm(x, mu, sigma):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sigma**2))
def fpois(x, lamb):
    return lamb**x*np.exp(-lamb)/scipy.special.factorial(x)
def fmaxwell3d(v_m__s, m_g, T_K):
    k_g_m2__s2_K= 8313.25 # g m^2/(s^2 K)
    return 4* np.pi* (v_m__s**2)*\
        (m_g/(2*np.pi*k_g_m2__s2_K*T_K))**(3/2)*\
            np.exp(-m_g* (v_m__s**2)/(2*k_g_m2__s2_K*T_K))
def fbose(E_eV, mu_eV, T_K):
    k_eV__K= 8.617e-5 # eV/K
    return 1/(np.exp((E_eV-mu_eV)/(k_eV__K*T_K))-1)
def ffermi(E_eV, mu_eV, T_K):
    k_eV__K= 8.617e-5 # eV/K
    return 1/(np.exp((E_eV-mu_eV)/(k_eV__K*T_K))+1)

x= np.linspace(0,5,100)
plt.plot(x, fexp(x, 0.1), label='lambda=0.1')
plt.plot(x, fexp(x, 1), label='lambda=1')
plt.plot(x, fexp(x, 2), label='lambda=2')
plt.title("Exponential Dağılım")
plt.legend()
plt.ylabel("PDF(x)")
plt.xlabel("x")
plt.show()
plt.close()

x= np.linspace(-8,8,100)
plt.plot(x, fnorm(x, 0, 1), label='sigma=1')
plt.plot(x, fnorm(x, 0, 2), label='sigma=2')
plt.plot(x, fnorm(x, 0, 3), label='sigma=3')
plt.title("Normal Dağılım, mu=0")
plt.legend()
plt.ylabel("PDF(x)")
plt.xlabel("x")
plt.show()
plt.close()

plt.plot(x, fnorm(x, -2, 1), label='mu=-2')
plt.plot(x, fnorm(x, 0, 1), label='mu=0')
plt.plot(x, fnorm(x, 2, 1), label='mu=2')
plt.title("Normal Dağılım, sigma=1")
plt.legend()
plt.ylabel("PDF(x)")
plt.xlabel("x")
plt.show()
plt.close()

x= np.arange(0,10)
plt.plot(x, fpois(x, 0.1), label='lambda=0.1')
plt.plot(x, fpois(x, 1), label='lambda=1')
plt.plot(x, fpois(x, 2), label='lambda=2')
plt.title("Poisson Dağılım, sigma=1")
plt.legend()
plt.ylabel("PDF(x)")
plt.xlabel("x")
plt.show()
plt.close()

v_m__s= np.linspace(0,2500,1000)
mHe_g= 4.002602* 1.66054e-24* 6.022e23 # 1 Mol He atomunun kütlesi (g)
mNe_g= 20.1797* 1.66054e-24* 6.022e23 # 1 Mol Ne atomunun kütlesi (g)
mAr_g= 39.948* 1.66054e-24* 6.022e23 # 1 Mol Ar atomunun kütlesi (g)

T_K= 298.15 #K (25 °C)
plt.title(f"Maxwell-Boltzmann Dağılımı T={T_K} K")
plt.plot(v_m__s, fmaxwell3d(v_m__s, mHe_g, T_K), 'r', label=f'He')
plt.plot(v_m__s, fmaxwell3d(v_m__s, mNe_g, T_K), 'b', label=f'Ne')
plt.plot(v_m__s, fmaxwell3d(v_m__s, mAr_g, T_K), 'k', label=f'Ar')
plt.ylabel("PDF(v) (Normalize Edilmemiş)")
plt.xlabel("v (m/s)")
plt.legend()
plt.show()
plt.close()

energy_eV= np.linspace(0.0001,0.2,1000)
plt.plot(energy_eV, fbose(energy_eV, 0, 5), 'b', label=f'T=5 K')
plt.plot(energy_eV, fbose(energy_eV, 0, 100), 'k', label=f'T=100 K')
plt.plot(energy_eV, fbose(energy_eV, 0, 273), 'r', label=f'T=273 K')
plt.ylabel("PDF(E) (Normalize Edilmemiş), mu=0")
plt.xlabel("E (eV)")
plt.legend()
plt.ylim([-0.1,1.1])
plt.show()
plt.close()

plt.plot(energy_eV, fbose(energy_eV, 0, 273), 'b', label=f'mu=0 K')
plt.plot(energy_eV, fbose(energy_eV, 0.01, 273), 'k', label=f'mu=0.01 K')
plt.plot(energy_eV, fbose(energy_eV, 0.05, 273), 'r', label=f'mu=0.05 K')
plt.ylabel("PDF(E) (Normalize Edilmemiş), T=273 K")
plt.xlabel("E (eV)")
plt.legend()
plt.ylim([-0.1,1.1])
plt.show()
plt.close()

energy_eV= np.linspace(0.45,0.65,100)
plt.plot(energy_eV, ffermi(energy_eV, 0.5, 5), 'b', label=f'T=5 K')
plt.plot(energy_eV, ffermi(energy_eV, 0.5, 100), 'k', label=f'T=100 K')
plt.plot(energy_eV, ffermi(energy_eV, 0.5, 273), 'r', label=f'T=273 K')
plt.ylabel("PDF(E) (Normalize Edilmemiş), mu=0.5")
plt.xlabel("E (eV)")
plt.legend()
plt.show()
plt.close()

plt.plot(energy_eV, ffermi(energy_eV, 0.5, 273), 'b', label=f'mu=0.5 K')
plt.plot(energy_eV, ffermi(energy_eV, 0.55, 273), 'k', label=f'mu=0.55 K')
plt.plot(energy_eV, ffermi(energy_eV, 0.85, 273), 'r', label=f'mu=0.85 K')
plt.ylabel("PDF(E) (Normalize Edilmemiş), T=273 K")
plt.xlabel("E (eV)")
plt.legend()
plt.show()
plt.close()
```
