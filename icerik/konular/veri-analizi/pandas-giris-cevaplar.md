---
title: "pandas - Giris - Problem Cevapları"
---

## Problem 1

1. Ekte bulunan `european_cities.csv` dosyasını okuyarak bir `pandas` dataframe (veri çerçevesi) oluşturun. Bu datayı okumak için `pd.read_csv('european_cities.csv')` fonksiyonunu kullanabilirsiniz.
2. [@web2024Feb-6] referansındaki `european_cities.csv` dosyasını okuyarak farklı isimde bir `pandas` dataframe (veri çerçevesi) oluşturun.
3. `.info()` fonksiyonunu kullanarak içeriği hakkında bilgi edinin.

### Çözüm

```python
import pandas as pd
# 1. Soru
df= pd.read_csv('../../../veri/veri-analizi-european_cities.csv')
# 2. Soru
df2= pd.read_csv('https://raw.githubusercontent.com/jrjohansson/numerical-python-book-code/master/european_cities.csv')
# 3. Soru
print(df.info())
```

## Referanslar

1. Numerical Python: Scientific Computing and Data, Science Applications with Numpy, SciPy and Matplotlib, Robert Johansson, Apress, İkinci Basım, 2019, **syf 406**
2. VS Code ile csv dosyası görüntüleme: [Excel Viewer](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)
