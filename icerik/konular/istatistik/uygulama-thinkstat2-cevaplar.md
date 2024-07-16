---
title: "Uygulama - thinkstat2 - Problem Cevapları"
---

## Problem 1

Yeni doğan sağlıklı bebeklerin ağırlıklarının (pounds biriminde, `birthwgt_lb`) dağılımını inceledik. Aşağıdaki işlemleri yapın ve ilgili soruları cevaplayın.

1. Aynı işlemi doğumun ounce kısmı için yapın (`birthwgt_oz` değişkeni ile.) Bu kısımı virgülden sonraki kısım olarak düşünebilirsiniz.
   1. Dağılım için beklentiniz (estimation) nedir? Neden?
   1. Bazı değerlerin frekansı neden daha fazla?
2. Aynı işlemi kilogram biriminde yapın (dönüşüm yaparak değişkeni ile.)
3. Doğum yapan annelerin yaşlarını, yani `agepreg` değişkeni ile elde ettiğiniz dağılımı çizdirin.
   1. Dağılım tipi nedir?
   2. Atadığınız değişkenin tipini `type()` ekrana yazdırın.
   3. Bu dağılımın modu nedir?
   4. Bu dağılımın medyanı nedir?
   5. Bu dağılım simetrik mi?
   6. En genç ve en yaşlı annelerin yaşları nedir?
4. Doğum sürelerini, yani `prglngth` değişkeni ile elde ettiğiniz dağılımı çizdirin.
   1. Dağılım tipi nedir?
   2. Bu dağılımın modu nedir?
   3. Bu dağılımın medyanı nedir?
   4. En uzun ve en kısa doğum süreleri nedir?
   5. 21 haftadan küçük değerleri ve 45 haftadan büyük değerleri aykırı değer olarak kabul edin. Bu aykırı değerlerin sayısı nedir? 
   6. Aykırı değerlerin toplam veriye oranı nedir?
   7. Sadece aykırı değerleri çizdirin.

### Çözüm

```python
# ============================
# thinkStats2 ile ilgili modülleri içeri aktarmak için gereken kod
from sys import path 
from os import getcwd, pardir
from os.path import join, abspath
PWD = getcwd()
# Insert modules path
path.insert(0, join(PWD, "thinkStats2"))
# ============================

# ============================
# thinksStats2 dizini
thinkStats_dir= join(PWD, "thinkStats2")
# ============================

# ============================
# Verilerin olduğu dizin
# 3 üst dizine çık
veri_dir = join(abspath(join(\
    PWD, pardir, pardir, pardir))\
        , 'veri')
# ============================

import nsfg
import thinkplot
import thinkstats2
# Oku
preg= nsfg.ReadFemPreg(dct_file=join(veri_dir,\
    'veri_thinkStats2_2002FemPreg.dct'),\
    dat_file=join(veri_dir,\
        'veri_thinkStats2_2002FemPreg.dat.gz'))
# Sağlıklı doğumları seç
live= preg[preg.outcome==1]

# 1.
# Histogram oluştur
hist = thinkstats2.Hist(live.birthwgt_lb, label='Ağırlık (oz)')
# Histogramı çiz
thinkplot.Hist(hist)
thinkplot.Show(xlabel='Ounce', ylabel='Frekans')
thinkplot.Clf()
# Sorular
print(f"1.1.) Ağırlığın virgülden sonraki kısmının rastgele olmasını beklerim. Bundan dolayı dağılımın düzgün (uniform) olmasını beklerim.")
print(f"1.2.) 0'ın frekansı daha fazla çıktı. Bunun muhtemel sebebi, bazı bebeklerin kiloları yuvarlanarak kayıt altına alınmış olabilir.")
print("-"*40)

# 2.
# Histogram oluştur
hist = thinkstats2.Hist(live.birthwgt_lb*0.45 , label='Ağırlık (kg)')
# Histogramı çiz
thinkplot.Hist(hist)
thinkplot.Show(xlabel='kg', ylabel='Frekans')
print("-"*40)

# 3.
# Histogram oluştur
hist = thinkstats2.Hist(live.agepreg , label='Kadınların Hamilelik Yaşı')
# Histogramı çiz
thinkplot.Hist(hist)
thinkplot.Show(xlabel='yıl', ylabel='Frekans')
# Sorular
print(f"3.1) Normal dağılım.")
print(f"3.2) Değişkenin tipi: {type(live.agepreg)}")
print(f"3.3) Dağılımın modu: {live.agepreg.value_counts().index[0]}")
print(f"3.4) Dağılımın medyanı: {live.agepreg.median()}")
print(f"3.5) Dağılımın simetrik olması için ilk bakılan özellik modu ile medyanın aynı almasıdır. Burada mod ile medyan aynı değildir.")
# https://www.geeksforgeeks.org/python-pandas-dataframe-skew/
print(f"3.6) En genç anne: {live.agepreg.min()} ve en yaşlı anne: {live.agepreg.max()} yaşındadır.")
print("-"*40)

# 4.
# Histogram oluştur
hist = thinkstats2.Hist(live.prglngth , label='Kadınların Hamilelik Süresi')
# Histogramı çiz
thinkplot.Hist(hist)
thinkplot.Show(xlabel='hafta', ylabel='Frekans')
# Sorular
print(f"4.1) Normal dağılım.")
print(f"4.2) Dağılımın modu: {live.prglngth.value_counts().index[0]}")
print(f"4.3) Dağılımın medyanı: {live.prglngth.median()}")
print(f"4.4) En kısa doğum süresi {live.prglngth.min()} hafta ve en uzun doğum süresi {live.prglngth.max()} haftadır.")
# 4.5
aykiriDegerler= live.prglngth[(live.prglngth < 21) | (live.prglngth > 45)]
#aykiriDegerler= live.prglngth[live.prglngth > 21 | live.prglngth < 45]
#aykiriDegerler= live.prglngth[(live.prglngth > 21) or (live.prglngth < 45)]
#aykiriDegerler= live.prglngth[live.prglngth > 21 | live.prglngth < 45]
print(f"4.5) Aykırı değerlerin sayısı {aykiriDegerler.size}")
print(f"4.6) Aykırı değerlerin toplam veriye oranı %{aykiriDegerler.size/live.prglngth.size}")
# 4.7
aykiriDegerler_ayiklamis= live.prglngth[(live.prglngth > 21) & (live.prglngth < 45)]
# Histogram oluştur
hist = thinkstats2.Hist(aykiriDegerler_ayiklamis , label='Kadınların Hamilelik Süresi (Aykırı Değerler Ayıklanmış)')
# Histogramı çiz
thinkplot.Hist(hist)
thinkplot.Show(xlabel='hafta', ylabel='Frekans')
```