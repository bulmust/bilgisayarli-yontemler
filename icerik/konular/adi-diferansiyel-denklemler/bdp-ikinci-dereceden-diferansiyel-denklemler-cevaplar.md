---
title: "BDP - İkinci Dereceden Diferansiyel Denklemler - Promlem Cevapları"
---

## Problem 1 

Sürtünmesiz bir düzlemde serbest düşen bir parçacığın konum zaman grafiğini ve hız zaman grafiğini Newton'un ikinci yasasını kullanarak çizin. $g=9.81$ m/s $^{2}$ sabit düşüş ivmesi. Denklemleri Euler yöntemi ile çözün. Başlangıç koşulları $v(0)=10$ ve $y(0)=100$ olsun. Çözümü $n=100$ s adımda yapın. Zaman aralığı $t=0$ s'den $t=10$ s'ye kadar olsun.

$v(0)=0$ m/s için çözülen grafikler ile karşılaştırın.

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
# Global değişkenler
g=9.81
# Denklemin sağ tarafı
def F(yVek, x):
    # F=m*a
    # F=m*y''(t)
    # -g=y''(t)
    # y'(t)=v(t)
    # v'(t)=-g
    return np.array([yVek[1], -g])
# Başlangıç koşulları
x0=0
yVek=np.array([100, 0])
yVek10=np.array([100, 10])
xStop=5
n=100
# Çöz (v(0)=0)
xTum, yVekTum = bym.add_coz_euler_sistem(F, x0, xStop, yVek, n)
# Çöz (v(0)=10)
xTum10, yVekTum10 = bym.add_coz_euler_sistem(F, x0, xStop, yVek10, n)
# Analitik çözüm
# y(t) = y0 + v0*t - (1/2)*g*t^2
# v(t) = v0 - g*t
yAnalitik= yVek[0] + yVek[1]*xTum - (1/2)*g*xTum**2
yAnalitik10= yVek10[0] + yVek10[1]*xTum10 - (1/2)*g*xTum10**2
vAnalitik= yVek[1] - g*xTum
vAnalitik10= yVek10[1] - g*xTum10
# Çiz (v(0)=0)
fig,axs=plt.subplots(1,2)
# Soldaki grafik
axs[0].plot(xTum, yVekTum[0,:], 'o-', color='r', label='Euler $y(t)$')
axs[0].plot(xTum, yAnalitik, 'k', label='Analitik $y(t)$')
axs[0].set_ylabel('$y(t)$')
axs[0].legend()
# Sağdaki grafik
axs[1].plot(xTum, yVekTum[1,:], 'o-', color='r', label='Euler $v(t)$')
axs[1].plot(xTum, vAnalitik, 'k', label='Analitik $v(t)$')
axs[1].set_ylabel('$v(t)$')
axs[1].set_xlabel('$t$')
axs[1].legend()
# Sıkıştır
plt.tight_layout()
# Göster
plt.show()
# Kapat
plt.close()

# Çiz (v(0)=10)
fig,axs=plt.subplots(1,2)
# Soldaki grafik
axs[0].plot(xTum10, yVekTum10[0,:], 'o-', color='r', label='Euler $y(t)$')
axs[0].plot(xTum10, yAnalitik10, 'k', label='Analitik $y(t)$')
axs[0].set_ylabel('$y(t)$')
axs[0].legend()
# Sağdaki grafik
axs[1].plot(xTum10, yVekTum10[1,:], 'o-', color='r', label='Euler $v(t)$')
axs[1].plot(xTum10, vAnalitik10, 'k', label='Analitik $v(t)$')
axs[1].set_ylabel('$v(t)$')
axs[1].set_xlabel('$t$')
axs[1].legend()
# Sıkıştır
plt.tight_layout()
# Göster
plt.show()
# Kapat
plt.close()
```

## Problem 2

Yatay düzlemde $k=100$ N/m sabitine sahip $m=1$ kg kütleli yay olsun. Bu cisme denge noktasından $x_{0}=0.1$ m sıkıştırılarak harekete başlatılıyor. Cisim bırakıldığı anda hızı $v_{0}=0$ m/s. Bu cismin hareket denklemini $t=0-5$ aralığında Euler yöntemiyle çözünüz.

$$
-kx=m\frac{d^{2}x}{dt^{2}}
$$

Analitik çözüm: $x(t) = A\cos(\sqrt{k/m}x)+B\sin(\sqrt{k/m}x)$

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
# Global değişkenler
k=100
m=1
# Fonksiyon
def f(yVec,t):
    # yVec= [x, v]
    x= yVec[0]
    v= yVec[1]
    return np.array([v, -k/m*x])
# Başlangıç koşulları
x0= 0
xSon= 5
n= 100
y0Vek=np.array([0.1,0])
# Çöz
xTum, yVekTum= bym.add_coz_euler_sistem(f, x0, xSon, y0Vek, n)
# Çiz
plt.ylim([-0.2, 0.2])
plt.plot(xTum, yVekTum[0,:], 'o-', color='r', label= 'Euler')
plt.plot(xTum, (0.1)*np.cos(np.sqrt(k/m)*xTum), 'k-', label= 'Analitik')
plt.xlabel('t')
plt.legend()
plt.grid()
plt.show()
plt.close()
```

