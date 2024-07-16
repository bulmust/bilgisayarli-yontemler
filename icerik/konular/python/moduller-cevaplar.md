---
title: "Modüller - Problem Cevapları"
---

## Problem 1

1. Bir boyutlu arrayler
   1. 80'den 250'ye kadar sayıları ikişer ikişer giden bir array oluşturunuz ve ekrana yazdırınız. Bu arrayin adı `arr1d_1` olsun.
   2. Bu arrayin elemanlarının toplamını `np.sum()` fonksiyonu ile bulunuz ve ekrana yazdırınız.
   3. Bu arrayin elemanlarının ortalamasını `np.mean()` fonksiyonu ile bulunuz ve ekrana yazdırınız.
   4. Bu arrayin elemanlarının toplamını `for` döngüsü kullanarak bulunuz ve ekrana yazdırınız.
2. İki boyutlu arrayler
   1. 1 ile 100 arasındaki sayıları 10x10'luk bir matris haline getiriniz ve ekrana yazdırınız. Bu matrisin adı `arr2d_1` olsun.
   2. Bu matrisin elemanlarının toplamını `np.sum()` fonksiyonu ile bulunuz ve ekrana yazdırınız.
   3. Bu matrisin elemanlarının toplamını `for` döngüsü kullanarak bulunuz ve ekrana yazdırınız.
3. Bir boyutlu ve iki boyutlu arraylerde matematiksel işlemler
   1. Sadece 2'lerden oluşan 3 elemanlı bir boyutlu array oluşturunuz ve ekrana yazdırınız. Bu arrayin adı `arr1d_2` olsun. 
   2. 1'den 6'ya kadar olan sayıları ile 3x2'lük bir matris oluşturunuz ve ekrana yazdırınız. Bu matrisin adı `arr2d_2` olsun.
   3. `arr1d_2` arrayinin boyutunu ekrana yazdırınız.
   4. `arr2d_2` matrisinin boyutunu ekrana yazdırınız.
   5. Bu iki arrayin matris çarpımını yapınız ve ekrana yazdırınız.
4. Bir boyutlu sütun array (**Vektör**)
   1. Bir boyutlu, elemanları 1'den 3'e kadar olan sütun array oluşturunuz ve ekrana yazdırınız. Bu arrayin adı `vec_1` olsun.
   2. 1'den 6'ya kadar olan sayıları ile 2x3'lük bir matris oluşturunuz ve ekrana yazdırınız. Bu matrisin adı `arr2d_3` olsun.
   3. Bu iki arrayin matris çarpımını yapınız ve ekrana yazdırınız.

### Cevap

```python
import numpy as np
# 1. Soru
# 1.1. Soru
arr1d_1= np.arange(80,250)
print('arr1d_1\n', arr1d_1)

# 1.2. Soru
print("1.2 = ", np.sum(arr1d_1))

# 1.3. Soru
print("1.3 = ", np.mean(arr1d_1))

# 1.4. Soru
toplam=0
for it in arr1d_1:
    toplam += it
print('1.4 = ', toplam)
#veya
toplam2=0
for it in range(len(arr1d_1)):
    toplam2 += arr1d_1[it]
print('veya 1.4 = ', toplam2)

# 2. Soru
# 2.1. Soru
arr2d_1 = np.arange(1,101).reshape(10,10)
print('arr2d_1\n', arr2d_1)
# veya
arr2d_1 = np.array([np.arange(1,11),np.arange(11,21),np.arange(21,31),np.arange(31,41),np.arange(41,51)\
    , np.arange(51,61),np.arange(61,71),np.arange(71,81),np.arange(81,91),np.arange(91,101)])
print('arr2d_1\n', arr2d_1)

# 2.2. Soru
print("2.2 = ", np.sum(arr2d_1))

# 2.3. Soru
toplam=0
for it in arr2d_1:
    for it2 in it:
        toplam += it2
print('2.3 = ', toplam)
#veya
toplam2=0
for it in range(len(arr2d_1)):
    for it2 in range(len(arr2d_1[it])):
        toplam2 += arr2d_1[it,it2]
print('veya 2.3 = ', toplam2)

# 3. Soru
# 3.1. Soru
arr1d_2 = np.array([2,2,2])

# 3.2. Soru
arr2d_2 = np.array([[1,2],[3,4],[5,6]])

# 3.3. Soru
print("3.3 = ", arr1d_2.shape)

# 3.4. Soru
print("3.4 = ", arr2d_2.shape)

# 3.5. Soru
print("3.5 = ", np.dot(arr1d_2,arr2d_2))

# 4. Soru
# 4.1. Soru
vec_1 = np.array([[1],[2],[3]])
print('vec_1\n', vec_1)

# 4.2. Soru
arr2d_3 = np.array([[1,2,3],[4,5,6]])
print('arr2d_3\n', arr2d_3)

# 4.3. Soru
print("4.3 = \n", np.dot(arr2d_3, vec_1))
```

## Problem 2

1. `polinom1` adında `x` değişkeni ile çalışan bir fonksiyon oluşturun.
2. `polinom1` fonksiyonu $x^{2}-1$ değerini döndürsün.
3. Fonksiyon tanımlamasını bitirdikten sonra `if __name__ == '__main__':` bloğu yaratın. **ÖNEMLİ:** Artık her çalıştırılabilir dosyada bu bloğu kullanacağız.
4. `if __name__ == '__main__':` bloğu içerisinde `xAxis` değişkeni için -3 ile 3 arasında 1000 adet değer oluşturun.
5. Bu `xAxis` değişkeni için `polinom1` fonksiyonunu çağırın ve dönen sonucu `yAxis` değişkenine atayın.
6. `xAxis` ve `yAxis` değerlerini kullanarak grafik çizin.
7. Çizdiğiniz grafikte `xAxis` ve `yAxis` isimlerini belirleyin.
8. Arkaplan ızgarasını çizin.
9. Bu grafiği kapatın.
10. Yeni bir grafik çizdirin. Bu grafik için `xAxis` ve `yAxis` değerlerini kullansın ama bu kesikli cizgi seklinde olsun.
11. Yeni grafiği `polinom1.png` dosyası olarak kaydedin.
12. Bu grafiği kapatın.

### Cevap

```python
import matplotlib.pyplot as plt
import numpy as np

def polinom1(x):
    return x**2-1

if __name__ == '__main__':
    xAxis = np.linspace(-3, 3, 1000)
    yAxis = polinom1(xAxis)

    plt.plot(xAxis, yAxis)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()

    plt.plot(xAxis, yAxis, linestyle='dashed')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('polinom1.png')
    plt.close()
```