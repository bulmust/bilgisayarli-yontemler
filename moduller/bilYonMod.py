'''
Bilgisayarlı Yöntemler reposunda bulunan fonksiyonların kütüphanesi.
'''
import numpy as np

#! ===========================================
#! Adi Diferansiyel Denklem (ADD) Çözme
#! ===========================================
# Euler Yöntemi ile ADD Çözme (Tek Denklem)
def add_coz_euler(fonk_y_x, xBaslangic, xBitis, yBaslangic, adimSayisi):
    xTum= np.array([xBaslangic])
    yTum= np.array([yBaslangic])
    
    h= (xBitis- xBaslangic)/ adimSayisi
    for i in range(adimSayisi):
        xTum= np.append(xTum, xTum[i]+ h)
        yTum= np.append(yTum, yTum[i]+ h* fonk_y_x(yTum[i], xTum[i]))
    return xTum, yTum
# Euler Yöntemi ile ADD Sistemi Çözme (Denklem Sistemi)
def add_coz_euler_sistem(fonk_yVek_x, xBaslangic, xBitis, yBaslangic_vek, adimSayisi):
    xTum= np.array([xBaslangic])
    yBoy= len(yBaslangic_vek)
    yTum_vek= np.zeros((yBoy, adimSayisi+1))
    yTum_vek[:,0]= yBaslangic_vek
    #yTum_vek=
    #[[y_{0}(0), y_{0}(0+h), y_{0}(0+2h), ... ],
    # [y_{1}(0), y_{1}(0+h), y_{1}(0+2h), ... ]]
    
    h= (xBitis- xBaslangic)/ adimSayisi
    for i in range(adimSayisi):
        xTum= np.append(xTum, xTum[i]+ h)
        yTum_vek[:,i+1]= yTum_vek[:,i]+ h* fonk_yVek_x(yTum_vek[:,i], xTum[i])
    return xTum, yTum_vek
# 4. Derece Runge-Kutta Yöntemi
def add_coz_rk4_sistem(fonk_yVek_x, xBaslangic, xBitis, yBaslangic_vek, adimSayisi):
    xTum= np.array([xBaslangic])
    yBoy= len(yBaslangic_vek)
    yTum_vek= np.zeros((yBoy, adimSayisi+1))
    yTum_vek[:,0]= yBaslangic_vek
    #yTum_vek=
    #[[y_{0}(0), y_{0}(0+h), y_{0}(0+2h), ... ],
    # [y_{1}(0), y_{1}(0+h), y_{1}(0+2h), ... ]]
    
    h= (xBitis- xBaslangic)/ adimSayisi
    for i in range(adimSayisi):
        xTum= np.append(xTum, xTum[i]+ h)
        k1= h* fonk_yVek_x(yTum_vek[:,i], xTum[i])
        k2= h* fonk_yVek_x(yTum_vek[:,i]+ k1/2, xTum[i]+ h/2)
        k3= h* fonk_yVek_x(yTum_vek[:,i]+ k2/2, xTum[i]+ h/2)
        k4= h* fonk_yVek_x(yTum_vek[:,i]+ k3, xTum[i]+ h)
        yTum_vek[:,i+1]= yTum_vek[:,i]+ (k1+ 2*k2+ 2*k3+ k4)/6
    return xTum, yTum_vek
## ADD Çözme (odeint)
# import scipy.integrate as spInt
# yHep= spInt.odeint(fonk_y_x, np.array([y0, v0]), xHep)
 
#! ===========================================
#! Sayısal İntegral Alma
#! ===========================================
# ===========================================
# Trapezoidal Kural
def integral_trapezoidal(fonk, solSinir, sagSinir, adimSayisi):
    h= (sagSinir-solSinir)/ adimSayisi
    
    integral= 0
    for i in range(adimSayisi):
        integral= integral+ (fonk(solSinir)+ fonk(solSinir+h))* h/2
        solSinir= solSinir+ h
    # Alternatif Algoritma
    # xVal= np.arange(solSinir, sagSinir+h, h)
    # for i in range(adimSayisi):
    #     integral = integral + (fonk(xVal[i])+ fonk(xVal[i+1])) * h/2
    return integral
