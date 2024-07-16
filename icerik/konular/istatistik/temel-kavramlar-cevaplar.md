---
title: "İstatistik - Giris - Problem Cevapları"
---

## Problem 1

100 adet parayı 1000 kere atan ve `np.random.rand()` fonksiyonu kullanan bir betik dosyası yazın. Her atıldığında 100 tane paranın kaç tanesi tura geldiğini kaydedin ve sonucu histogram grafiği olarak çizdirin. 

### Çözüm

```python
import matplotlib.pyplot as plt
import numpy as np
#import random

sonuc = []

for i in range(1000):
    say_tura = 0
    for j in range(100):
        #if random.random() < 0.5:
        if np.random.rand() < 0.5:
            say_tura += 1
    sonuc.append(say_tura)

plt.hist(sonuc, bins=range(101))
plt.title("100 adet paranın 1000 kere atılması sonucunda tura gelme sayısı")
plt.xlabel("Tura gelme sayısı")
plt.ylabel("Frekans")
plt.show()
```

## Problem 2

Problem 1'de verilen betik dosyasını `np.random.choice()` fonksiyonu kullanarak yapın.

### Çözüm

```python
import numpy as np
import matplotlib.pyplot as plt

toplamTuraSaiyi= np.zeros(1000)
for it in range(1000):
    # 100 tane rastgele -1 ve 1 değeri üret
    paraAtma= np.random.choice([0,1], size=100)
    
    # Tüm Değerleri topla. 1'ler sanki tura gelmiş gibi düşünülebilir.
    toplamTuraSaiyi[it] = np.sum(paraAtma)
    
plt.hist(toplamTuraSaiyi, bins=range(101))
plt.show()
```

## Problem 3

100 adet zarı 1000 kere atan ve `np.random.choice()` fonksiyonunu kullanan bir betik dosyası yazın. Her atıldığında 100 tane zarın kaç tanesinin 6 geldiğini, kaç tanesinin 5 geldiğini vs. kaydedin ve sonucu histogram grafiği olarak çizdirin.

### Çözüm
```python
import numpy as np
import matplotlib.pyplot as plt

toplamTuraSaiyi= np.zeros((6,1000))
for it in range(1000):
    for it2 in range(100):
        # 100 tane rastgele -1 ve 1 değeri üret
        paraAtma= np.random.choice([0,1,2,3,4,5])

        # 1 Gelenler
        if paraAtma == 0:
            toplamTuraSaiyi[0,it] = toplamTuraSaiyi[0,it]+ 1
        # 2 Gelenler
        elif paraAtma==1:
            toplamTuraSaiyi[1,it] = toplamTuraSaiyi[1,it]+ 1
        # 3 Gelenler
        elif paraAtma==2:
            toplamTuraSaiyi[2,it] = toplamTuraSaiyi[2,it]+ 1
        # 4 Gelenler
        elif paraAtma==3:
            toplamTuraSaiyi[3,it] = toplamTuraSaiyi[3,it]+ 1
        # 5 Gelenler
        elif paraAtma==4:
            toplamTuraSaiyi[4,it] = toplamTuraSaiyi[4,it]+ 1
        # 6 Gelenler
        elif paraAtma==5:
            toplamTuraSaiyi[5,it] = toplamTuraSaiyi[5,it]+ 1        
# Çiz
plt.hist(toplamTuraSaiyi[0], bins=range(101), color='red', label="1", alpha=0.5)
plt.hist(toplamTuraSaiyi[1], bins=range(101), color='blue', label="2", alpha=0.5)
plt.hist(toplamTuraSaiyi[2], bins=range(101), color='green', label="3", alpha=0.5)
plt.hist(toplamTuraSaiyi[3], bins=range(101), color='yellow', label="4", alpha=0.5)
plt.hist(toplamTuraSaiyi[4], bins=range(101), color='orange', label="5", alpha=0.5)
plt.hist(toplamTuraSaiyi[5], bins=range(101), color='purple', label="6", alpha=0.5)
plt.vlines(100/6, 0, 130, color='black', label="1/6", lw=3)
plt.xlim([0,40])
plt.legend()
plt.show()
```

## Problem 4

Aşağıdaki linkte bulunan excel dosyasını indirin. 

