

# Faiz Hesaplama

Bu proje, ana paranın faiz oranı ve belirli bir süre dikkate alınarak gelecekteki değerini veya bugünkü değerini hesaplayan bir hesaplama programıdır.

## Kullanım

1. Ana para miktarını, faiz oranını ve hesaplama yapmak istediğiniz yılı girin.

2. Gelecekteki değeri mi yoksa bugünkü değeri mi hesaplamak istediğinizi belirtin. Gelecekteki değer için 'G' veya 'g', bugünkü değer için 'B' veya 'b' girin.

3. Program, hesaplama sonuçlarını ekranda gösterecektir.

Örnek:

```python
ana_para = float(input("Ana para miktarını girin: "))
faiz_orani = float(input("Faiz oranını girin (örneğin %20 için 0.20): "))
yil = int(input("Kaç yıl sonra hesaplama yapmak istediğinizi girin: "))

secim = input("Gelecekteki değeri mi yoksa bugünkü değeri mi hesaplamak istersiniz? (Gelecekteki değer için 'G', Bugünkü değer için 'B' girin): ")

if secim == "G" or secim == "g":
    gelecekteki_deger = hesaplamayi_yap(ana_para, faiz_orani, yil)
    print(f"{yil} yıl sonra elinizdeki para miktarı: {gelecekteki_deger:.2f} TL")
elif secim == "B" or secim == "b":
    gelecekteki_deger = hesaplamayi_yap(ana_para, faiz_orani, yil)
    bugunku_deger = tam_tersi_hesapla(gelecekteki_deger, faiz_orani, yil)
    print(f"{yil} yıl sonra elde etmek istediğiniz para miktarı: {gelecekteki_deger:.2f} TL")
    print(f"Bugünkü değeri: {bugunku_deger:.2f} TL")
else:
    print("Geçersiz seçim yapıldı.")

```
## Lisans

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu projeyi [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisansladık. Lisansın tam açıklamasını burada bulabilirsiniz.