# Simpson 1/3 Kuralı
def integral_simpson(fonk, solSinir, sagSinir, adimSayisi):
    h= (sagSinir-solSinir)/ adimSayisi
    
    integral= fonk(solSinir)+ fonk(sagSinir)
    for i in range(1,adimSayisi):
        katsayi= solSinir + i*h
        if i%2 == 0:
            integral = integral+ 2* fonk(katsayi)
        else:
            integral = integral+ 4* fonk(katsayi)
    return integral* (h/ 3)
# Monte-Carlo İntegral Yöntemi
def integral_monteCarlo(fonk,solSinir,sagSinir,adimSayisi):
    if adimSayisi>1000000:
        print('Adım sayısı çok büyük. Lütfen 1.000.000\'den küçük bir adım sayısı giriniz.')
        return None
    # a ve b arasında n tane rastgele sayı üret
    x = np.random.uniform(solSinir,sagSinir,size=(adimSayisi))
    fonksiyonDegerleri = fonk(x)
    return ((sagSinir-solSinir)/adimSayisi)*np.sum(fonksiyonDegerleri)
# ===========================================
## Trapezoidal Kural - Scipy
# import scipy.integrate as scpInt
# integral, hata = scpInt.quad(fonk, solSinir, sagSinir)

#! ===========================================
#! Sayısal Türev Alma
#! ===========================================
# İlk Merkezi Farklar Yaklaşıklığı, Birinci Dereceden Türev
def turev_merkezi_olmayan_ilk_birinci(veri):
    xVeri= veri[:,0]
    yVeri= veri[:,1]
    
    veriAdeti= len(xVeri)
    # Turev terimi bir adet eksik olacak.
    # turev değişkeninin ilk sütunu xVerisi, ikinci sütunu türev değeri olacak. 
    turev= np.zeros((veriAdeti,2))
    
    # Adım aralığı sabit ise
    # h=xVeri[1]-xVeri[0]
    
    # Birinci dereceden türev algoritması
    for i in range(veriAdeti-1):
        turev[i,0]= xVeri[i]
        turev[i,1]= (yVeri[i+1]- yVeri[i])/ (xVeri[i+1]- xVeri[i])
        # turev[i,1]=(yVeri[i+1]-yVeri[i])/h
    
    # Son terimin türevi
    turev[-1,0]= xVeri[-1]
    turev[-1,1]= (yVeri[-1]- yVeri[-2])/ (xVeri[-1]- xVeri[-2])
    return turev

#! ===========================================
#! Kök Bulma
#! ===========================================
#Artan Arama Yöntemi
def kok_bulma_artan_arama(fonksiyon, aralikKucuk,aralikBuyuk, adimAraligi):
    '''[Numerical Methods in Engineering with Python 3]
    '''
    x1 = aralikKucuk
    f1 = fonksiyon(aralikKucuk)
    x2 = aralikKucuk + adimAraligi
    f2 = fonksiyon(x2)
    while np.sign(f1) == np.sign(f2):
        if x1 >= aralikBuyuk: 
            return None,None
        x1 = x2
        f1 = f2
        x2 = x1 + adimAraligi
        f2 = fonksiyon(x2)
    return x1,x2
# İkiye Bölme Yöntemi
def kok_bulma_ikiye_bolme(fonksiyon, aralikKucuk, aralikBuyuk, tolerans):
    '''https://pythonnumericalmethods.berkeley.edu/notebooks/chapter19.03-Bisection-Method.html
    '''
    # aralikKucuk ve aralikBuyuk kök mü?
    if np.sign(fonksiyon(aralikKucuk)) == np.sign(fonksiyon(aralikBuyuk)):
        raise Exception("The scalars a and b do not bound a root")
        
    # Aralığın orta noktasını bul
    m = (aralikKucuk + aralikBuyuk)/2
    
    # Eğer orta nokta kök ise, kök orta noktadır.
    if np.abs(fonksiyon(m)) < tolerans:
        return m
    # Eğer kök aralik küçük ve orta nokta arasındaysa, aralığı küçült
    elif np.sign(fonksiyon(aralikKucuk)) == np.sign(fonksiyon(m)):
        return kok_bulma_ikiye_bolme(fonksiyon, m, aralikBuyuk, tolerans)
    # Eğer kök aralik büyük ve orta nokta arasındaysa, aralığı küçült
    elif np.sign(fonksiyon(aralikBuyuk)) == np.sign(fonksiyon(m)):
        return kok_bulma_ikiye_bolme(fonksiyon, aralikKucuk, m, tolerans)
