# Koşullu yaş örneği
"""
sayi1=int(input('Lütfen bir sayı giriniz:'))

print('Yaşınız: ',sayi1)
if sayi1>18:
    print('Giriş hakkınız vardır.')
elif sayi1==18:
    print('Giriş hakkınız vardır.')
else:
    print('Giremezsiniz!')
"""

# Koşullu hava durumu örneği
"""
print('(güneşli/karlı/yağmurlu)')
rapor=input('Bugün hava nasıl?:')
if rapor=='güneşli'or rapor=='Güneşli':
    print('Bugün hava güneşli.')
elif rapor=='karlı'or rapor=='Karlı':
    print('Bugün hava karlı.')
elif rapor=='yağmurlu'or rapor=='Yağmurlu':
    print('Bugün hava yağmurlu.')
else:
    print('Böyle bir hava durumu bulunamadı.')
"""

# Kullanıcı giriş örneği
"""
kullaniciadi = input('Kullanıcı adınızı girin:')
parola = input('Parolanızı girin:')

karar = input('Giriş yapmak istiyorsanız G, çıkış yapmak için Ç harfine basınız:')
if karar == 'G':
    kullaniciadi2 = input('Kullanıcı Adı:')
    parola1 = input('Parola:')
    if kullaniciadi == kullaniciadi2 and parola == parola1:
        print('Giriş yapıldı.')
    elif kullaniciadi != kullaniciadi2:
        print('KULLANICI ADI HATALI.')
    elif parola != parola1:
        print('PAROLA HATALI.')
    else:
        print('KULLANICI ADI VE PAROLA HATALI!')
elif karar == 'Ç':
    print('Çıkış yapıldı.')
else:
    print('Hatalı yazım.')
"""

