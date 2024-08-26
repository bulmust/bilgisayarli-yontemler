---
title: "scipy - stats - Problem Cevapları"
---
## Problem 1

- Yakın bir galakside süpernova meydana geldiğini düşünün. Bu süpernovadan Dünya'ya nötrino parçacıkları gelecektir.
- Nötrinolar, kütleli (neredeyse sıfır) ve spin 1/2 parçacıklardır.
- Dünya'daki nötrino gözlem evleri süpernovadan gelen nötrinoları enerjilerine göre gözlemlemiştir. Bu gözlemler `neutrinoCount.csv` dosyasında verilmiştir. Bu dosyayı indirmek için [tıklayınız](../../../veri/veri_neutrinoCount.csv).
- Bu dosyadaki ilk sütun gelen nötrinoların enerjileri, ikinci sütun ise bu enerjilerdeki nötrinoların sayısıdır.

1. Nötrinolar hangi istatistiksel dağılımı takip eder?
2. `neutrinoCount.csv` dosyasını okuyun.
3. Nötrinoların ortalama enerjisini ve standart sapmasını bulun.
4. `neutrinoCount.csv` dosyasındaki veri normalize midir? Değil ise normalize edin.
5. Gelen nötrinoların enerjiye göre sayılarının grafiğini çizdirin.
6. Gelen nötrino sayılarını 1'e normalize edin.
7. Aşağıdaki normalize edilmiş Fermi-Dirac dağılımını kullanarak nötrinoların sıcaklığını $2-10$ MeV arasında arayın.

$$f(E) = \frac{1}{1.803 T^{3}} \frac{E^{2}}{1+\exp(E/T)}$$

### Çözüm

```python
################################################
import os
# Bu dosyanın bulunduğu dizini al
current_dir = os.path.abspath('')
# 3 üst dizine çık
veri_dir = os.path.join(\
    os.path.abspath(\
        os.path.join(\
    current_dir, os.pardir, os.pardir, os.pardir))\
        , 'veri')
################################################

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def fd_dist(E_MeV, T_MeV):
    return (1/ (1.803* (T_MeV**3)))* (E_MeV**2) / (1 + np.exp(E_MeV/ T_MeV))

seri1= pd.read_csv(veri_dir+"/veri_neutrinoCount.csv", index_col="Energy_MeV")
print(f"Ortalama neutrino enerjisi [MeV] = {seri1.mean().iloc[0]}")
print(f"Standart sapma [MeV] = {seri1.std().iloc[0]}")

seri1= seri1/ np.sum(seri1.values[:,0])
plt.plot(seri1.index.values, seri1.values[:,0], color="red", marker="o")
plt.show()
plt.close()

plt.plot(seri1.index, seri1.values[:,0], color="red", marker="o")
for it in range(2, 10):
    plt.plot(seri1.index, fd_dist(seri1.index, T_MeV=it), label=f"T={it} MeV")
    
plt.legend()
plt.show()

#E_MeV= np.linspace(1, 50, 50)
#T_MeV= 4

#dist= 500* (1/ (1.803* (T_MeV**3)))* (E_MeV**2) / (1 + np.exp(E_MeV/ T_MeV))
# Convert dist to integer
#dist= dist + np.random.uniform(0, 1, len(dist))
#dist= np.round(dist, 0)
#print(dist)
#seri1= pd.Series(dist, index=E_MeV)
#print(seri1)
#seri1.to_csv("neutrinoCount.csv", header=["Count"], index_label="Energy_MeV")
#seri1= pd.read_csv("neutrinoCount.csv", index_col="Energy_MeV")

#plt.plot(seri1.index, seri1)
# Normalize the seri1 distribution
```

## Problem 2

1. Standart sapması 5 olan ve ortalaması 35 olan bir normal dağılıma sahip 1000 elemanlı bir dizi oluşturun. `scipy.stats.norm`.
2. Bu dizinin histogramını çizdirin. Histogramı çizmeden önce ürettiğiniz objeye rastgele sayılar atamanız gerekecektir. Bunun için `rvs(10000)` komutunu kullanabilirsiniz. Bin sayısını 100 alabilirsiniz.
3. Bu dizinin beklenen değerini ekrana yazdırın.
4. Bu dizinin varyansını ekrana yazdırın.
5. Bu dizinin standart sapmasını ekrana yazdırın.
6. $40$'ın gelme olasılığını bulun.

### Çözüm

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Create a normal distribution with mean= 35 and std= 5
normal_dist= stats.norm(35,5)

# Plot histogram of normal distribution
plt.hist(normal_dist.rvs(10000), bins=100)
plt.show()
plt.close()

# Expected value of normal distribution
print(f"Ortalama: {normal_dist.mean()}")

# Variance of normal distribution
print(f"Varyans: {normal_dist.var()}")

# Standard deviation of normal distribution
print(f"Standart Sapma: {normal_dist.std()}")

# Find values in 0.01 and 0.99 quantiles
x_lim= normal_dist.interval(0.99)
x_val= np.linspace(*x_lim, 1000)

# Plot PDF of normal distribution
#plt.plot(x_val, normal_dist.pdf(x_val))
#plt.ylabel("PDF")
#plt.show()
#plt.close()

# Plot CDF of normal distribution
#plt.plot(x_val, normal_dist.cdf(x_val))
#plt.ylabel("CDF")
#plt.show()
#plt.close()

# Find the probability of x= 40
print(f" 40 sayısının gelme olasılığı: {normal_dist.pdf(40)}")
```