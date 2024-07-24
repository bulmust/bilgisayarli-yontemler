---
title: "Alıştırmalar ve Problemler"
---

## Problem 1

Kullanıcıdan dört sayı isteyin. Kullanıcının girdiği sayıları `float` formatına çevirin.

1. Kullanıcının girdiği sayıları sırayla bir listeye yerleştirin. Yani 4 elemanlı tek boyutlu bir listenin elemanlarını kullanıcıya doldurtun. Listeyi ekrana yazdırın.
2. Bu listenin tüm elemanlarının iki katını, `for` döngüsü kullanarak elde edin ve sonucu ekrana yazdırın.
3. Eğer girilen sayılardan en az bir tanesi 5'ten büyükse ekrana `... sayıları 5'ten büyüktür.` yazsın. Burada "..." yerine kullanıcının girdiği sayılar yazsın. Aksi taktirde `5'ten büyük sayı girmediniz.` yazsın.

## Problem 2

Bir liste oluşturun ve o listenin elemanları `4, 8, 15, 16, 23, 42` olsun. `for` döngüsü ve `.append()` fonksiyonu kullanarak listenin sonuna 1'den 80'a kadar sayılar ekleyin. Elde ettiğiniz yeni listenin adı `yeniListe` olsun.

   1. Bilgilendirme: `[3,7]` listesinin birinci elemanı `7`'dir. `yeniListe` listenin birinci, beşinci ve son elemanını ekrana yazdırın.
   2. `yeniListe` listesinin son beş elemanını ekrana yazdırın.
   3. `yeniListe` listesinin son elli elemanının toplamını ekrana yazdırın. 
   4. `yeniListe` listesinin son elli elemanının çarpımını ekrana yazdırın.
   5. `yeniListe` listesindeki tüm çift elemanları yerine `True`, tüm tek elemanları yerine `False` yazın.
   6. `yeniListe` listesinin elemanlarını alt alta olacak şekilde `yeniListe.txt` dosyasına yazdırın.

## Problem 3

1.  $1$'den $42$ sayısına kadar olan tüm sayıları toplayın. Sonu ekrana yazdırın.
2.  $1$'den $42$ sayısına kadar olan tüm çift sayıları toplayın. Ekrana yazdırın.
3.  $1$'den $89$'a kadar ($89$ dahil) olan tüm sayıları `for` döngüsünü kullanarak ekrana yazdıran bir betik yazın. Bu döngü, 18'de duracak şekilde olsun.

## Problem 4

