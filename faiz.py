def hesaplamayi_yap(ana_para, faiz_orani, yil):
    gelecekteki_deger = ana_para / ((1 + faiz_orani) ** yil)
    return gelecekteki_deger

def tam_tersi_hesapla(gelecekteki_deger, faiz_orani, yil):
    bugunku_deger = gelecekteki_deger * ((1 + faiz_orani) ** yil)
    return bugunku_deger

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