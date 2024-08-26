---
title: "Uygulama - Ses Dalgaları - Problem Cevapları"
---

## Problem 1

**Kara Delik Birleşmesi (GW150914)**

1. <https://gwosc.org/events/GW150914/> sitesine gidin. Bu sitede 2015 yılında tespit edilen kara delik birleşmesi verileri bulunmaktadır.
2. _Observation of Gravitational Waves from a Binary Black Hole Merger_ başlığına tıklayınız. Burada hem Hanford hem de Livingston merkezlerinden alınan veriler bulunmaktadır.
   1. <https://gwosc.org/GW150914data/P150914/fig1-observed-H.txt>
   2. <https://gwosc.org/GW150914data/P150914/fig1-observed-L.txt>
3. Bu dosyaları `pandas` kütüphanesini kullanarak okuyun, `pandas.read_csv("<LINK>, skiprows=1, sep=" ", header=None")` .
4. Verilerin grafiğini üst üste çizdirin.
5. Verileri wav dosyası olarak kaydedin. (https://www.youtube.com/watch?v=TWqhUANNFXw)
6. Verilerin Fourier dönüşümünü yapın ve grafiklerini çizdirin.

### Çözüm

```python
################################################
import os
import sys
# Bu dosyanın bulunduğu dizini al
current_dir = os.path.abspath('')
# 3 üst dizine çık + sesler klasörü
sesler_dir = os.path.join(os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir)), 'sesler')
# Bu klasör var mı? Yoksa oluştur
if not os.path.exists(sesler_dir):
    # Oluştur
    os.makedirs(sesler_dir)
# Linux/MacOS için
# Eğer OS Linux/Unix ise
if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    sesler_dir = sesler_dir + "/"
# Eğer OS, Windows ise
elif sys.platform == "win32":
    sesler_dir = sesler_dir + "\\"
################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy.fft as fft
# Hanford Verisi
veri_H= pd.read_csv(\
    "https://gwosc.org/GW150914data/P150914/fig1-observed-H.txt"\
        , skiprows=1, sep=" ", header=None)
veri_H.columns= ["zaman_s", "gerilim_1e21"]
# Livingston Verisi
veri_L= pd.read_csv(\
    "https://gwosc.org/GW150914data/P150914/fig1-observed-L.txt"\
        , skiprows=1, sep=" ", header=None)
veri_L.columns= ["zaman_s", "gerilim_1e21"]
# Çiz
plt.plot(veri_L.zaman_s, veri_L.gerilim_1e21, 'b', label='Livingston')
plt.plot(veri_H.zaman_s, veri_H.gerilim_1e21, 'r', label='Hanford', alpha=0.5)
plt.xlabel("Zaman (s)")
plt.ylabel("Gerilim (1e-21)")
plt.legend()
plt.show()
# HFD
# Hanford
veri_H_hfd= fft.fft(veri_H.gerilim_1e21.to_numpy())
veri_H_hfd_freq= fft.fftfreq(len(veri_H.gerilim_1e21), 1/len(veri_H.gerilim_1e21))
# Livingston
veri_L_hfd= fft.fft(veri_L.gerilim_1e21.to_numpy())
veri_L_hfd_freq= fft.fftfreq(len(veri_L.gerilim_1e21), 1/len(veri_L.gerilim_1e21))
# Çiz
plt.plot(veri_L_hfd_freq, np.abs(veri_L_hfd), 'b', label='Livingston')
plt.plot(veri_H_hfd_freq, np.abs(veri_H_hfd), 'r', label='Hanford', alpha=0.5)
plt.xlabel("Frekans (Hz)")
plt.ylabel("HFD")
plt.xlim([-125, 125])
plt.legend()
plt.show()
# Normalizasyon
orneklemOrani_L= np.int16(1/(veri_L.zaman_s.to_numpy()[1]- veri_L.zaman_s.to_numpy()[0]))
orneklemOrani_H= np.int16(1/(veri_H.zaman_s.to_numpy()[1]- veri_H.zaman_s.to_numpy()[0]))
veri_H_wav= np.int16(np.real(veri_H.gerilim_1e21 / np.max(np.abs(veri_H.gerilim_1e21))) * 32767)
veri_L_wav= np.int16(np.real(veri_L.gerilim_1e21 / np.max(np.abs(veri_L.gerilim_1e21))) * 32767)
# Wav dosyasına kaydet
wavfile.write(sesler_dir+ "GW150914_Hanford.wav", orneklemOrani_H, veri_H_wav)
wavfile.write(sesler_dir+ "GW150914_Livingston.wav", orneklemOrani_L, veri_L_wav)
# Yavaslatarak kaydet
wavfile.write(sesler_dir+ "GW150914_Hanford_yavas.wav", orneklemOrani_H//4, veri_H_wav)
wavfile.write(sesler_dir+ "GW150914_Livingston_yavas.wav", orneklemOrani_L//4, veri_L_wav)
```

## Problem 2

**Gürültü Silme**

1. Gürültü filtreleme işlemini `problem2-gurultulu-sinyal.wav` dosyası için yapın. Dosyaya [bu linkten](../../../sesler/problem2-gurultulu-sinyal.wav) ulaşabilirsiniz. Bu dosya C akoru ve G akorunu ardı ardına eklenerek oluşturulmuştur.
2. Ses dosyasını tam ortadan ikiye ayırın. 
3. İlk yarısına hfd yapın. Bu frekansların 261.63 Hz, 329.63 Hz ve 392.0 Hz olduğunu göreceksiniz.
4. Bu frekanslar dışındaki tüm frekansları sıfırlayın.
5. İkinci yarısına hfd yapın. Bu frekansların 392.0 Hz, 493.88 Hz ve 293.66 Hz olduğunu göreceksiniz.
6. Bu frekanslar dışındaki tüm frekansları sıfırlayın.
7. Ardından bu iki dosyanın ters hfd'sini alın ve birleştirin.
8. Filtrelenmiş ses dosyasını `problem2-gurultusuz-sinyal.wav` olarak kaydedin.

### Örnek Ses Dosyası Oluşturma

```python
################################################
import os
import sys
# Bu dosyanın bulunduğu dizini al
current_dir = os.path.abspath('')
# 3 üst dizine çık + sesler klasörü
sesler_dir = os.path.join(os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir)), 'sesler')
# Bu klasör var mı? Yoksa oluştur
if not os.path.exists(sesler_dir):
    # Oluştur
    os.makedirs(sesler_dir)
# Linux/MacOS için
# Eğer OS Linux/Unix ise
if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    sesler_dir = sesler_dir + "/"
# Eğer OS, Windows ise
elif sys.platform == "win32":
    sesler_dir = sesler_dir + "\\"
################################################

import numpy as np
import scipy.io.wavfile as wavfile
# Ses oluştur
orneklemOrani= 44100
sure= 2
t= np.linspace(0, sure, orneklemOrani* sure)
veri= np.zeros(len(t))
# İlk Yarısı, C Akoru
for it in [261.63, 329.63, 392.00]:
    veri+= np.sin(2*np.pi*it*t)
# İkinci Yarısı, G Akoru
tmp= np.zeros(len(t))
for it in [392.00, 493.88, 293.66]:
    tmp+= np.sin(2*np.pi*it*t)
# Veri ve tmp'yi birleştir.
veri= np.append(veri, tmp)
# Gürültü ekle
veri+= np.random.rand(len(veri))
veri= np.int16(veri / np.max(np.abs(veri)) * 32767)
# Wav olarak kaydet
wavfile.write(sesler_dir+ "problem2-gurultulu-sinyal.wav", orneklemOrani, veri)
```

### Çözüm

```python
################################################
import os
import sys
# Bu dosyanın bulunduğu dizini al
current_dir = os.path.abspath('')
# 3 üst dizine çık + sesler klasörü
sesler_dir = os.path.join(os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir)), 'sesler')
# Bu klasör var mı? Yoksa oluştur
if not os.path.exists(sesler_dir):
    # Oluştur
    os.makedirs(sesler_dir)
# Linux/MacOS için
# Eğer OS Linux/Unix ise
if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    sesler_dir = sesler_dir + "/"
# Eğer OS, Windows ise
elif sys.platform == "win32":
    sesler_dir = sesler_dir + "\\"
################################################

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy.fft as fft
# Dosyayı Oku
orneklemOrani, veri = wavfile.read(sesler_dir+ "problem2-gurultulu-sinyal.wav")
# Süre
sure= len(veri)/ orneklemOrani
# Zaman dizisi
t= np.linspace(0, sure, len(veri))
# İki ayrı veriye ayır
veri1= veri[:int(len(veri)/2)]
veri2= veri[int(len(veri)/2):]
# HFD
hfd_veri1= fft.fft(veri1)
hfd_veri2= fft.fft(veri2)
# Frekanslar
hfd_frek1= fft.fftfreq(len(veri1), 1/orneklemOrani)
hfd_frek2= fft.fftfreq(len(veri2), 1/orneklemOrani)
# Çiz
plt.plot(hfd_frek1, np.abs(hfd_veri1), 'r')
plt.plot(hfd_frek2, np.abs(hfd_veri2), 'k')
plt.xlim([-1000,1000])
plt.show()
plt.close()
# Tepe yapan frekansları bul
# Verinin ilk yarısında
elemanlar1=[]
for it in [261.63, 329.63, 392.00]:
    # Pozitif tarafta
    elemanlar1.append((np.abs(hfd_frek1 - it)).argmin())
    # Negatif tarafta
    elemanlar1.append((np.abs(hfd_frek1 + it)).argmin())
# Verinin ikinci yarısında
elemanlar2=[]
for it in [392.0, 493.88, 293.66]:
    # Pozitif tarafta
    elemanlar2.append((np.abs(hfd_frek2 - it)).argmin())
    # Negatif tarafta
    elemanlar2.append((np.abs(hfd_frek2 + it)).argmin())
# Filtrelenmiş HFD
hfd_veri1_filtre= np.zeros(len(hfd_veri1), dtype= np.complex128)
hfd_veri2_filtre= np.zeros(len(hfd_veri2), dtype= np.complex128)
# Make 0 except indices
hfd_veri1_filtre[elemanlar1]= hfd_veri1[elemanlar1]
hfd_veri2_filtre[elemanlar2]= hfd_veri2[elemanlar2]
# Çiz
plt.figure(figsize=(15,5))
plt.plot(hfd_frek1, np.abs(hfd_veri1_filtre), 'r')
plt.plot(hfd_frek2, np.abs(hfd_veri2_filtre), 'k')
plt.xlim([-1000,1000])
plt.show()
plt.close()
# THFD
veri1_filtre= fft.ifft(hfd_veri1_filtre)
veri2_filtre= fft.ifft(hfd_veri2_filtre)
# Birleştir
veri_filtre= np.concatenate((veri1_filtre, veri2_filtre))
# Normalize et
veri_filtre= np.int16((\
    np.real(veri_filtre)/ np.max(np.abs(veri_filtre)))* 32767)
# Wav dosyasına kaydet
wavfile.write(sesler_dir\
    + "problem2-filtrelenmis-sinyal.wav"\
        , orneklemOrani, veri_filtre.real)
```

## Problem 3

1. `/sesler/` klasörünün içerisinde bulunan [DeepPurple_SmokeOnTheWaterIntro.wav](../../../sesler/DeepPurple_SmokeOnTheWaterIntro.wav) dosyasını `orneklemOrani, data = wavfile.read()` olacak şekilde okuyun. Bu kayıt stereo bir dosyadır ve `data` değişkeninin ilk sütununu almanız yeterlidir. *Bu işlem ile stereo ses kaydının sadece bir tarafını alıyorsunuz.*
2. Sinyali 4'e ayırın. Bunun için aşağıda verilen tablodaki süreleri kullanın. *Yardım: `t` zaman arrayiniz olsun. $t=2$ saniyeye karşılık gelen argümanı bulmak için `arg1=np.argmin(np.abs(t- 2))` komutunu kullanabilirsiniz. Yani `arg1` değişkeni `100` gibi bir değer olursa `t[arg1]` değeri $2$ saniye olacaktır.*
3. Ayrılan riffleri zamana göre `fig, axs= plt.subplots(4, 1)` komutunu kullanarak 4 ayrı grafikte çizdirin. `axs[0].plot()` komutunu kullanın. Güzel gözükmesini istiyorsanız grafiği göstermeden önce `fig.tight_layout()` komutunu kullanabilirsiniz.
4. Ayırdığınız riffleri ayrı ayrı `wav` dosyası olarak kaydedin.
5. Tüm rifflerin Fourier dönüşümlerini alın ve frekanslarını belirleyin.
6. Tüm rifflerin pozitif frekans uzaylarını alt alta çizdirin. `axs[0].set_xlim(0, 1000)` komutunu kullanarak x-eksenini $0$ ile $1000$ arasında limitleyebilirsiniz.
7. ilk riff verisinin pozitif frekans uzayında gördüğünüz tepe (peak) değerleri hangi frekansa denk geliyor, bulun, ekrana yazdırın ve Fourier dönüşümü grafiğinde gösterin (`plt.axvline(x= hfdfrek_riff1_tepeler_pozitif[0], color= "red", lw= 0.5, ls= "--")`). *Yardım: "`fft` verisinde hangi değerler `fft > 9e6` koşulunu sağlanıyor?" sorusuna cevap olacak şekilde bir komut yazabilirsiniz.*

| Riff-1   | Riff-2   | Riff-3   | Riff-4   |
|:--------:|:--------:|:--------:|:--------:|
| 0 s - 2.0 s | 2.0 s - 4.25 s| 4.25 s - 6.35 s | 6.35 s - Sonuna kadar |

### Çözüm

```python
################################################
import os
import sys
# Bu dosyanın bulunduğu dizini al
current_dir = os.path.abspath('')
# 3 üst dizine çık + sesler klasörü
sesler_dir = os.path.join(os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir)), 'sesler')
# Bu klasör var mı? Yoksa oluştur
if not os.path.exists(sesler_dir):
    # Oluştur
    os.makedirs(sesler_dir)
# Linux/MacOS için
# Eğer OS Linux/Unix ise
if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    sesler_dir = sesler_dir + "/"
# Eğer OS, Windows ise
elif sys.platform == "win32":
    sesler_dir = sesler_dir + "\\"
################################################

import scipy.io.wavfile as wavfile
import scipy.fft as fft
import numpy as np
import matplotlib.pyplot as plt
#1
orneklemOrani, data = wavfile.read(sesler_dir+"DeepPurple_SmokeOnTheWaterIntro.wav")
data= data[:,0]
# Süre
sure= len(data)/ orneklemOrani
# Zaman dizisi
t= np.linspace(0, sure, len(data))
#2
riff1_arg= np.argmin(np.abs(t- 2.0))
riff2_arg= np.argmin(np.abs(t- 4.25))
riff3_arg= np.argmin(np.abs(t- 6.35))
# Veri
riff1= data[:riff1_arg]
riff1_t= t[:riff1_arg]
riff2= data[riff1_arg:riff2_arg]
riff2_t= t[riff1_arg:riff2_arg]
riff3= data[riff2_arg:riff3_arg]
riff3_t= t[riff2_arg:riff3_arg]
riff4= data[riff3_arg:]
riff4_t= t[riff3_arg:]
#3
# Çiz
fig, axs= plt.subplots(4,1)
axs[0].plot(riff1_t, riff1)
axs[1].plot(riff2_t, riff2)
axs[2].plot(riff3_t, riff3)
axs[3].plot(riff4_t, riff4)
plt.tight_layout()
plt.show()
plt.close()
#4
# Kaydet
wavfile.write(sesler_dir+"DeepPurple_SmokeOnTheWaterIntro_riff1.wav", orneklemOrani, riff1)
wavfile.write(sesler_dir+"DeepPurple_SmokeOnTheWaterIntro_riff2.wav", orneklemOrani, riff2)
wavfile.write(sesler_dir+"DeepPurple_SmokeOnTheWaterIntro_riff3.wav", orneklemOrani, riff3)
wavfile.write(sesler_dir+"DeepPurple_SmokeOnTheWaterIntro_riff4.wav", orneklemOrani, riff4)
#5
# HFD
hfd_riff1= fft.fft(data[:riff1_arg])
hfd_riff2= fft.fft(data[riff1_arg:riff2_arg])
hfd_riff3= fft.fft(data[riff2_arg:riff3_arg])
hfd_riff4= fft.fft(data[riff3_arg:])
# FFT Frekanslar
fftfrek_riff1= fft.fftfreq(len(hfd_riff1), 1/orneklemOrani)
fftfrek_riff2= fft.fftfreq(len(hfd_riff2), 1/orneklemOrani)
fftfrek_riff3= fft.fftfreq(len(hfd_riff3), 1/orneklemOrani)
fftfrek_riff4= fft.fftfreq(len(hfd_riff4), 1/orneklemOrani)
#6
# Çiz
fig, axs= plt.subplots(4,1)
axs[0].plot(fftfrek_riff1, np.abs(hfd_riff1))
axs[1].plot(fftfrek_riff2, np.abs(hfd_riff2))
axs[2].plot(fftfrek_riff3, np.abs(hfd_riff3))
axs[3].plot(fftfrek_riff4, np.abs(hfd_riff4))
for it in range(4):
    axs[it].set_xlim(0, 1000)
plt.tight_layout()
plt.show()
plt.close()
#7
hfdfrek_riff1_tepeler= fftfrek_riff1[hfd_riff1 > 9e6]
hfdfrek_riff1_tepeler_pozitif= hfdfrek_riff1_tepeler[hfdfrek_riff1_tepeler > 0]
# Print
print(f"Tepe noktalarında frekanslar: {hfdfrek_riff1_tepeler_pozitif} Hz")
# Çiz
plt.plot(fftfrek_riff1, np.abs(hfd_riff1))
for it in range(len(hfdfrek_riff1_tepeler_pozitif)):
    plt.axvline(x= hfdfrek_riff1_tepeler_pozitif[it], color= "red", lw= 0.5, ls= "--")
plt.xlim([0, 1000])
plt.show()
plt.close()
```