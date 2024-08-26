---
title: "Kümülatif Dağılım Fonksiyonu - Problem Cevapları"
---

## Problem 1

1. Rastgele 1000 adet normal dağılımda sayı üretin ve histogramını (bin=50 olsun) siyah olarak çizdirin.
2. Bu dağılımın yüzde 50'lik dilimine (`np.percentile()`) mavi bir çizgi (`plt.axvline()`) çizin.
3. Bu dağılımın ilk ve son çeyreğine düz yeşil bir çizgi çizin.
4. Kümülatif dağılım fonksiyonunu (`np.cumsum()`) çizdirin.

### Çözüm

```python
import numpy as np
import matplotlib.pyplot as plt

dagilim= np.random.randn(1000)
fig,ax= plt.subplots(figsize=(16,4))

#1
plt.hist(dagilim, bins=50,color="red")

#2
plt.axvline(np.percentile(dagilim, 50), color='blue', linewidth=2)

#3
plt.axvline(np.percentile(dagilim, 25), color='green', linewidth=2)
plt.axvline(np.percentile(dagilim, 75), color='green', linewidth=2)

# X ekseninde hangi nokta olacağını da göstermek için o noktaları x eksenine ekle
x_ticks = np.append(ax.get_xticks(), np.round(np.percentile(dagilim, 25), 2))
x_ticks = np.append(x_ticks, np.round(np.percentile(dagilim, 75),2))

# Yeni eklenmiş x eksenini belirle
ax.set_xticks(x_ticks)

plt.show()
plt.close()

#4
# PMF
fig, ax = plt.subplots(2, figsize=(16,8))
ax[0].hist(dagilim, bins=30, density=True, color='black')
ax[0].set_title('PMF')

# CDF
counts, bin_edges = np.histogram(dagilim, bins=50, density=True)
cdf = np.cumsum(counts)
ax[1].plot(bin_edges[1:], cdf/cdf[-1], color='black', lw=4)
ax[1].set_title('CDF')

# ========== MAKYAJ ==========
y_ticks = np.append(ax[1].get_yticks(), [0.25, 0.5, 0.75])
ax[1].set_yticks(y_ticks)
ax[1].set_ylim(-0.05,1.05)
ax[1].set_xlim(-3.05,3.05)
# Find closest to y=0.25
closest_index = np.argmin(np.abs(cdf/cdf[-1] - 0.25))
closest_value = bin_edges[closest_index+1]
# Put a dot on the closest point
ax[1].axvline(closest_value, ymax=0.25, color='green', linewidth=2)
ax[1].axhline(0.25, xmax=1, color='green',ls='--', alpha=0.5)
# Find closest to y=0.5
closest_index = np.argmin(np.abs(cdf/cdf[-1] - 0.5))
closest_value = bin_edges[closest_index+1]
# Put a dot on the closest point
ax[1].axvline(closest_value, ymax=0.5, color='blue', linewidth=2)
ax[1].axhline(0.5, xmax=1, color='blue',ls='--', alpha=0.5)
# Find closest to y=0.75
closest_index = np.argmin(np.abs(cdf/cdf[-1] - 0.75))
closest_value = bin_edges[closest_index+1]
# Put a dot on the closest point
ax[1].axvline(closest_value, ymax=0.75, color='green', linewidth=2)
ax[1].axhline(0.75, xmax=1, color='green',ls='--', alpha=0.5)
# X ekseninde hangi nokta olacağını da göstermek için o noktaları x eksenine ekle
x_ticks = np.append(ax[1].get_xticks(), np.round(np.percentile(dagilim, 25), 2))
#x_ticks = np.append(x_ticks, np.round(np.percentile(dagilim, 50),2))
x_ticks = np.append(x_ticks, np.round(np.percentile(dagilim, 75),2))
# Yeni eklenmiş x eksenini belirle
ax[1].set_xticks(x_ticks)
# ========== MAKYAJ ==========

plt.show()
plt.close()
```