# Newton-Raphson Yöntemi
def kok_bulma_newton_raphson(fonksiyon, turevFonksiyon, baslangicNoktasi, tolerans):
    '''https://pythonnumericalmethods.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html
    '''
    # Başlangıç noktası kök mü?
    if np.abs(fonksiyon(baslangicNoktasi)) < tolerans:
        return baslangicNoktasi
    # Başlangıç noktası kök değilse, yeni bir başlangıç noktası bul
    else:
        return kok_bulma_newton_raphson(fonksiyon, 
                                        turevFonksiyon, 
                                        baslangicNoktasi - fonksiyon(baslangicNoktasi)/turevFonksiyon(baslangicNoktasi), 
                                        tolerans)

#! ===========================================
#! İnterpolasyon ve Eğri Uydurma Fonksiyonları
#! ===========================================
# Lagrange Interpolasyonu
def lagrange_interpolasyon_dizi(xVeri, yVeri, xAraDizi):
    '''
    Lagrange polinomu ile verilen noktalardan geçen polinom hesaplanır.
    '''
    # Verilen xVeri datasının boyutu tutulur.
    n = int(len(xVeri))
    # İstenilen xAraDizi datasının boyutu tutulur.
    nAra= int(len(xAraDizi))
    # =================

    # Lagrange polinomu hesaplanır.
    yDizi = np.zeros(nAra)
    for it in range(nAra):
        yGecici = 0.0
        for i in range(n):
            pt = 1.0
            # Kardinal fonksiyonu hesaplanır.
            for j in range(n):
                if i != j:
                    pt= pt* (xAraDizi[it]- xVeri[j])/(xVeri[i]- xVeri[j])
            # Lagrange polinomu hesaplanır.
            yGecici = yGecici + yVeri[i]* pt
        yDizi[it]= yGecici
    # =================
    return yDizi
# Newton Interpolasyonu
def newton_interpolasyon_dizi(xData, yData, xNewArray):
    '''[https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.05-Newtons-Polynomial-Interpolation.html]
    Newton polinomu ile verilen noktalardan geçen polinom hesaplanır.
    '''
    
    # Bölünmüş Fark (Divided Differences) hesaplayan fonksiyon.
    def divided_diff(xData, yData):
        '''
        Function to calculate the divided differences table
        '''
        n = len(yData)
        coef = np.zeros([n, n])
        # the first column is y
        coef[:,0] = yData
        
        for j in range(1,n):
            for i in range(n-j):
                coef[i,j] = (coef[i+1,j-1] - coef[i,j-1]) / (xData[i+j]-xData[i])
        return coef

    # Verilen x değerlerinin bir eksiğinin boyutu tutulur.
    n= len(xData)- 1
    # =================
    coef = divided_diff(xData, yData)[0, :]
    # =================
    # Newton polinomu hesaplanır.
    yNewArray = coef[n]
    for k in range(1,n+1):
        yNewArray = coef[n-k] + (xNewArray -xData[n-k])* yNewArray
    return yNewArray
# ===========================================
# Eğri Uydurma - En küçük kare uydurma
# np.polyfit(tumVeri_XBileseni, tumVeri_YBileseni, fitEdilecekPolinomunDerecesi)