## Problem 3

@sec-problem2 bölümündeki soruyu $F_{sürtünme}= -bv$ sürtünme kuvveti varlığında çözünüz. Burada $b=1$ Ns/m sabit ve $v$ cismin hızıdır.

$$
-b\frac{dx}{dt}-kx=m\frac{d^{2}x}{dt^{2}}
$$


Analitik çözüm: $x(t) = Ae^{-\sigma t}e^{i\omega t}+ Be^{-\sigma t}e^{-i \omega t}$. Burada frekans $\omega = \sqrt{(k/m)-(b^{2}/4m^{2})}$ ve genliği belirleyen terim $\sigma=b/2m$ [@web2024Feb-2].

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
# Global değişkenler
k=100
m=1
b=1
# Fonksiyon
def f(yVec,t):
    # yVec= [x, v]
    x= yVec[0]
    v= yVec[1]
    return np.array([v, (-b*v)-(k/m*x)])
# Başlangıç koşulları
x0= 0
xSon= 5
n= 2000
y0Vek=np.array([0.1,0])
# Çöz
xTum, yVekTum= bym.add_coz_euler_sistem(f, x0, xSon, y0Vek, n)
# Analitik çözüm
dampFreq= np.sqrt( (k/ m)- ((b**2)/ (4* m**2)) )
genlik= np.exp(-(b/(2*m))*xTum)
A= 0.05
B=0.05
yAnalitik= A*genlik*np.exp(1j*dampFreq* xTum)+ B*genlik*np.exp(-1j*dampFreq* xTum)
print(f"{yAnalitik[-1]:.4f}")
# Çiz
plt.ylim([-0.2, 0.2])
plt.plot(xTum, yVekTum[0,:], 'o-', color='r', label= 'Euler')
plt.plot(xTum, np.real(yAnalitik), 'k-', label= 'Analitik')
plt.xlabel('t')
plt.legend()
plt.grid()
plt.show()
plt.close()
```

## Problem 4

Düşey düzlemde $m=1$ kg kütleli bir cisim salınsın. Bu cisim denge noktasından $\theta_{0}=\pi/9$ rad açı ile harekete başlıyor. Cisim bırakıldığı anda açısal hızı $\omega_{0}=$ rad/s. Bu cismin hareket denklemini $t=0-10$ arasında Euler yöntemiyle çözünüz. En uygun sonuç için $n=10000$ adım alınız. ($g=9.81$)

$$
\frac{d^{2}\theta}{dt^{2}}=-\frac{g}{l}\sin \theta
$$

Analitik çözüm: $x(t) = A\cos(\sqrt{g/l}x)+B\sin(\sqrt{g/l}x)$

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
# Global değişkenler
l=1
g=9.81
# Fonksiyon
def f(yVec,t):
    # yVec= [x, v]
    x= yVec[0]
    v= yVec[1]
    return np.array([v, -g/l*np.sin(x)])
# Başlangıç koşulları
x0= 0
xSon= 10
n= 100
y0Vek=np.array([np.pi/9,0])
# Çöz
xTum, yVekTum= bym.add_coz_euler_sistem(f, x0, xSon, y0Vek, n)
# Çiz
plt.plot(xTum, yVekTum[0,:], 'o-', color='r', label= 'Euler')
plt.plot(xTum, y0Vek[0]*np.cos(np.sqrt(g/l)*xTum), 'k-', label= 'Analitik')
plt.xlabel('t')
plt.legend()
plt.grid()
plt.show()
plt.close()
```

## Problem 5

@sec-problem4 bölümündeki problemi $\theta_{0}=\pi/2$ başlangıç koşulu için tekrar çalıştırınız. $\sin \theta \approx \theta$ yaklaşıklığı artık geçerli olmadığı için analitik çözümün hatalı olduğunu unutmayınız.

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
# Global değişkenler
l=1
g=9.81
# Fonksiyon
def f(yVec,t):
    # yVec= [x, v]
    x= yVec[0]
    v= yVec[1]
    return np.array([v, -g/l*np.sin(x)])
