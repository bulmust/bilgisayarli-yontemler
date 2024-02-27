# Bilgisayarlı Yöntemler

Çeşitli kaynaklardan derlenerek hazırlanan sayısal yöntem veya bilgisayarlı yöntemler notlarını içerir.

## İçerik

## Quarto Detayları

### Kurulum

Quarto kurulumu için aşağıdaki siteyi ziyaret edebilirsiniz.

[Quarto ile başlama, https://quarto.org/docs/get-started/](https://quarto.org/docs/get-started/)

Bu repo VS Code kullanılarak hazırlanmıştır.

### Metadata

Tüm `md` dosyalarında aşağıdaki metadata yaml bloğu kullanılmalıdır. Örneğin

```markdown
---
title: "Başlık Adı"
author: "Taygun Bulmus"
bibliography: refereanslar.bib
toc: true
number-sections: true
highlight-style: pygments
format: 
  html: 
    code-fold: true
    html-math-method: katex
  pdf: 
    geometry: 
      - top=30mm
      - left=20mm
  docx: default
jupyter: python3
---

```
### İçerik (Markdown)

#### Belirtme Çizgileri (callouts)

`note`, `tip`, `warning`, `caution`, ve `important` olmak üzere 5 farklı belirtme çizgisi kullanılabilir. Kullanım şekli `::: {.callout-tip}` şeklinde başlanır ve `:::` ile biter. Burada tip yerine `note`, `tip`, `warning`, `caution`, ve `important` yazabilirsiniz.

```markdown
::: {.callout-note}
Not 1
:::
```

#### Başlık

Başlıklar `#` işareti ile belirtilir. `#` sayısı arttıkça başlık seviyesi azalır. Başıklara alıntı yapılabilir. Örneğin  `## Plot {#sec-etiket}` plot başlığına alıntı yapmak için `@sec-etiket` şeklinde kullanılabilir.


#### Matematiksel İfadeler

Matematiksel ifadeler için `$$` arasında yazılmalıdır. Sondaki dolar işaretinin yanına ` {#eq-etiket}` şeklinde etiket verilebilir. Bu etiketleri metin içerisinde `@eq-etiket` şeklinde alıntı yapabilirsiniz. Metinde **Equation 1**

```markdown
$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$ {#eq-etiket}
```

#### Alıntı ve Referans 

Başlık (header) dosyasında belirtilen (`bibliography: refereanslar.bib`) `bib` dosyasındaki referanslar `[@taygun1988]` şeklinde kullanılabilir. Bu referanslar en altta otomatik olarak oluşturulur.


```
## Bilgiler

Taygun'un 1988'deki makalesinde matematiksel yöntemlerin öneminden bahsetmiştir. [@taygun1988].

## Referanslar

```

### Kod Bloğu

Ref: [Quarto Code Cells: Jupyter](https://quarto.org/docs/reference/cells/cells-jupyter.html)

#### Multiple Figures

```python
#| label: fig-gapminder
#| fig-cap: "Big Caption"
#| fig-subcap:
#|   - "Figure 1 Caption"
#|   - "Figure 2 Caption"
#| layout-ncol: 2
#| column: page

import matplotlib.pyplot as plt
```