#! ===========================================
#! Doğrusal Cebir Fonksiyonları
#! ===========================================
# LU Ayrıştırma Yöntemi ile L, U elde etme
def LU_ayrisma(katsayiMat):
    '''
    LU ayrıştırma yöntemi ile katsayı matrisi ayrıştırılır.
    
    coeffMat: Katsayı matrisi
    '''
    # Katsayı matrisinin boyutu kontrol edilir
    n = int(len(katsayiMat))
    if n != len(katsayiMat[0]):
        print("Katsayı matrisinin boyutu uyumlu değil.")
        return None
    # Eğer katsayı matrisi int verilirse float'a çevrilmesi gerekir, çünkü
    # LU ayrıştırma yapılırken katsayı matrisi ondalık sayı olabilir.
    katsayiMat= katsayiMat.astype(float)
    # L ve U matrisleri oluşturulur.
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    # LU ayrıştırma
    for k in range(0, n):
        L[k,k] = 1.0
        # U matrisi
        for j in range(k, n): 
            sum = 0.0
            for s in range(0, k):
                sum = sum + L[k,s]* U[s,j]
            U[k,j] = katsayiMat[k,j] - sum
        # L matrisi
        for i in range(k+1, n):
            sum = 0.0
            for s in range(0, k):
                sum = sum + L[i,s]* U[s,k]
            L[i,k] = (katsayiMat[i,k] - sum)/ U[k,k]
    return L, U
# LU Ayrıştırma Yöntemi Denklem Çözme
def LU_ayrisma_cozucu(katsayiMat, sonucVec):
    '''[Numerical Methods in Engineering with Python 3]
    LU ayrıştırma yöntemi ile denklem sistemini çözer.
    
    katsayiMat: Katsayı matrisi
    sonucVec: Sonuç vektörü
    '''
    # Katsayı matrisinin boyutu kontrol edilir
    n = int(len(katsayiMat))
    
    # LU ayrıştırma
    L, U= LU_ayrisma(katsayiMat)
    # Ax = b -> LUx = b -> Ly = b (Ux=y)
    # Önce Ly = b denklemi çözülür.
    
    # İleri yerine koyma fazı
    y = np.zeros(n)
    for k in range(0, n):
        y[k] = sonucVec[k]- np.dot(L[k,0:k], y[0:k])
    # Son olarak Ux = y denklemi çözülür.
    # Geri yerine koyma fazı
    cozumVek= np.zeros(n)
    for i in range(n-1, -1, -1):
        cozum= y[i]
        # Üst üçgensel formülde yerine koyma
        for j in range(i+1, n):
            cozum= cozum- U[i,j] * cozumVek[j]
        # Katsayı matrisinde doğrudan çözümü bulma
        cozumVek[i]= cozum/ U[i,i]
    return cozumVek
# LU Ayrıştırma Yöntemi Sistem Çözme
def LU_ayrisma_cozucu_sistem(katsayiMat, sonucMatrisi):
    '''[Numerical Methods in Engineering with Python 3]
    LU ayrıştırma yöntemi ile denklem sistemini çözer.
    
    katsayiMat: Katsayı matrisi
    sonucVec: Sonuç vektörü
    '''
    # Katsayı matrisinin boyutu kontrol edilir
    n= np.shape(sonucMatrisi)[0] #?
    no_of_eq= np.shape(sonucMatrisi)[1] #?
    cozumMat= np.zeros(np.shape(sonucMatrisi))
    katsayiMat_Temp= np.copy(katsayiMat)
    # LU ayrıştırma
    for it_noEq in range(no_of_eq):
        sonucVec= sonucMatrisi[:,it_noEq]
        katsayiMat= np.copy(katsayiMat_Temp)
        
        L, U= LU_ayrisma(katsayiMat)

        # İleri yerine koyma fazı
        y = np.zeros(n)
        for k in range(0, n):
            y[k] = sonucVec[k]- np.dot(L[k,0:k], y[0:k])
        # Son olarak Ux = y denklemi çözülür.
        # Geri yerine koyma fazı
        cozumVek= np.zeros(n)
        for i in range(n-1, -1, -1):
            cozum= y[i]
            # Üst üçgensel formülde yerine koyma
            for j in range(i+1, n):
                cozum= cozum- U[i,j] * cozumVek[j]
            # Katsayı matrisinde doğrudan çözümü bulma
            cozumVek[i]= cozum/ U[i,i]
        cozumMat[:,it_noEq]= cozumVek
    return cozumMat

