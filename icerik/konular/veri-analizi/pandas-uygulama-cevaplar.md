---
title: "pandas - Uygulama - Problem Cevapları"
---

## Problem 1

Github sitesinde bulunan [veri_imdb_1e5rows.tsv](../../../veri/veri_imdb_1e5rows.tsv) dosyasındaki [verinin metadatasına](https://www.imdb.com/interfaces/) inceleyin. Bu veri, `title.akas.tsv.gz` adlı dosyanın ilk $10^{5}$ satırıdır. Bu veriyi `pd.read_table()` fonksiyonu ile okuyun. 

Eğer tüm veri ile çalışmak istiyorsanız (1.8 gb) [şu linkteki](https://datasets.imdbws.com/title.akas.tsv.gz) dosyayı indirin. Bu dosya sıkıştırılmış dosyadır. Bu dosyayı indirdikten sonra dışarı aktarın.

Bu veri hakkında aşağıdaki soruları cevaplayın.

1. Bu verinin sütunları nelerdir?
2. Bu verinin kaç sütunu var?
3. Bu verinin kaç satırı var?
4. Bu verinin ilk 2 satırını gösterin.
5. Bu verinin son 2 satırını gösterin.
6. Bu veri setindeki tüm biricik dilleri (`language`) gösterin.
7. Bu veri setindeki tüm biricik bölgeleri (`region`) gösterin.
8. Bu veri setindeki her bir biricik dilde kaç adet film vardır?
9. Bu veri setindeki her bir biricik bölgede kaç adet film vardır?
10. Bu veri setindeki `attributes` sütununu çıkarın (değişkene atayın).
11. Bu verideki sütunların veri tiplerini ekrana yazdırın.
12. Bu verinin `ordering` sütununu tam sayı haline getirin (değişkene atayın).
13. Bu verinin `isOriginalTitle` sütununu `bool` haline getirin (değişkene atayın).
14. Bu verinin etiketlerini `titleId` olacak şekilde gösterin (değişkene atayın).
15. Bu verinin etiketini `titleId` ve `title` olarak değiştirin (değişkene atayın).
16. Bu veriyi `titleId` sütununa göre sıralayın (değişkene atayın).
17. Bu verideki tüm `\N` değerlerini `pd.NA` değerleri ile değiştirin (değişkene atamayın).
18. Bu verinin `titleId` ve `title` etiketlerini tekrar sütun haline getirin (değişkene atayın).
19. Bu verideki `types` sütunu içerisinde olan `original` verisine sahip satırları gösterin ve sonucu `df2` değişkenine atayın.
20. Bu veride `isOriginalTitle` sütunu `True` olan satırları gösterin ve sonucu `df2` ile karşılaştırın. Yani elde ettiğiniz veri ile `df2` verisi aynı mı? Değilse hangi satırlar farklı?

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
# Oku
df= pd.read_table(veri_dir+"/veri_imdb_1e5rows.tsv")
#1. Bu verinin sütunları nelerdir?
print(f"-------------------\n1)\n {df.columns.to_numpy()}")
#2. Bu verinin kaç sütunu var?
print(f"-------------------\n2)\n {len(df.columns)}")
#3. Bu verinin kaç satırı var?
print(f"-------------------\n3)\n {len(df)+1}")
#4. Bu verinin ilk 5 satırını gösterin.
print(f"-------------------\n4)\n {df.head(2)}")
#5. Bu verinin son 5 satırını gösterin.
print(f"-------------------\n5)\n {df.tail(2)}")
#6. Bu veri setindeki tüm biricik dilleri (`language`) gösterin.
print(f"-------------------\n6)\n {df['language'].unique()}")
#7. Bu veri setindeki tüm biricik bölgeleri (`region`) gösterin.
print(f"-------------------\n7)\n {df['region'].unique()}")
#8. Bu veri setindeki her bir biricik dilde kaç adet film vardır?
print(f"-------------------\n8)\n {df['language'].value_counts()}")
#9. Bu veri setindeki her bir biricik bölgede kaç adet film vardır?
print(f"-------------------\n9)\n {df['region'].value_counts()}")
#10. Bu veri setindeki `attributes` sütununu çıkarın (değişkene atayın).
df.drop(columns=['attributes'], inplace=True)
#11. Bu verideki sütunların veri tiplerini ekrana yazdırın.
print(f"-------------------\n11)\n {df.dtypes}")
#12. Bu verinin `ordering` sütununu tam sayı haline getirin (değişkene atayın).
df["ordering"].apply(lambda x: int(x))
#13. Bu verinin `isOriginalTitle` sütununu `bool` haline getirin (değişkene atayın).
df.isOriginalTitle = df.isOriginalTitle.astype(bool)
df.dtypes
#14. Bu verinin etiketlerini `titleId` olacak şekilde gösterin (değişkene atamayın).
print(f"-------------------\n14)\n {df.set_index('titleId')}")
#15. Bu verinin etiketini `titleId` ve `title` olarak değiştirin (değişkene atayın).
df.set_index(['titleId', 'title'], inplace=True)
print(f"-------------------\n15)\n {df.head()}")
#16. Bu veriyi `titleId` sütununa göre sıralayın (değişkene atayın).
df.sort_values(by=['titleId'], inplace=True)
print(f"-------------------\n16)\n {df.head(2)}")
#17. Bu verideki tüm `\N` değerlerini `pd.Na` değerleri ile değiştirin (değişkene atamayın).
df_tmp=df.replace(r'\N', pd.NA).head(2)
print(f"-------------------\n17)\n {df_tmp}") # r"" raw string. \N alt satıra geçmesin diye.
del df_tmp
#18. Bu verinin `titleId` ve `title` etiketlerini tekrar sütun haline getirin (değişkene atayın).
df= df.reset_index()
print(f"-------------------\n18)\n {df.head(2)}")
#19. Bu verideki `types` sütunu içerisinde olan `original` verisine sahip satırları gösterin ve sonucu `df2` değişkenine atayın.
df2= df[df.types.str.contains('original')]
print(f"-------------------\n19)\n {df2.head(12)}")
# 20. Bu veride `isOriginalTitle` sütunu `True` olan satırları gösterin ve sonucu `df2` ile karşılaştırın. Yani elde ettiğiniz veri ile `df2` verisi aynı mı?  Değilse hangi satırlar farklı?
df3= df[df.isOriginalTitle==True]
print(f"-------------------\n20)\n {df3.head(12)}")
print("--------------------")
print(f"-------------------\n20)\n {df2.equals(df3)}")
print("--------------------")
print(f"Farklı olan satırlar: {pd.concat([df2,df3]).drop_duplicates(keep=False)}")
```

## Problem 2

TÜİK'in veri merkezinde bulunan "[Hava Alanlarında Toplam Yolcu ve Yük Trafiği](../../../veri/veri_HavaalanlarindaToplamYolcuVeYukTrafigi.xls)" verisini indirin. Bu veri dosyasında herhangi bir değişiklik yapmayın!

Aşağıdaki soruları cevaplayın.

1. Bu excel dosyasını okuyun ve `df` değişkenine atayın. (Not: `read_excel` fonksiyonu ile okumak için xlrd kütüphanesini kurmanız gerekebilir. `pip install xlrd` komutu ile kurabilirsiniz.)
2. Veri çerçevesini gösterin.
3. Veri çerçevesi temizleyin. Bu temizlemeyi excel dosyasını açıp değil pandas ile yapın. Bu temizlemeyi aşağıdaki grafikleri çizebilmek için yapın:
   1. Toplam Yolcu - Yıl grafiğini çizdirin. Aynı grafik üzeride iç hat yolcusu ve dış hat yolcusunun yıllara göre grafiği de olsun.
   2. Toplam Yükün (Ton), iç hat yükünün (Ton) ve dış hat yükünün (Ton) yıllara göre grafiğini çizdirin.

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
# Oku
## skiprows parametresi Tablonunu ilk satırlarını belirlitilen sayı kadar atlar.
## skipfooter paramteresi Tablonun sonunda satırları belirtilen sayı kadar atlar
df = pd.read_excel(\
    veri_dir+'/veri_HavaalanlarindaToplamYolcuVeYukTrafigi.xls'\
    ,skiprows=5, skipfooter=4\
        , usecols="A, B, C, D, F, G, H")
df.columns = ["Yıl", "Toplam Yolcu", "İç Hat Yolcu"\
    , "Dış Hat Yolcu", "Toplam Yük", "İç Hat Yük", "Dış Hat Yük"]
# Çiz
yil = df["Yıl"]
plt.plot(yil.index, df["Toplam Yolcu"], label='Toplam Yolcu')
plt.plot(yil.index, df["İç Hat Yolcu"], label='Toplam Yolcu')
plt.plot(yil.index, df["Dış Hat Yolcu"], label='Toplam Yolcu')
plt.xlabel('Yıl')
plt.ylabel('Yolcu Sayısı')
plt.title('Yıllara Göre Yolcu Sayısı')
plt.legend()
plt.show()
plt.close()
# Toplam Yolcu
toplamYolcu = df.groupby("Yıl")["Toplam Yolcu"].sum()
toplamIcHatYolcu = df.groupby("Yıl")["İç Hat Yolcu"].sum()
toplamDisHatYolcu = df.groupby("Yıl")["Dış Hat Yolcu"].sum()
# Çiz
plt.plot(toplamYolcu.index, toplamYolcu, label='Toplam Yük')
plt.plot(toplamIcHatYolcu.index, toplamIcHatYolcu, label='İç Hat Yük')
plt.plot(toplamDisHatYolcu.index, toplamDisHatYolcu, label='Dış Hat Yük')
plt.xlabel('Yıl')
plt.ylabel('Yük Ağırlığı')
plt.title('Yıllara Göre Yük Ağırlığı')
plt.legend()
plt.show()
plt.close()
```

## Problem 3

Bir veri çatısı (data frame) oluşturun ve aşağıdaki tablodaki verileri içine yerleştirin. Veri çatısının sütunları sırasıyla "Ad_Soyad", "Yas", "Cinsiyet", "Meslek" olsun.

| Ad_Soyad | Yas | Cinsiyet | Meslek |
|------ |-----|----------|--------|
| Ali   Yılmaz  | 42  | Erkek    | Mühendis|
| Canan Kaya    | 35  | Kadın    | Doktor |
| Ece   Özer    | 27  | Kadın    | Hukukçu|
| Fatma Yılmaz  | 45  | Kadın    | Avukat |
| Gamze Kaya    | 32  | Kadın    | Mühendis|

- Veri çatısının ilk 3 satırını yazdırın.
- Veri çatısının ad-soyad sütununu temelli olarak etikete (indexe) kaydedin, ve ekrana yazdırın.
- Veri çatısındaki kişilerin yaş ortalamasını hazır fonksiyon kullanarak hesaplayın ve ekrana yazdırın.
- Yaşı 40'dan büyük olanların bilgilerini ekrana yazdırın.

### Çözüm

```python
import pandas as pd

df= pd.DataFrame([\
    ['Ali Yılmaz', 42, 'Erkek', 'Mühendis'],\
    ['Canan Kaya', 35, 'Kadın', 'Doktor'],\
    ['Ece Özer', 27, 'Kadın', 'Hukuçu'],\
    ['Fatma Yılmaz', 45, 'Kadın', 'Avukat'],\
    ['Gamze Kaya', 32, 'Kadın', 'Mühendis']],\
    columns= ['Ad_Soyad', 'Yas', 'Cinsiyet', 'Meslek'])

print(df.head(3))
print("------------------")
df.set_index('Ad_Soyad', inplace=True)
print(df)
print("------------------")
print(df.Yas.mean())
print("------------------")
print(df[df.Yas>40])
```

## Problem 4

Bir fizik laboratuvarında, bir yayın esneklik sabiti ölçümü için deney yapılmıştır. Deney, bir dizi ağırlığın ($m_{1}$, $m_{2}$, $m_{3}$, $\dots$) yayın ucuna asılması ve her bir ağırlığın yayı uzatma miktarının ölçülmesiyle gerçekleştirilmiştir.

Veriler, her bir ağırlığın yayın uzatma miktarı (kg biriminde) ve uygulanan kuvvetin (N biriminde) bir listesi olarak elde edilmiştir.

| Kütle (kg) | Uzama, $\Delta x$ (m) |
|:---:|:---:|
|0.1 | 0.02|
|0.2 | 0.05|
|0.3 | 0.07|
|0.4 | 0.1|
|0.5 | 0.12|

1. **[5 Puan]** Bu verileri bir DataFrame'e kaydedin.
2. **[5 Puan]** Her kütle için yayın esneklik sabitini ($k$ [N/m]) hesaplayın, ($k = F / \Delta x$) ve DataFrame'e yeni sütun olarak ekleyin. ($g=9.81$ $m/s^{2}$)
3. **[5 Puan]** Her bir ağırlık için potansiyel enerjiyi hesaplayın ($E = 1/2 \times k \times x^{2}$) ve DataFrame'e yeni sütun olarak ekleyin.
4. **[5 Puan]** DataFrame'in son halinin ilk satırını ekrana yazdırın.
5. **[5 Puan]** DataFrame'in son halinin son satırını ekrana yazdırın.
6. **[5 Puan]** Yatay eksende uzama (m), dikey eksende potansiyel enerji (J = N $\times$ m) olacak şekilde bir grafik oluşturun.

### Çözüm

```python
import pandas as pd
import matplotlib.pyplot as plt

# Verileri oluşturma
data = {
    'Kütle (kg)': [0.1, 0.2, 0.3, 0.4, 0.5],
    'Uzatma (m)': [0.02, 0.05, 0.07, 0.1, 0.12]
}

# DataFrame oluşturma
df = pd.DataFrame(data)

# Yayın esneklik sabiti hesaplama
df['Yayın Esneklik Sabiti (N/m)'] = df['Kütle (kg)']*9.81 / df['Uzatma (m)']

# Potansiyel enerjiyi hesaplama
df['Potansiyel Enerji (J)'] = 0.5* df['Yayın Esneklik Sabiti (N/m)']* df['Uzatma (m)']**2

plt.plot(df['Uzatma (m)'], df['Potansiyel Enerji (J)'])
plt.xlabel('Uzatma (m)')
plt.ylabel('Potansiyel Enerji (J)')
plt.show()

# DataFrame'i yazdırma
print(df.head(1))
print(df.tail(1))
```

## Problem 5

[Bu linkteki](../../../veri/veri_bilgYont1_notlar.csv) `veri_bilgYont1_notlar.csv` dosyasını indirin. Bu dosyada her bir öğrencinin ödevleri, quizleri, arasınav ve final notları bulunmaktadır. Bu dosyadaki veri kütüphanesini kullanarak aşağıdaki soruları cevaplayın.

1. Dosyayı `pandas` kütüphanesini kullanarak okuyun.
2. Verinin ilk 5 satırını ekrana yazdırın.
3. Verinin son 2 satırını ekrana yazdırın.
4. Verinin sütunların isimlerini ekrana yazdırın.

Aşağıdaki işlemleri yapın ve değişkene atayın. Atadıktan sonra ilk 2 satırını ekrana yazdırın.

5. Etiketleri `ogrenci1`, `ogrenci2` ... `ogrenci14` gibi olacak şekilde değiştirin. 
6. Her bir öğrencinin ödevin ortalamasını bulun ve veri çatısında (data frame) bir sütun olarak kaydedin. Sütunun ismi `OdevOrt` olsun.
7. Her bir öğrencinin quizlerinin ortalamasını bulun ve veri çatısında (data frame) bir sütun olarak kaydedin. Sütunun ismi `QuizOrt` olsun.
8. Her bir öğrencinin dönem sonu ortalamasını bulun ve sütun ismi `Ortalama` olacak şekilde kaydedin. Dönem sonu ortalaması aşağıdaki gibi hesaplanır:
   
   - Quizler \%10
   - Ödevler \%20
   - Arasınav \%30
   - Final \%40
   
9. Her bir öğrencinin harf sonu notunu, ortalamaya bakarak hesaplayın ve sütun ismi `HarfNot` olacak şekilde kaydedin. Harfli notlar aşağıdaki gibi hesaplanır:

|Ortalama | Harf Notu |
|---|---|
|90-100 | AA |
|85-89 | BA |
|80-84 | BB |
|75-79 | CB |
|70-74 | CC |
|65-69 | DC |
|60-64 | DD |
|50-59 | EE |
|0-49 | FF |

10. Her bir öğrencinin quizlerinin arasından en yüksek 5 notu seçin ve `QuizOrtBoost` sütunu olarak kaydedin. Her öğrencinin ortalamasını ve harf notunu `QuizOrtBoost` kullanarak hesaplayın.

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
import numpy as np
#1
df= pd.read_csv(veri_dir+"/veri_bilgYont1_notlar.csv")

#2
print(f"\n2)\n{df.head()}")

#3
print(f"\n3)\n{df.tail(2)}")

#4
print(f"\n4)\n{df.columns.values}")

#5
idices= []
for it in range(1, df.shape[0]+1):
    idices.append(f"Ogrenci{it}")
df.index= idices
print(f"\n5)\n{df.head(2)}")

#6
odevBasliklari= df.columns[:9] #[0:9] # 9 ödev var.
df['OdevOrt'] = df[odevBasliklari].mean(axis=1)
print(f"\n6)\n{df.head(2)}")

#7
quizBasliklari= df.columns[9:16] #[9:16] # 7 quiz var.
df['QuizOrt'] = df[quizBasliklari].mean(axis=1)
print(f"\n7)\n{df.head(2)}")

#8 
df['Ortalama']= df["QuizOrt"]*0.1+ df["OdevOrt"]*0.2\
    + df["Arasinav"]*0.3+ df["Final"]*0.4
print(f"\n8)\n{df.head(2)}")

#9
harfNotu={
    "AA": [90,100],
    "BA": [85,89],
    "BB": [80,84],
    "CB": [75,79],
    "CC": [70,74],
    "DC": [65,69],
    "DD": [60,64],
    "EE": [50,59],
    "FF": [0,49]
}
df["HarfNot"]= ["" for x in range(len(df))]
for i in range(len(df)):
    ortalama = df["Ortalama"][i]
    for harf, aralik in harfNotu.items():
        if ortalama >= aralik[0] and ortalama <= aralik[1]:
            df.loc[df.index[i], 'HarfNot'] = harf
            break
print(f"\n9)\n{df['HarfNot']}")

#10
# QuizOrtBoost
quizBasliklari= df.columns[9:16]
df["QuizOrtBoost"]= df["Butunleme"]
for i in range(len(df)):
    quizOrtBoost= df[quizBasliklari].iloc[i].nlargest(5).mean()
    df.loc[df.index[i], "QuizOrtBoost"]= quizOrtBoost

# OrtalamaBoost
df['OrtalamaBoost']= df["QuizOrtBoost"]*0.1+ df["OdevOrt"]*0.2\
    + df["Arasinav"]*0.3+ df["Final"]*0.4

# HarfNotBoost
df["HarfNotBoost"]= [""]*len(df)
for i in range(len(df)):
    ortalama = df.OrtalamaBoost[i]
    for harf, aralik in harfNotu.items():
        if ortalama >= aralik[0] and ortalama <= aralik[1]:
            df.loc[df.index[i], "HarfNotBoost"] = harf
            break
print(f"\n10)\n{df['HarfNotBoost']}")
```