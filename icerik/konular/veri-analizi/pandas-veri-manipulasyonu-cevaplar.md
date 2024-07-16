---
title: "pandas - Veri Manipülasyonu - Problem Cevapları"
---

## Problem 1

1. <https://www.kaggle.com/datasets/prithusharma1/all-nobel-laureates-1901-present> sitesine gidin ve nobel ödülü almış kişiler ile ilgili veriyi indirin. Direkt indirmek için [tıklayınız.](../../veri/veri_nobel_latest.csv)
2. Verileri pandas paketi ile okuyun.
3. Cinsiyetler sütununda (Gender) biricik (unique) değerleri bulun. Bunları bir diziye (array) atayın.
4. Bulduğunuz biricik değerlerden "Gender" sütununda kaç adet olduğunu bulun.
5. Ödüllerin toplam cinsiyet (Gender) bar grafiğini çizdirin. `plt.bar()`
6. "Birth_Country_Code" sütununda biricik değerleri bulmadan önce `dropna()` komutu ile nan değerlerini silin.
7. Ödül alan kişilerin doğduğu ülkelerin ("Birth_Country_Code") toplam sayısını gösteren bir bar grafiği çizdirin.

### Çözüm

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("nobel_latest.csv")

all_unique_genders= df["Gender"].unique()
genders= np.zeros(len(all_unique_genders))

for it in range(len(df["Gender"])):
    for it2 in range(len(all_unique_genders)):
        if df["Gender"][it] == all_unique_genders[it2]:
            genders[it2] += 1

plt.bar(all_unique_genders, genders)
plt.show()
plt.close()

all_unique_birth_code= df["Birth_Country_Code"].dropna().unique()
birth_codes= np.zeros(len(all_unique_birth_code))

for it in range(len(df["Birth_Country_Code"])):
    for it2 in range(len(all_unique_birth_code)):
        if df["Birth_Country_Code"][it] == all_unique_birth_code[it2]:
            birth_codes[it2] += 1

plt.figure(figsize=(20,10))
plt.bar(all_unique_birth_code, birth_codes)
# Rotate xticks
plt.xticks(rotation=90)
plt.show()
plt.close()
```

## Problem 2

1. <https://www.kaggle.com/datasets/abhinand05/daily-sun-spot-data-1818-to-2019> sitesine gidin ve Güneş lekesi verilerini indirin. Direkt indirmek için [tıklayınız.](../../veri/veri_sunspot_data.csv)
2. Verileri pandas paketi ile okuyun.
3. İlk sütunu ("Unnamed: 0") silin.
4. "Number of Sunspots" başlığındaki tüm $-1$ olan terimleri `np.nan` ile değiştirin.
5. Yeni bir sütun oluşturun. Bu sütunun adı "Year-Month-Day" olsun. Bu sütuna yılları, ayları ve günleri içeren bir dize (string) yazın. Örneğin, "1818-01-01" gibi. Bunu yapabilmek için dize (string) tipine geçmeniz gerekmektedir. Örneğin `df["Day"].astype(str)`.
6. Günlere göre kaç adet güneş lekesi olduğunu ("Number of Sunspots") gösteren bir grafik çizdirin. Yatay eksende bir şey olmasın.
7. Yeni bir veri çatısı (dataframe) oluşturun. Bu veri çatısının etiketleri (indices) yıllar, sütunu ise o yıldaki toplam güneş lekesi sayısı olsun. `df.groupby("Hangi sütunu gruplayacak")["<Hangi sütuna göre gruplanacak>"].sum()` komutu ile gruplayabilirsiniz.
8. Yeni oluşturduğunuz veri çatısını çizdirin. Yaklaşık her 11 senede bir güneş lekesi sayısının arttığını gözlemleyebilirsiniz. Buna [Solar döngü](https://en.wikipedia.org/wiki/Solar_cycle) (Solar cycle) denir.

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
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv(os.path.join(veri_dir,"sunspot_data.csv"))
df.pop("Unnamed: 0")
df["Number of Sunspots"].replace(-1,np.nan, inplace=True)
# Combine Year Month and day columns
df["Year-Month-Day"] = df["Year"].astype(str) + "-" + df["Month"].astype(str) + "-" + df["Day"].astype(str)

plt.plot(df["Number of Sunspots"])
plt.show()
plt.close()

# Summation of all sunspots in a year and take one of them
df2= df.groupby("Year")["Number of Sunspots"].sum()
df2.plot(xlabel="Year", ylabel="Number of Sunspots")
plt.xlim([1980,2025])
plt.show()
plt.close()
```