# Gauss Eleme Yontemi - Ust ucgen forma getirerek - Geri Yerine koyma Iceren
def gauss_eleme_ust_ucgen(katsayiMat, sonucVec):
    '''[Numerical Methods in Engineering with Python 3]
    Gauss eleme yöntemi ile dogrusal denklem sisteminin çözümü bulur.
    
    coeffMat: Katsayı matrisi
    resultVec: Sonuç vektörü
    '''
    # Boyut
    n= len(sonucVec)
    if n != len(katsayiMat):
        print("Katsayı matrisi ve sonuç vektörünün boyutları uyumlu değil.")
        return None
    # Katsayı ve sonuç matrislerini float tipine çevir.
    katsayiMat= katsayiMat.astype(float)
    sonucVec= sonucVec.astype(float)
    # Üst üçgensel matris oluştur.
    for k in range(0, n-1): # k: pivot satırı
        for i in range(k+1, n): # i: pivot satırından sonraki satırlar
            #print(f"katsayiMat Once\n {katsayiMat}")
            if katsayiMat[i, k] != 0:
                lamb = katsayiMat[i, k]/ katsayiMat[k, k]
                #print(f"lamb: {lamb}")
                # Katsayı matrisini değiştir
                #print(f"i, k: {i}, {k}")
                #print(f"katsayiMat[i, k:n]: {katsayiMat[i, k:n]}")
                #print(f"lamb*katsayiMat[k, k:n]: {lamb*katsayiMat[k, k:n]}")
                #print(f"katsayiMat[i, k:n]- lamb* katsayiMat[k, k:n]: {katsayiMat[i, k:n]- lamb* katsayiMat[k, k:n]}")
                katsayiMat[i, :]= katsayiMat[i, :]- lamb* katsayiMat[k, :]
                # Sonuç vektörünü değiştir
                sonucVec[i]= sonucVec[i]- lamb* sonucVec[k]
            #print(f"katsayiMat Sonra\n {katsayiMat}")
    # Geri Yerine Koyma Yap
    cozumVek= np.zeros(n)
    # Son satırdan başlayarak geriye doğru ilerleme
    for i in range(n-1, -1, -1):
        cozum= sonucVec[i]
        # Üst üçgensel formülde yerine koyma
        for j in range(i+1, n):
            cozum= cozum- katsayiMat[i,j] * cozumVek[j]
        # Katsayı matrisinde doğrudan çözümü bulma
        cozumVek[i]= cozum/ katsayiMat[i,i]
    return cozumVek
# Gauss Eleme Yöntemi - Sistem - Üst üçgensel forma getirerek - Geri Yerine koyma Iceren
def gauss_eleme_ust_ucgen_sistem(katsayiMat, sonucMatrisi):
    # Boyut
    n= np.shape(sonucMatrisi)[0] #?
    no_of_eq= np.shape(sonucMatrisi)[1] #?
    if n != len(katsayiMat):
        print("Katsayı matrisi ve sonuç vektörünün boyutları uyumlu değil.")
        return None
    # Katsayı ve sonuç matrislerini float tipine çevir.
    katsayiMat= katsayiMat.astype(float)
    sonucMatrisi= sonucMatrisi.astype(float)
    cozumMat= np.zeros(np.shape(sonucMatrisi))
    katsayiMat_Temp= np.copy(katsayiMat)
    # Alt üçgensel matris oluştur.
    for it_noEq in range(no_of_eq):
        sonucVec= sonucMatrisi[:,it_noEq]
        katsayiMat= np.copy(katsayiMat_Temp)
        for k in range(0, n-1):
            for i in range(k+1, n):
                if katsayiMat[i, k] != 0:
                    lamb = katsayiMat[i, k]/ katsayiMat[k, k]
                    katsayiMat[i, :]= katsayiMat[i, :]- lamb* katsayiMat[k, :]
                    sonucVec[i]= sonucVec[i]- lamb* sonucVec[k]
        # İleri yerine koyma fazı
        print(katsayiMat)
        cozumVek= np.zeros(n)
        # İlk satırdan başlayarak ileriye doğru ilerleme
        for i in range(n-1, -1, -1):
            cozum= sonucVec[i]
            # Alt üçgensel formülde yerine koyma
            for j in range(i+1, n):
                cozum= cozum- katsayiMat[i,j] * cozumVek[j]
            # Katsayı matrisinde doğrudan çözümü bulma
            cozumVek[i]= cozum/ katsayiMat[i,i]
        cozumMat[:,it_noEq]= cozumVek
    return cozumMat
