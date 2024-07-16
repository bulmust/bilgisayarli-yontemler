## Hızlı Ters Karekök Alma Algoritması (Fast Inverse Square Root)

90'lı yıllarda "3 boyutlu" fps (first person shooter) alanındaki bilgisayar oyunları yapılarken hız konusunda büyük zorluklar yaşanıyordu. Zamanın bilgisayarları, yapay 3 boyut yaratmak için sık sık kullanılan $1/\sqrt{x}$ işlemini çok kez yapmaya uygun değildi.

Bu sorunu aşmak için  3dfx Interactive firması, Quake oyununun fizik motorunu hızlandırmak için daha önceden keşfedilen Hızlı Ters Karekök alma algoritmasını kullandı. O zamanlarda çok popüler olan Doom gibi oyunlara kıyasla Quake oyunda inanılmaz bir hızlanma elde ettiler. Bu algoritma üç boyutlu grafiklere sahip bilgisayar oyunlarında çok önemli bir yere sahiptir.

## Linkler

1. İngilizce wikipedia sayfası: <https://en.wikipedia.org/wiki/Fast_inverse_square_root>
   - Bu sayfada algoritmanın nasıl çalıştığı anlatılmakta ve C kodlama dili ile yazılmış fonksiyonu bulunmaktadır.
2. Python kod örneği: <https://ajcr.net/fast-inverse-square-root-python/>
3. Algoritma hakkında makale: <https://mrober.io/papers/rsqrt.pdf>
4. Quake III Arena kaynak kod içerisinde bulunan hızlı ters karekök alma algoritması: <https://archive.softwareheritage.org/swh:1:cnt:bb0faf6919fc60636b2696f32ec9b3c2adb247fe;origin=https://github.com/id-Software/Quake-III-Arena;visit=swh:1:snp:4ab9bcef131aaf449a7c01370aff8c91dcecbf5f;anchor=swh:1:rev:dbe4ddb10315479fc00086f08e25d968b4b43c49;path=/code/game/q_math.c;lines=549-572>
5. Algoritmayı açıklayan ayrıntılı video: <https://www.youtube.com/watch?v=p8u_k2LIZyo>

## Yapılacaklar

Aşağıdaki maddelere yeni eklemeler yapabilirsiniz, sırasını değiştirebilirsiniz ancak silemezsiniz.

- [ ] Hızlı Ters Karekök Alma algoritmasının nasıl çalıştığı anlaşılacak.
- [ ] Hızlı Ters Karekök Alma algoritması Python ile yazılacak.
- [ ] Diğer paketlerdeki örnekleri ile karşılaştırılarak hız testi yapılacak.
  - [ ] Numpy paketi kullanılarak hız denemesi yapılacak. Numpy paketinde hangi algoritma kullanılıyor belirlenecek.
  - [ ] Başka hangi paketler kullanılabilir araştırılacak. İlgili paketin algoritmasına bakılacak ve hız denemeleri yapılacak
- [ ] Sunum hazırlanacak.
- [ ] Derste sunulacak.