# Başlangıç koşulları
x0= 0
xSon= 10
n= 100
y0Vek=np.array([np.pi/2,0])
# Çöz
xTum, yVekTum= bym.add_coz_euler_sistem(f, x0, xSon, y0Vek, n)
# Çiz
plt.plot(xTum, yVekTum[0,:], 'o-', color='r', label= 'Euler')
plt.plot(xTum, y0Vek[0]*np.cos(np.sqrt(g/l)*xTum), 'k-', label= 'Analitik')
plt.xlabel('t')
plt.legend()
plt.grid()
plt.show()
plt.close()
```

## Problem 6

İki cisim problemini (baryosentrik yani merkezdeki cisim hareket etmesin) Euler yöntemiyle ($n= 1000, 10000, 100000$ adımda) çözünüz. Burada $\mu=3.98\times 10^{5}$ km $^{3}$/s $^{2}$, $x_{0}=-2500$ km, $y_{0}=-5500$ km, $v_{x0}=7.5$ km/s, $v_{y0}=0.5$ km/s olarak alın. Aşağıdaki denklemleri $t=0-100000$ s arasında çözün. $y-x$ grafiği çizin. $(x,y)=(0,0)$ noktası merkezdeki cismin konumunu göstersin.

$$
\frac{d^{2}x}{dt^{2}}=-\frac{\mu}{(x^{2}+y^{2})^{3/2}}x
$$

$$
\frac{d^{2}y}{dt^{2}}=-\frac{\mu}{(x^{2}+y^{2})^{3/2}}y
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
# Global değişkenler
mu=3.986*10**5
# Fonksiyon
def f(yVec,t):
    # yVec= [x, v_x, y, v_y]
    x= yVec[0]
    v_x= yVec[1]
    y= yVec[2]
    v_y= yVec[3]
    r= np.sqrt(x**2+y**2)
    return np.array([v_x, -mu*x/r**3, v_y, -mu*y/r**3])
# Başlangıç koşulları
x0= 0
xSon= 100000
n= 10000
y0Vek= np.array([-2500,7.5,-5500,0.5])
# Çöz
xTum, yVekTum= bym.add_coz_euler_sistem(f, x0, xSon, y0Vek, n)
# Çiz
plt.plot(0, 0, 'o-', color='k', label='Güneş')
plt.plot(yVekTum[0,0], yVekTum[2,0], 'o-', color='r')
plt.plot(yVekTum[0,:], yVekTum[2,:], color='r', label= 'Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
plt.close()
```

## Problem 7

Üç cisim problemini `scipy.integrate.solve_ivp()` fonksiyonu ile çözünüz. Animasyonunu yaratınız.

$$
\frac{d^{2}r_{i}}{dt^{2}}=G\sum_{j\neq i}m_{j}\frac{(r_{j}-r_{i})}{|r_{j}-r_{i}|^{3}} , i=1,2,3$
$$

Burada $r_{i}$, $i$'nci parçacığın konum vektörü olup kartezyen koordinatlarda iki bileşenlidir, $r_{i}\equiv r_{i}(x,y)$. Başlangıç koşulları ve sabitleri aşağıdaki gibi alınız. Burada $v_{i}\equiv \frac{dr_{i}}{dt}$ şeklindedir.

- $G=1$ Nm$^{2}$/kg$^{2}$,
- Zaman aralığı $t=0-10$ s arasında 1000 adımda.

**Figure-8** stabil çözümü:

- $m_{1}=1$, $m_{2}=1$, $m_{3}=1$ kg
- $r_{1}=(-0.97000436, 0.24308753)$ m,
- $r_{2}=(-0.97000436, 0.24308753)$ m,
- $r_{3}=(0, 0)$, m,
- $v_{1}=(0.466203685, 0.43236573)$ m/s,
- $v_{2}=(0.466203685, 0.43236573)$ m/s,
- $v_{3}=(-0.93240737, -0.86473146)$ m/s.

### Çözüm