# Gauss Eleme Yöntemi - Alt üçgensel forma getirerek - İleri Yerine koyma Iceren
def gauss_eleme_alt_ucgen(katsayiMat, sonucVec):
    # Boyut
    n= len(sonucVec)
    if n != len(katsayiMat):
        print("Katsayı matrisi ve sonuç vektörünün boyutları uyumlu değil.")
        return None
    # Katsayı ve sonuç matrislerini float tipine çevir.
    katsayiMat= katsayiMat.astype(float)
    sonucVec= sonucVec.astype(float)
    # Alt üçgensel matris oluştur.
    for k in range(n-1, 0, -1): #? Ust Ucgensel Matris: for k in range(0, n-1):
        for i in range(k-1, -1, -1): #? Ust Ucgensel Matris: for i in range(k+1, n):
            #print(f"katsayiMat Once\n {katsayiMat}")
            if katsayiMat[i, k] != 0:
                lamb = katsayiMat[i, k]/ katsayiMat[k, k]
                katsayiMat[i, :]= katsayiMat[i, :]- lamb* katsayiMat[k, :]
                sonucVec[i]= sonucVec[i]- lamb* sonucVec[k]
            #print(f"katsayiMat Sonra\n {katsayiMat}")
    # İleri yerine koyma fazı
    cozumVek= np.zeros(n)
    # İlk satırdan başlayarak ileriye doğru ilerleme
    for i in range(0, n): #? Geri Yerine koyma: for i in range(n-1, -1, -1):
        cozum= sonucVec[i]
        # Alt üçgensel formülde yerine koyma
        for j in range(0, i): #? Geri Yerine koyma: for j in range(i+1, n):
            cozum= cozum- katsayiMat[i,j] * cozumVek[j]
        # Katsayı matrisinde doğrudan çözümü bulma
        cozumVek[i]= cozum/ katsayiMat[i,i]
    return cozumVek
# Gauss Eleme Yöntemi - Sistem - Alt üçgensel forma getirerek - İleri Yerine koyma Iceren
def gauss_eleme_alt_ucgen_sistem(katsayiMat, sonucMatrisi):
    # Boyut
    n= np.shape(sonucMatrisi)[0] #?
    no_of_eq= np.shape(sonucMatrisi)[1] #?
    if n != len(katsayiMat):
        print("Katsayı matrisi ve sonuç vektörünün boyutları uyumlu değil.")
        return None
    # Katsayı ve sonuç matrislerini float tipine çevir.
    katsayiMat= katsayiMat.astype(float)
    sonucMatrisi= sonucMatrisi.astype(float) #?
    cozumMat= np.zeros(np.shape(sonucMatrisi)) #?
    katsayiMat_Temp= np.copy(katsayiMat) #?
    # Alt üçgensel matris oluştur.
    for it_noEq in range(no_of_eq): #?
        sonucVec= sonucMatrisi[:,it_noEq] #?
        katsayiMat= np.copy(katsayiMat_Temp) #?
        for k in range(n-1, 0, -1):
            for i in range(k-1, -1, -1):
                if katsayiMat[i, k] != 0:
                    lamb = katsayiMat[i, k]/ katsayiMat[k, k]
                    katsayiMat[i, :]= katsayiMat[i, :]- lamb* katsayiMat[k, :]
                    sonucVec[i]= sonucVec[i]- lamb* sonucVec[k]
        print(katsayiMat)
        # İleri yerine koyma fazı
        cozumVek= np.zeros(n)
        # İlk satırdan başlayarak ileriye doğru ilerleme
        for i in range(0, n):
            cozum= sonucVec[i]
            # Alt üçgensel formülde yerine koyma
            for j in range(0, i):
                cozum= cozum- katsayiMat[i,j] * cozumVek[j]
            # Katsayı matrisinde doğrudan çözümü bulma
            cozumVek[i]= cozum/ katsayiMat[i,i]
        cozumMat[:,it_noEq]= cozumVek #?
    return cozumMat #?

