---
title: "Olasılık Kütle Fonksiyonu - Problem Cevapları"
---

## Problem 1

1 ile 10 arasında rastgele 100 sayı üretin.

1. Bu sayıların histogram grafiğini çizdirin.
2. Bu sayıların frekanslarını ekrana yazdırın.
3. Bu sayıları normalize edin ve ekrana yazdırın.
4. Bu sayıların olasılık kütle grafiğini çizdirin.

### Çözüm

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sayilar= np.random.randint(1,10,100)
#1
plt.hist(sayilar, bins=9, color='red')
plt.show()
plt.close()
#2
seriPd = pd.Series(sayilar)
print("Frekanslar\n", seriPd.value_counts())
#3
seriPd_norm= seriPd.value_counts(normalize=True)
# seriPd_norm= seriPd.value_counts()/len(seriPd)
print("Normalize edilmiş\n", seriPd_norm)
#4
seriPd_norm.plot.bar(color='black')
```

## Problem 2

Bir zar atıldığında beklenen değer ne olur? Matematiksel olarak hesaplayınız (Bilgisayarda değil).

### Çözüm

$E[X] = 1 \times 1/6 + 2 \times 1/6 + 3 \times 1/6 + 4 \times 1/6 + 5 \times 1/6 + 6 \times 1/6 = 3.5$

## Problem 3

1. 2 zar atıldığında zarların toplamının beklenen değerini, varyansını ve standart sapmasını teorik olarak hesaplayan betik dosyası yazın.
2. 2 zarı atın ve zarların toplamını kaydedin. Bu işlemi 3600 kere yapın.
   1. Toplam kaç kere "2,3,4,5,6,7,8,9,10,11,12" geldiğini gösteren histogramı aynı grafikte çizdirin.
   2. Olasılık kütle fonksiyonunu çizdirin. (y eksenini 1'e normalize edin. Bunun için `np.array(np.unique(toplamGelme, return_counts=True))` fonksiyonunu kullanıp hangi sayıdan kaç adet geldiği bilgisini alabilirsiniz.) Bir önceki sorudan olması gereken olasılık kütle fonksiyonu değerlerini de bu grafikte gösteriniz. _Bonus: Bu işlemleri `pandas` paketini kullanarak yapınız._
   3. Beklenen değerini, varyansı ve standart sapmasını, üstte bulduğunuz deney sonuçlarını ile bulduğunuz olasılık kütle fonksiyonunu kullanarak hesaplayın. Bu değerler ile teorik değerler ile karşılaştırın.

### Çözüm

```python
import numpy as np

olasilikKutleFonk= [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

beklenenDeger = 0
varyans= 0
#for i in range(2,13):
#    beklenenDeger += i * olasilikKutleFonk[i-2]

zar= [2,3,4,5,6,7,8,9,10,11,12]
for i in range(len(zar)):
    beklenenDeger += zar[i]*olasilikKutleFonk[i]

for i in range(2,13):
    varyans += (i - beklenenDeger)**2 * olasilikKutleFonk[i-2]

print(f"Beklenen Değer: {beklenenDeger:.2f}")
print(f"Varyans: {varyans:.2f}")
print(f"Standart Sapma: {np.sqrt(varyans):.2f}")

atisSayisi= 3600

toplamGelme= np.array([])

for it in range(atisSayisi):
    zar1 = np.random.randint(1,7) # 3 | 1
    zar2= np.random.randint(1,7) # 4 | 2
    toplamGelme= np.append(toplamGelme, zar1 + zar2) # toplamGelme => [] -> [7,3]

fig, ax = plt.subplots(figsize=(10,5))
plt.title("İki Zarın Toplamının Histogram Grafiği")
plt.hist(toplamGelme, color="black", bins=21)
plt.xticks([2,3,4,5,6,7,8,9,10,11,12])
plt.show()
plt.close()

# Olasılık kütle Fonksiyonu hesapla
toplamGelme_pmf = np.array(np.unique(toplamGelme, return_counts=True))
# toplamGelme_pmf[0] = [2,3,4,5,6,7,8,9,10,11,12]
# topalGelme_pmf[1] = [2'nin gelme miktarı, 3'ün gelme miktarı, ...]

# Pandas
#temp= pd.Series(toplamGelme)
#toplamGelme_pmf= temp.value_counts()

toplamGelme_pmf[1]= toplamGelme_pmf[1]/ atisSayisi
# topalGelme_pmf[1] = [2'nin gelme olasılığı, 3'ün gelme olasılığı, ...] <- olasılık kütle fonksiyonu

fig, ax = plt.subplots(figsize=(10,5))
plt.title("İki Zarın Toplam Gelme Sayısı Olasılık Kütle Fonksiyonu")
plt.bar(toplamGelme_pmf[0], toplamGelme_pmf[1], color="red")
plt.scatter(toplamGelme_pmf[0], [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]\
            , color="black")
plt.xticks([2,3,4,5,6,7,8,9,10,11,12])

plt.show()
plt.close()

# Beklenen değer
beklenenDeger_deney = 0
varyans_deney= 0

for it in range(len(toplamGelme_pmf[0])): # [2,3,4,5,6,7,8,9,10,11,12]
    # beklenenDeger_deney += zarların toplamı    * "deneysel" pmf
    beklenenDeger_deney   += toplamGelme_pmf[0,it] * toplamGelme_pmf[1,it]

for it in range(len(toplamGelme_pmf[0])):
    varyans_deney += (toplamGelme_pmf[0,it] - beklenenDeger_deney)**2 * toplamGelme_pmf[1,it]

print(f"Teorik Beklenen değer: {beklenenDeger:.2f}")
print(f"Deney  Beklenen değer: {beklenenDeger_deney:.2f}")
print("")
print(f"Teorik Varyans: {varyans:.2f}")
print(f"Deney  Varyans: {varyans_deney:.2f}")
print("")
print(f"Teorik Standart Sapma: {np.sqrt(varyans):.2f}")
print(f"Deney  Standart Sapma: {np.sqrt(varyans_deney):.2f}")
```