```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Sabitler
G=1
m1= m2= m3= 1

# Denklemin sağ tarafı
def fonk(t,y):
    # Konum vektörleri y değişkeninin ilk iki elemanı
    # hızlar da konumdan sonraki elemanlar olsun.
    # yani y arrayi şöyle olacak:
    # y= [r1_x, r1_y, r2_x, r2_y, r3_x, r3_y, \
    #     v1_x, v1_y, v2_x, v2_y, v3_x, v3_y]
    
    # Konumlar
    r1= y[0:2]
    r2= y[2:4]
    r3= y[4:6]

    # Hızlar
    v1= y[6:8]
    v2= y[8:10]
    v3= y[10:12]

    # Payda kısmı
    # Norm fonksiyonu |r2-r1| anlamına gelir. İki boyutlu vektörün normu
    # |r2-r1|= sqrt((r2_x-r1_x)^2 + (r2_y-r1_y)^2) şeklindedir.
    r12= np.linalg.norm(r2-r1)
    r13= np.linalg.norm(r3-r1)
    r23= np.linalg.norm(r3-r2)

    # Denklemin sağ tarafı
    # Hızlar
    dr1dt = v1
    dr2dt = v2
    dr3dt = v3

    # r1'nin ivmesi
    dv1dt = G * m2 * (r2 - r1) / r12**3 + G * m3 * (r3 - r1) / r13**3
    dv2dt = G * m1 * (r1 - r2) / r12**3 + G * m3 * (r3 - r2) / r23**3
    dv3dt = G * m1 * (r1 - r3) / r13**3 + G * m2 * (r2 - r3) / r23**3

    # Tüm sonuçları birleştir.
    # np.concatenate(), boyutları birden fazla olan dizileri birleştirmek için kullanılır.
    return np.concatenate([dr1dt, dr2dt, dr3dt, dv1dt, dv2dt, dv3dt])

# Başlangıç koşulları
#! Figür-8
r1_0 = np.array([0.97000436, -0.24308753])
r2_0 = np.array([-0.97000436, 0.24308753])
r3_0 = np.array([0.0, 0.0])
v1_0 = np.array([0.466203685, 0.43236573])
v2_0 = np.array([0.466203685, 0.43236573])
v3_0 = np.array([-0.93240737, -0.86473146])

# Başlangıç koşullarını birleştir
y0 = np.concatenate([r1_0, r2_0, r3_0, v1_0, v2_0, v3_0])

# Zaman aralığı
t0= 0
tSon= 10
tTum= np.linspace(t0, tSon, 1000)

# Çöz
cozum= solve_ivp(fonk, (t0, tSon), y0, t_eval= tTum, method= 'RK45')

# Çözüm
r1_cozum= cozum.y[0:2].T
r2_cozum= cozum.y[2:4].T
r3_cozum= cozum.y[4:6].T

# Animasyon:
fig, ax = plt.subplots(figsize=(8, 8))

# x ve y eksenlerinin sınırlarını belirle
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Baslangicta hicbir sey yok
cizgi1, = ax.plot([], [], 'b-', label='Cisim 1')
cizgi2, = ax.plot([], [], 'g-', label='Cisim 2')
cizgi3, = ax.plot([], [], 'r-', label='Cisim 3')
nokta1, = ax.plot([], [], 'bo')
nokta2, = ax.plot([], [], 'go')
nokta3, = ax.plot([], [], 'ro')

zamanTaslagi = 'Zaman = {:.1f}'
zamanYazisi = ax.text(0.05, 0.95, '', transform=ax.transAxes)

# Baslangıc verisini fonksiyon olarak ver
def baslangic():
    cizgi1.set_data([], [])
    cizgi2.set_data([], [])
    cizgi3.set_data([], [])
    
    nokta1.set_data([], [])
    nokta2.set_data([], [])
    nokta3.set_data([], [])

    zamanYazisi.set_text('')

    return cizgi1, cizgi2, cizgi3, nokta1, nokta2, nokta3

# Her nokta için yenileme fonksiyonu
def yenile(frame):
    cizgi1.set_data([r1_cozum[:frame, 0]], [r1_cozum[:frame, 1]])
    cizgi2.set_data([r2_cozum[:frame, 0]], [r2_cozum[:frame, 1]])
    cizgi3.set_data([r3_cozum[:frame, 0]], [r3_cozum[:frame, 1]])

    nokta1.set_data([r1_cozum[frame, 0]], [r1_cozum[frame, 1]])
    nokta2.set_data([r2_cozum[frame, 0]], [r2_cozum[frame, 1]])
    nokta3.set_data([r3_cozum[frame, 0]], [r3_cozum[frame, 1]])

    zamanYazisi.set_text(zamanTaslagi.format(tTum[frame]))
    return cizgi1, cizgi2, cizgi3, nokta1, nokta2, nokta3, zamanYazisi

# Animasyon
animasyon= animation.FuncAnimation(fig, yenile, frames= len(tTum), init_func= baslangic, blit= True, interval=25)

# Goster
plt.legend()
plt.show()
```