# Matris Tersini Bulma - LU Ayrıştırma Yöntemi Kullanarak
def matris_tersi_al_LU(matris):
    '''
    LU ayrıştırma yöntemi ile katsayı matrisinin tersini hesaplar.
    '''
    # =================
    # Katsayı matrisinin boyutu kontrol edilir
    n = int(len(matris))
    # =================
    
    # =================
    matris_tersi = np.zeros((n,n))
    # =================

    # =================
    # LU ayrıştırma
    for i in range(n):
        matris_tersi[:,i] = LU_ayrisma_cozucu(matris, np.identity(n)[i]) #?
    # =================

    return matris_tersi
# Matris Tersini Bulma - Gauss Eleme Yöntemi Kullanarak
def matris_tersi_al_gauss(matris):
    '''
    LU ayrıştırma yöntemi ile katsayı matrisinin tersini hesaplar.
    '''
    # =================
    # Katsayı matrisinin boyutu kontrol edilir
    n = int(len(matris))
    # =================
    
    # =================
    matris_tersi = np.zeros((n,n))
    # =================

    # =================
    # LU ayrıştırma
    for i in range(n):
        matris_tersi[:,i] = gauss_eleme_alt_ucgen(matris, np.identity(n)[i]) #?
    # =================

    return matris_tersi

#! ===========================================
#! Python Alıştırma Fonksiyonları
#! ===========================================
# Faktöriyel Alma
def faktoriyel(sayi):
    if not isinstance(sayi, int):
        return False
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc

# 1'den n'e kadar olan sayıların toplamı
def topla(sayi):
    if not isinstance(sayi, int):
        return False
    sonuc = 0
    for i in range(1, sayi + 1):
        sonuc += i
    return sonuc

# En büyük ortak bölen
def obeb(sayi1, sayi2):
    if not isinstance(sayi1, int) or not isinstance(sayi2, int):
        return False
    buyukSayi= min(sayi1, sayi2)
    sonuc = 1
    for it in range(1, buyukSayi + 1):
        if sayi1 % it == 0 and sayi2 % it == 0:
            sonuc = it
    return sonuc

# En büyük ortak kat
def okek(sayi1, sayi2):
    if not isinstance(sayi1, int) or not isinstance(sayi2, int):
        return False
    return (sayi1/ obeb(sayi1, sayi2)) * (sayi2)

# Verilen sayilardan dik üçgen oluşturulabilir mi?
def dik_mi(sayi1, sayi2, sayi3):
    if not isinstance(sayi1, int) or not isinstance(sayi2, int) or not isinstance(sayi3, int):
        return False
    sirali_array= np.sort([sayi1, sayi2, sayi3])
    if sirali_array[0] ** 2 + sirali_array[1] ** 2 == sirali_array[2] ** 2:
        return True
    return False

# Matrislerin çarpımı
def mat_carp(mat1, mat2):
    boy1= np.shape(mat1)
    boy2= np.shape(mat2)
    if len(boy1) == 1:
        boy1= (1, boy1[0])
    if len(boy2) == 1:
        boy2= (1, boy2[0])
    if not isinstance(mat1, np.ndarray):
        return False
    if boy1[1] != boy2[0]:
        return False
    if np.array_equal(mat1, np.zeros(boy1)) or np.array_equal(mat2, np.zeros(boy2)):
        print("Bir matrisin tüm elemanları sıfırdır.")
        print(f"mat1:\n {mat1}")
        print(f"mat2:\n {mat2}")
        return np.zeros((boy1[1], boy2[0]))
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

# Dalga fonkiyonunun normalizasyonu
def normalize_et_dalgaFonk(arr1):
    if np.ndim(arr1) != 1:
        print("Bu fonksiyon sadece arrayler için çalışmaktadır.")
        return None
    sonuc= 0
    for it in arr1:
        sonuc += np.conj(it)* it
    normalizasyonKatsayisi= 1/np.sqrt(sonuc)
    return arr1* normalizasyonKatsayisi