1.  Bir fonksiyon yazın. Bu fonksiyon ekrana sadece `Naber Dünyalı?` yazdırsın.
2.  Bir fonksiyon yazın. Bu fonksiyon ekrana `Merhaba Dünyalı. Ben $100$'a kadar saymayı biliyorum.` yazsın ardından ekrana $0$'dan $100$'e kadar ($100$ dahil) tüm sayıları yazdırsın.
3.  Bir fonksiyon yazın. Bu fonksyion bir adet değişkeni alsın (Ör. `fonksiyon1(sayi)`) ve karesini geri döndürsün.
4.  Bir fonksiyon yazın. Bu fonksiyon bir adet değişkeni alsın. `a sayısının kübü ...` yazsın ve kübünü geri döndürsün. Burada "a" fonksiyonun aldığı değişken ve "..." o değişkenin kübü olacaktır.
5.  Bir fonksiyon yazın. Bu fonksiyon iki adet değişken alsın. Birinci değişkenden ikinci değişkene kadar olan tüm sayıların toplamını ekrana yazdırsın ve değerini döndürsün.
6.  Bir fonksiyon yazın. Bu fonksiyon bir adet değişken alsın. Girilen değişken $x^2-1=0$ denkleminin çözümü ise `True` değil ise `False` döndürsün.
7.  Bir fonksiyon yazın. Bu fonksiyon beş adet değişken alsın. Bu değişkenler bir cismin uzay-zaman koordinatları **x,y,z,t** ve x eksenine göre göreli (rölatif) **hızı** olsun. Eğer hız değişkenin değeri ışık hızından büyükse ekrana bunun mümkün olamayacağını yazsın. Eğer hız değişkeni ışık hızından küçükse, uzay-zaman koordinatlarının yere göre (duran gözlemci) ne olacağını hesaplasın ve yeni koordinatları ekrana yazdırsın. Bunun için [Lorentz Dönüşümünü](https://tr.wikipedia.org/wiki/Lorentz_d%C3%B6n%C3%BC%C5%9F%C3%BCm%C3%BC) kullanmanız gerekir. Buna ek olarak fonksiyon Galileo Dönüşümüne göre ne olacağını da hesaplasın ve ekrana yazdırsın. Fonksiyon, Lorentz dönüşümü ile elde ettiğiniz yeni uzay-zaman koordinatlarını döndürsün.

## Problem 5

**Modül**

Aşağıdaki soruları, oluşturduğunuz `fiz365.py` dosyası içerisine cevaplayın. Ardından `calistir.py` adında bir betik dosyasında yazdıklarınızı çağırın.

1. `fiz365.py` dosyasının içerisine `numpy` modülünü `np` ismiyle çağırın.
2. `faktoriyel()` adında bir fonksiyon yazın. Bu fonksiyon bir tam sayı alsın ve o sayının faktöriyelini döndürsün. Eğer verilen sayı tam sayı değilse `False` değeri döndürsün.
   1. `isinstance(sayi, int)` fonksiyonu, `sayi` degiskeninin `int` tipinde olup olmadığını sınar. Eğer `int` ise `True` değeri döndürür. Eğer değilse `False` değeri döndürür.
3. `topla()` adında bir fonksyion yazın. Bu fonksyion bir tam sayı alsın ve birden o sayıya kadar olan tüm tam sayıların toplamını döndürsün. Eğer sayı tam sayı değilse `False` değeri döndürsün.
4. `obeb()` adında bir fonksyion yazın. Bu fonksyion iki tam sayı alsın ve o sayıların ortak bölenlerinin en büyüğünü döndürsün. Eğer verilen sayı tam sayı değilse `False` değeri döndürsün.
5. `okek()` adında bir fonksyion yazın. Bu fonksyion iki tam sayı alsın ve o sayıların ortak katlarının en küçüğünü döndürsün. Eğer verilen sayı tam sayı değilse `False` değeri döndürsün.
6. `dik_mi()` adında bir fonksyion yazın. Bu fonksiyon üç sayı alsın ve bu üç sayıdan bir dik üçgen oluşuyor mu denesin. Eğer oluşuyorsa `True` dönmüyorsa `False` değeri döndürsün.
   1. Sayıları sıralamak için `np.sort([sayi1, sayi2])` fonksiyonunu kullanabilirsiniz.
7. `calistir.py` dosyası içerisine `fiz365` modülünü `f365` ismi ile çağırın ve aşağıdaki fonksiyonları çalıştırın. Çıktılarını ekrana ne olduklarını belirterek yazdırın.
   1. `faktoriyel(5)`, `faktoriyel(5.5)`
   2. `topla(5)`, `topla(5.5)`
   3. `obeb(12, 28)`, `obeb(12, 28.5)`
   4. `okek(8, 28)`, `okek(8, 28.5)`, `okek(8.3, 28)`. Sonuç neden tam sayı yani `int` şeklinde değil de `.0` şeklinde oluyor? Açıklayınız.
   5. `dik_mi(3, 5, 4)`, `dik_mi(3, 4, 6)`
8. `fizik365.py` dosyasını kaydedin ve yedekleyin. Bu dosyayı dersin geri kalanında kullanacağız.

## Problem 6

**Karışık Alıştırmalar**

Aşağıdaki sorularda fonksiyonları yazın. Ardından uygun değerler için fonksyionları çağırın ve çıktısını ekrana yazdırın.

1. Bir fonksiyon yazın. Bu fonksiyon iki adet değişken alsın. Birinci değişkenden ikinci değişkene kadar (ikinci değişken dahil değil) olan tüm sayıların toplamını ekrana yazdırsın ve değerini döndürsün.
2. Bir fonksiyon yazın. Bu fonksiyon bir adet değişken alsın. Girilen değişken $x^3+2x^2-x-1=0$ denkleminin çözümü ise `True` değil ise `False` döndürsün.
3. Bir fonksyion yazın. Bu fonksiyon bir adet değişken alsın. Bu değişken **uzaklık** gibi olsun ve 1 boyutlu negatif elektrik yükünün girilen (değişken) uzaklıktaki elektrik potansiyelini birimiyle beraber ekrana yazdırsın ve değerini döndürsün.
4. Bir fonksiyon yazın. Bu fonksiyon iki adet değişken alsın. Birinci değişken **konumdaki belirsizlik** gibi olsun.İkinci değişken de **momentumdaki belirsizlik** gibi olsun. Girilen değerleri Heisenberg Belirsizlik İlkesine uyup uymadığını kontrol etsin. Eğer uyuyorsa `True` eğer uymuyorsa `False` döndürsün.
5. Bir fonksiyon yazın. Bu fonksiyon üç adet değişken alsın. Bu değişkenler; **kütle 1**, **kütle 2** ve **uzaklık** olsun. Fonksiyonda, girilen kütle ve uzaklık değerleri kullanılarak iki kütle arasında oluşan çekim kuvvetinin değerini birimiyle beraber ekrana yazdırsın. Sonuç değerini de döndürsün.
6. Bir fonksiyon yazın. Bu fonksiyon dört adet değişken alsın. Bu değişkenler; **ilk uzaklık**, **ilk hız**, **zaman** ve **ivme** olsun. Fonksiyonda, girilen değerler kullanılarak, başlangıçta $x_0$ konumunda olan ve ilk hızı $v_0$ olan bir cismin $a$ ivmesi altında $t$ saniye sonra hangi konumda olacağı belirlensin. Sonucu birimiyle beraber ekrana yazdırın. Sonuç değerini döndürsün. Burada tüm büyüklüklükler skalerdir.
7. Bir fonksiyon yazın. Bu fonksiyon iki adet değişken alsın. Bu değişkenler; **başlangıç hızı** ve **atış açısı** olsun. Fonksiyonda, yatay düzlemde, $v_0$ ile $\theta$ açısıyla atılan bir cismin hangi konumda tekrar yatay düzlemde olacağı bulunsun. Atıştan sonra hangi konumda olduğu, havada geçirdiği süre ve maksimum çıkabileceği yükseklik ekrana yazdırılsın. Bu üç değerden oluşan bir tuple oluşturun. Fonksiyon bu tuple'ı döndürsün. Burada tüm büyüklüklükler skalerdir.

### Çözüm

```python
# Karışık Alıştırmalar
import numpy as np
#1
def soru1(var1,var2):
    sonuc = 0
    for it in range(var1, var2):
        sonuc = sonuc+ it
    return sonuc
print(soru1(3,10))
#2
def soru2(x):
    if x**2- 1 == 0:
        return True
    else:
        return False
print(soru2(1))
print(soru2(-1))
print(soru2(2))
#3
def soru3(r_m):
    sabit_Nm2_C2 = 8.99*10e9 # Nm^2/C^2 
    elektrikYuk_C= 1.602*10e-19 # C
    potansiyel_V = sabit_Nm2_C2* elektrikYuk_C / r_m
    return potansiyel_V
print(soru3(r_m=10))
#4
def soru4(deltaX_m, deltaP_kgm_s):
    hBar_J_s= 1.0545718*10e-34 # J*s
    # 1 J = 1 kg m^2 / s^2
    if deltaX_m* deltaP_kgm_s > hBar_J_s/2:
        return True
    else:
        return False
print(soru4(deltaX_m=1e-19, deltaP_kgm_s=1e-9))
#5
def soru5(kutle1_kg, kutle2_kg, r_m):
    sabit_Nm2_kg2= 6.67*10e-11 # Nm^2/kg^2
    return sabit_Nm2_kg2* kutle1_kg* kutle2_kg/ r_m**2
print(soru5(kutle1_kg=10, kutle2_kg=10, r_m=10))
#6
def soru6(x0_m, v0_m_s, t_s, a_m2_s):
    return x0_m+ v0_m_s*t_s+ 0.5* a_m2_s* t_s**2
print(soru6(x0_m=10, v0_m_s=10, t_s=10, a_m2_s=10))
#7
def soru7(v0_m_s, theta):
    g_m_s2= 9.81
    
    v0x_m_s= v0_m_s* np.sin(theta)
    v0y_m_s= v0_m_s* np.cos(theta)
    
    # t ucus
    tUcus_s= 2*(v0y_m_s/g_m_s2)
    
    # Yatay duzlemde olduğu nokta
    xSon_m= v0x_m_s* tUcus_s
    
    # Maksimum Yükseklik
    hMax_m= (v0y_m_s* (tUcus_s/2))/2
    
    return (xSon_m, tUcus_s, hMax_m)
print(soru7(v0_m_s=10, theta=np.pi/4))
```

## Problem 7

**Matris çarpımı**

1. 2 adet 3x3 matris oluşturun. Bunlardan bir tanesi 1'den 10'a kadar (10 dahil değil) diğeri ise 10'dan 19'a kadar olsun.
2. Bu iki matrisi `@` ile çarpın ve sonucu ekrana yazdırın.
3. `sonuc` adında 3x3'lük sıfır matrisi oluşturun.
4. İlk matrisin birinci, ikinci ve üçüncü satırlarını ekrana yazdırın.
5. İkinci matrisin tüm sütunlarını ayrı ayrı ekrana yazdırın.
6. İlk matrisin ilk satırını ikinci matrisin ilk sütunu ile çarpın. Çıkan sonucu `sonuc` elemanın birinci satır birinci sütunundaki elemanına atayın.
7. İlk matrisin ikinci satırını ikinci matrisin ilk sütunu ile çarpın. Çıkan sonucu `sonuc` elemanın birinci satır ikinci sütunundaki elemanına atayın.
8. İlk matrisin üçüncü satırını ikinci matrisin ilk sütunu ile çarpın. Çıkan sonucu `sonuc` elemanın birinci satır üçüncü sütunundaki elemanına atayın.
9. İlk matrisin ikinci satırını ikinci matrisin ilk sütunu ile çarpın. Çıkan sonucu `sonuc` elemanın ikinci satır birinci sütunundaki elemanına atayın.
10. `mat_carp` adında bir fonksiyon oluşturun ve bu fonksiyon iki adet matris alsın. İki matrisi, `for` döngü(leri)sü yardımı ile çarpsın. Adımlar aşağıdaki gibidir.
    1. Bu fonksiyon, matrislerin boyutlarını incelesin. Eğer matrislerin boyutu, ilk matrisin boyutu **NxM**, ikinci matrisin boyutu **MxT** şeklinde değilse `False` değerini döndürsün.
    2. Eğer herhangi bir matrisin tüm elemanları **0** ise **Bir matrisin tüm elemanları sıfırdır.** şeklinde ekrana yazı yazsın ve `for` döngüsüne girmeden sonucu uygun boyutta **0** matrisi döndürsün.
    3. Eğer herhangi bir matris birim matris ise **... matrisi birim matristir.** şeklinde ekrana yazı yazsın ve `for` döngüsüne girmeden sonucu ekrana yazsın.
11. Yukarıdaki yazdığınız fonksiyonu uyarı metinleri ekranda yazacak şekilde bir çok kez çağırın.
12. Eğer `mat_carp()` fonksiyonunu çağırırken girdilerden birisi bir boyutlu array olursa, hata alacaksınız. Bunun nedeni hakkında düşünün ve gerekli düzenlemeyi yapın.

### Çözüm

```python
import numpy as np
#1 
mat1= np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2= np.array([[10,11,12],[13,14,15],[16,17,18]])
print(mat1)
print(mat2)
#2
print(mat1 @ mat2)
#3
sonuc= np.zeros((3,3))
#4
print(mat1[0,:])
print(mat1[1,:])
print(mat1[2,:])
#5
print(mat2[:,0])
print(mat2[:,1])
print(mat2[:,2])
#6
sonuc[0,0]= np.sum(mat1[0,:] * mat2[:,0])
print(sonuc)
#7
sonuc[0,1]= np.sum(mat1[0,:] * mat2[:,1])
print(sonuc)
#8
sonuc[0,2]= np.sum(mat1[0,:] * mat2[:,2])
print(sonuc)
#9
sonuc[1,0]= np.sum(mat1[1,:] * mat2[:,0])
print(sonuc)
#10
def mat_carp(mat1, mat2):
    boy1= np.shape(mat1)
    boy2= np.shape(mat2)
    #10.1
    if boy1[1] != boy2[0]:
        return False
    #10.2
    if np.array_equal(mat1, np.zeros(boy1)) or np.array_equal(mat2, np.zeros(boy2)):
        print("Bir matrisin tüm elemanları sıfırdır.")
        print(f"mat1:\n {mat1}")
        print(f"mat2:\n {mat2}")
        return np.zeros((boy1[1], boy2[0]))
    #10.3
    if np.array_equal(mat1, np.eye(boy1[0])):
        print("Bir matris birim matristir.")
        print(f"mat1:\n {mat1}")
        return mat2
    if np.array_equal(mat2, np.eye(boy2[0])):
        print("Bir matris birim matristir.")
        print(f"mat2:\n {mat2}")
        return mat1
    sonuc= np.zeros((boy1[0], boy2[1]))
    for it1 in range(boy1[0]):
        for it2 in range(boy2[1]):
            sonuc[it1,it2]= np.sum(mat1[it1,:] * mat2[:,it2])
    return sonuc
#11
mat1= np.array([[1,2],[3,4]]) #np.zeros((3,3)) #np.eye(3) #np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2= np.array([[10,11,12],[13,14,15],[16,17,18]])
print(f"mat_carp(mat1, mat2)\n {mat_carp(mat1, mat2)}")
print(f"\nmat1 @ mat2 \n{mat1 @ mat2}")
```

## Problem 8

**Dalga Fonksiyonun Normalizasyonu**

1. `normalize_et_dalgaFonk` adında bir fonksiyon yazın. Bu fonksiyonun bir adet numpy array tipi değişken alsın. 
   1. Alınan array en genel olarak sanal sayılardan oluşsun. Array'in her elemanını kendisinin sanal eşleniği (`np.conj()`) kendisini çarpsın ve çıkan sonuçları toplayıp **bir** adet  sayı elde etsin.
   2. Fonksiyona girdi olarak verilen arrayi, elde edilen bu sayının kareköküne (`np.sqrt()`) bölsün ve elde edilen arrayi geri döndürsün.
   3. Girdi 1 boyutlu array değilse, **bu fonksiyon sadece arrayler için çalışmaktadır.** yazsın. Bunun için `np.ndim()` fonksiyonunu kullanbilirsiniz. Fonksiyon girdisi bir boyutlu array değilse `None` değerini döndürsün.
2. Bu fonksiyonu `[1, 1]` değerleri için çağırın.
3. `xAxis` adında ve içeriği `0`'dan `1`'e kadar 100 elemanlı bir array oluşturun. Yardım: `np.linspace(baslangicSayi, bitisSayi, adet)`
4. `yAxis` adında ve içeriği `0`'dan `1`'e kadar 100 elemanlı bir array oluşturun.
5. Çizim yapmak için `matplotlib.pyplot` modülünü `plt` ismiyle çağırın ve x ve y eksenlerini çizdirin. Çizginin rengi siyah `k` olsun.
6. `[1, 1]` arayini normalize ettiğimizde elde ettiğimiz arrayi de kırmızı ile `r` çizdirin.
   1. Bunun için 3. ve 4. adımı `normalize_et_dalgaFonk` fonksiyonunu kullanarak tekrarlamanız gerekir. Fonksiyonu çağırdığınızda geri dönen iki değerden ilki `xAxis`'in 0'dan o noktaya kadar olan değerlerini belirleyecek, ikincisi ise `yAxis`'in 0'dan o noktaya kadar olan değerlerini belirleyecek.
7. __Bu adımda bilgisayar kod yazmanıza gerek yoktur.__ Kuantum dalga fonksiyonu aşağıdaki gibi verilmiştir. Aşağıdaki verilen gösterimler eşdeğerdir.

$$
|\psi> = A \left(\sin\theta|\uparrow> + \cos\theta|\downarrow>\right)
$$

$$
|\psi> = A\sin\theta \left(\begin{matrix}1\\0\end{matrix}\right) + A\cos\theta\left(\begin{matrix}0\\1\end{matrix}\right)
$$

$$
|\psi> = A\left(\begin{matrix}\sin \theta\\\cos \theta\end{matrix}\right)
$$

Bu kuantum durumu normalize olması için A ne olmalıdır? Yardım: $|<\psi|\psi>|^2=1$ için $A$ ne olmalıdır?

8. Aşağıdaki dalga fonksiyonunu el ile normalize ediniz. `normalize_et_dalgaFonk` fonksiyonunu kullanarak yaptığınız hesabı kontrol ediniz.

$$
|\psi> = A \left((1+i)|\uparrow> + (1-i)|\downarrow> \right)
$$

### Çözüm

Dalga Fonksiyonunu normalize edelim.

$$
|<\psi|\psi>|^2=1
$$

$$
| |A|^{2} \left[(1-i)(1+i) + (1+i)(1-i) \right]|^2 = 1
$$

$$
|4 |A|^{2} |^{2} = 1
$$

$$
|A|^{2}= \frac{1}{4}
$$

$$
A= \frac{1}{2}
$$

Bu durumda normalize edilmiş dalga fonksiyonu aşağıdaki gibidir.

$$
|\psi> = \frac{1+i}{2}|\uparrow> + \frac{1-i}{2}|\downarrow>
$$

Diğer soruların cevapları da aşaıdaki gibidir.

```python
import numpy as np
import matplotlib.pyplot as plt

#1
def normalize_et_dalgaFonk(arr1):
    #1.1
    if np.ndim(arr1) != 1:
        print("Bu fonksiyon sadece arrayler için çalışmaktadır.")
        return None
    sonuc= 0
    for it in arr1:
        sonuc += np.conj(it)* it
    normalizasyonKatsayisi= 1/np.sqrt(sonuc)
    return arr1* normalizasyonKatsayisi
#2
print(f"normalize_et_dalgaFonk(np.array([1,1])) = {normalize_et_dalgaFonk(np.array([1,1]))}")
#3
xAxis= np.linspace(0, 1, 100)
#4
yAxis= np.linspace(0, 1, 100)
#5
plt.plot(xAxis, yAxis, 'k')
#6
normalize_arr= normalize_et_dalgaFonk(np.array([1,1]))
xAxis= np.linspace(0, normalize_arr[0], 100)
yAxis= np.linspace(0, normalize_arr[1], 100)
plt.plot(xAxis, yAxis, 'r')
#8
print(normalize_et_dalgaFonk(np.array([1+1j,1-1j])))
```