[Standart Solar Spectrumu Linki](https://www.pveducation.org/sites/default/files/PVCDROM/Appendices/AM0AM1_5.xls)

- Bu excel dosyasındaki verileri temizleyin.
  - Başlıkları sadece `Wavelength (nm)`, `Extraterrestrial W*m-2*nm-1`, `Global tilt  W*m-2*nm-1`, `Direct+circumsolar W*m-2*nm-1` kalsın.
  - Tüm diğer verileri silin.
  - Tüm tablar (sheets) silin.
  - Tüm veriyi `float` tipine çevirin.
- Temizlediğiniz veriyi okuyun ve `Wavelength (nm)` sütununu x ekseni olacak şekilde tüm kolonların grafiklerini aynı figürde çizdirin.
- `Extraterrestrial W*m-2*nm-1` en yüksek değerini bulun.
- En yüksek değerin kaç Kelvin olduğunu bulun. ([Wien's Öteleme Kanunu](https://en.wikipedia.org/wiki/Wien%27s_displacement_law))
- En yüksek değerin kaç Celsius olduğunu bulun.
- Görünür ışığın spektrumunu yukarıda çizdiğiniz grafikte gösterin.

Kaynak: [Solar Spectrum](https://www.pveducation.org/pvcdrom/appendices/standard-solar-spectra)

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

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Oku
df= pd.read_excel(veri_dir+ "/veri_AM0AM1_5.xls")
# Kolon isimlerini sil
df.columns= ["" for x in range(df.columns.shape[0])]
# İlk Satırı kolon isimleri olarak ata
df.columns= df.loc[0]
# İlk satırı sil
df.drop(0, inplace=True)
# 4-6 Kolonlarını sil
df= df.iloc[:,:4]
# 1. Kolonu index olarak ata
df.set_index("Wavelength (nm)", inplace=True)
#df.head()
#df.info()
# Çiz
df.plot(kind="line")
# Tiplerin float olmasını sağla
df= df.astype(float)
#df.info()
# [Extraterrestrial W*m-2*nm-1] Maksimum değerini bul
valMax = df["Extraterrestrial W*m-2*nm-1"].max()
argMax = df["Extraterrestrial W*m-2*nm-1"].argmax()
waveMax_nm = df["Extraterrestrial W*m-2*nm-1"].index[argMax]
waveMax_mum = waveMax_nm/1000
print(f"Max parlaklık [ W*m^(-2)*nm^(-1) ]     = {valMax}")
print(f"Max parlaklığa sahip dalga boyu [ nm ] = {waveMax_nm}")
print(f"Max parlaklığa sahip dalga boyu [ \mu m ] = {waveMax_mum}")

# Find temperature using Wien's displacement law
# https://en.wikipedia.org/wiki/Wien%27s_displacement_law

T = 2898/waveMax_mum # [K]
print(f"Gunesin Sicakligi [K] = {T}")

# Bu sıcaklık hangi dalga boyuna karşılık geliyor
#print(df["Extraterrestrial W*m-2*nm-1"].info())
maxExtraterrestrial_index= df["Extraterrestrial W*m-2*nm-1"].idxmax()

# Bu dalga boyu hangi renge denk geliyor?
if maxExtraterrestrial_index >= 380 and maxExtraterrestrial_index < 450:
    print(f"{maxExtraterrestrial_index} nm dalgaboyu: Mor")
elif maxExtraterrestrial_index >= 450 and maxExtraterrestrial_index < 485:
    print(f"{maxExtraterrestrial_index} nm dalgaboyu: Mavi")
elif maxExtraterrestrial_index >= 485 and maxExtraterrestrial_index < 500:
    print(f"{maxExtraterrestrial_index} nm dalgaboyu: Cyan")
elif maxExtraterrestrial_index >= 500 and maxExtraterrestrial_index < 565:
    print(f"{maxExtraterrestrial_index} nm dalgaboyu: Yeşil")
elif maxExtraterrestrial_index >= 565 and maxExtraterrestrial_index < 590:
    print(f"{maxExtraterrestrial_index} nm dalgaboyu: Sarı")
elif maxExtraterrestrial_index >= 590 and maxExtraterrestrial_index < 625:
    print(f"{maxExtraterrestrial_index} nm dalgaboyu: Turuncu")
elif maxExtraterrestrial_index >= 625 and maxExtraterrestrial_index < 750:
    print(f"{maxExtraterrestrial_index} nm dalgaboyu: Kırmızı")
else:
    print(f"{maxExtraterrestrial_index} nm dalgaboyu: GÖRÜNÜR SPECTRUM DIŞINDA")
#df.describe()
# Daha güzel çiz (ÇALIŞMIYOR)
# tumRenkler_Dalgaboyunm= {"mor": [380, 444.99],
#                          "mavi": [445, 484.99],
#                          "cyan": [485, 499.99],
#                          "yesil": [500, 564.99],
#                          "sari": [565, 589.99],
#                          "turuncu": [590, 624.99],
#                          "kirmizi": [625, 750]}
# # The closest indices where tumRenkler_Dalgaboyunm is in df.index
# tumRenkler_karsiliklari= {}
# for isim, degerler in tumRenkler_Dalgaboyunm.items():
#     degerTemp= []
#     for it in range(2):
#         degerTemp.append(np.abs(df.index - degerler[it]).argmin())
#     tumRenkler_karsiliklari[isim]= degerTemp
# mor_min=tumRenkler_karsiliklari["mor"][0]
# mavi_min=tumRenkler_karsiliklari["mavi"][0]
# cyan_min=tumRenkler_karsiliklari["cyan"][0]
# yesil_min=tumRenkler_karsiliklari["yesil"][0]
# sari_min=tumRenkler_karsiliklari["sari"][0]
# turuncu_min=tumRenkler_karsiliklari["turuncu"][0]
# kirmizi_min=tumRenkler_karsiliklari["kirmizi"][0]

# mor_max=tumRenkler_karsiliklari["mor"][1]
# mavi_max=tumRenkler_karsiliklari["mavi"][1]
# cyan_max=tumRenkler_karsiliklari["cyan"][1]
# yesil_max=tumRenkler_karsiliklari["yesil"][1]
# sari_max=tumRenkler_karsiliklari["sari"][1]
# turuncu_max=tumRenkler_karsiliklari["turuncu"][1]
# kirmizi_max=tumRenkler_karsiliklari["kirmizi"][1]

# zeros_mor=np.zeros(mor_max-mor_min, dtype=float)
# zeros_mavi=np.zeros(mavi_max-mavi_min)
# zeros_cyan=np.zeros(cyan_max-cyan_min)
# zeros_yesil=np.zeros(yesil_max-yesil_min)
# zeros_sari=np.zeros(sari_max-sari_min)
# zeros_turuncu=np.zeros(turuncu_max-turuncu_min)
# zeros_kirmizi=np.zeros(kirmizi_max-kirmizi_min)
    
# fig, ax = plt.subplots()
# df["Extraterrestrial W*m-2*nm-1"].plot(kind="line", color='black', lw=3)

# x= df.index.to_numpy()
# y=df["Extraterrestrial W*m-2*nm-1"].to_numpy()
# print(y.dtype)

# ax.fill_between(x[mor_min:mor_max], y[mor_min:mor_max], zeros_mor, color='m')
# ax.fill_between(x[mavi_min:mavi_max], y[mavi_min:mavi_max], zeros_mavi,color='b')
# ax.fill_between(x[cyan_min:cyan_max], y[cyan_min:cyan_max], zeros_cyan,color='c')
# ax.fill_between(x[yesil_min:yesil_max], y[yesil_min:yesil_max], zeros_yesil,color='g')
# ax.fill_between(x[sari_min:sari_max], y[sari_min:sari_max], zeros_sari,color='y')
# ax.fill_between(x[turuncu_min:turuncu_max], y[turuncu_min:turuncu_max], zeros_turuncu,color='orange')
# ax.fill_between(x[kirmizi_min:kirmizi_max], y[kirmizi_min:kirmizi_max], zeros_kirmizi,color='r')

# plt.xlim([x[mor_min]-250,x[kirmizi_max]+250])
# plt.show()
```

## Problem 5

1. 600 adet parayı 1000 kere atan bir algoritma oluşturun. 600 adet parnın kaçı tura geldiğini hesaplasın. Bunu 1000 kere yapacak şekilde mofiye edin. 600 tane para atıldığında kaç tanesinin tura geldiğini gösteren bir histogram çizdirin.
2. Aynı işlemi bu sefer bir zaın 3 gelmesi için yapın. Yani, 600 adet zarı 1000 kere attığınızda, 600 zarın kaç defa 3 geldiğini hesaplayan bir program yazın. 600 tane zar atıldığında kaç tanesinin 3 geldiğini gösteren bir histogram çizdirin.
3. 600 adet zarı ve 600 adet parayı aynı anda yani beraber 1000 kere atıldığında, kaçında 3 ve tura geldiğini hesaplayan bir program yazın. 600 tane para ve zar atıldığında kaç tanesi 3 **ve** tura geldiğini gösteren bir histogram çizdirin.

- **Not**: 2. sorunun verisini kullanabilirsiniz.
- **İpucu**: Dağılımının $600\times(1/2)\times(1/6)=50$ etrafında olması beklenir.

4. Aşağıdaki adımları yapın.
   1. 1200 adet (birinci zarı 600 kere ikinci zarı 600 kere düşünün) zarı 1000 kere atıp, ikili toplamları kaç kere 7 geldiğini ve kaç kere 12 geldiğini hesaplayan bir program yazın. 1200 tane zar atıldığında ikili toplamları kaç kere 7 ve kaç kere 12 geldiğini gösteren histogramları aynı figürde çizdirin.
   2. Toplamı 7 ve 12 gelen dağılımlar için aşağıdaki değerleri hesaplayın.
      1. Ortalama değer
      2. Mod (en çok tekrar eden değer)
      3. Standart sapma, Varyans
      4. Medyan
      5. Maksimum ve Minimum değer
   3. İki dağılım için efektif boyutu, Cohen'in d değerini hesaplayın.

- **İpucu**: Algoritmayı şöyle yazabilirsiniz. İki ayrı zarı attım ve toplamları 7 geldi. Bunu 600 kere tekrarladım ve kaydettim. Bu işlemi 1000 kere daha yaptım.
- **İpucu2**: 7'nin dağılımının $600\times(1/6)=100$ etrafında olması beklenir. (1+6, 2+5, 3+4, 4+3, 5+2, 6+1)
- **İpucu3**: 12'nin dağılımının $600\times(1/36)=16.7$ etrafında olması beklenir.
- **İpucu4**: 

$$
d = \frac{\overline{x}_1 - \overline{x}_2}{s_{havuz}}
$$

$$
s_{havuz}= \sqrt{\frac{n_1s_1^2 + n_2s_2^2}{n_1 + n_2}}
$$

### Çözüm

```python
import numpy as np
import matplotlib.pyplot as plt

toplamTura= np.zeros(1000)
toplamUc=   np.zeros(1000)
toplamUcTura= np.zeros(1000)
toplamYedi= np.zeros(1000)
toplamOnIki= np.zeros(1000)

for it in range(1000):
    # 100 tane rastgele -1 ve 1 değeri üret
    paraAtma= np.random.choice([0,1], size=600)
    
    # Tüm Değerleri topla. 1'ler sanki tura gelmiş gibi düşünülebilir.
    toplamTura[it] = np.sum(paraAtma)
    
    for it2 in range(600):
        # 1, 2, 3, 4, 5, 6 arasından birisini seç
        zarAtma= np.random.choice([1,2,3,4,5,6])
        zarAtma2= np.random.choice([1,2,3,4,5,6])
        
        # 3 Gelenler
        if zarAtma == 3:
            toplamUc[it] = toplamUc[it]+ 1
        # 3 ve Tura Gelenler
        if paraAtma[it2] == 1 and zarAtma == 3:
            toplamUcTura[it] = toplamUcTura[it]+ 1
        # Toplamı 7 Gelenler
        if zarAtma+ zarAtma2 == 7:
            toplamYedi[it] = toplamYedi[it]+ 1
        # Toplamı 12 Gelenler
        if zarAtma+ zarAtma2 == 12:
            toplamOnIki[it]= toplamOnIki[it]+ 1

#4.2.1
print(f"\n4.2.1)\n7'nin ortalama değeri :{np.mean(toplamYedi)}\
                \n12'nin ortalama değeri:{np.mean(toplamOnIki)}")
#4.2.2
values7, counts7 = np.unique(toplamYedi, return_counts=True)
values12, counts12 = np.unique(toplamOnIki, return_counts=True)
print(f"\n4.2.2)\n7'nin modu  :{values7[np.argmax(counts7)]}\
                \n12'nin modu :{values12[np.argmax(counts12)]}")
#4.2.3
print(f"\n4.2.3)\n7'nin standart sapması ve varyansı  :{np.std(toplamYedi)}\
    , {np.var(toplamYedi)}\
    \n12'nin standart sapması ve varyansı :{np.std(toplamOnIki)}\
    , {np.var(toplamOnIki)}")
#4.2.4
print(f"\n4.2.4)\n7'nin medyanı  :{np.median(toplamYedi)}\
                \n12'nin medyanı :{np.median(toplamOnIki)}")
#4.2.6
print(f"\n2.5)\n7'nin min ve maks değeri  :{np.min(toplamYedi)}\
    , {np.max(toplamYedi)}\
    \n12'nin min ve maks değeri :{np.min(toplamOnIki)}\
    , {np.max(toplamOnIki)}")
#4.3
n1=1000
n2=1000
s1= np.std(toplamYedi)
s2= np.std(toplamOnIki)
shavuz= np.sqrt(((n1)*(s1**2)+ (n2)*(s2**2))/(n1+n2))
cohenD= (np.mean(toplamYedi)- np.mean(toplamOnIki))/shavuz
print(f"\n4.3)\nCohen D değeri :{cohenD}")

fig, axs = plt.subplots(4, figsize=(5, 10))
axs[0].hist(toplamTura, bins=25, color='g', label="Tura Gelenler")
axs[1].hist(toplamUc, bins=25, color='y', label="3 Gelenler")
axs[2].hist(toplamUcTura, bins=25, color='b', label="3 ve Tura Gelenler")
axs[3].hist(toplamYedi, bins=25, color='r', label="7 Gelenler")
axs[3].hist(toplamOnIki, bins=25, color='k', label="12 Gelenler")
for i in range(4):
    axs[i].legend()    
plt.show()
plt.close()
```
