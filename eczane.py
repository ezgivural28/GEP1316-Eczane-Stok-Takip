"""Eczane stok ve son kullanma tarihi takip mini uygulamasi."""
from datetime import date, datetime
import csv

ilaclar = []

def pozitif_tamsayi_oku(mesaj, sifir_olabilir=True):
    while True:
        try:
            deger = int(input(mesaj))
            if deger < 0 or (deger == 0 and not sifir_olabilir):
                print('Uyari: Gecerli bir pozitif sayi giriniz.')
                continue
            return deger
        except ValueError:
            print('Uyari: Lutfen tam sayi giriniz.')

def tarih_oku(mesaj):
    while True:
        try:
            return datetime.strptime(input(mesaj).strip(), '%Y-%m-%d').date()
        except ValueError:
            print('Uyari: Tarihi YYYY-AA-GG biciminde giriniz.')

def durum_hesapla(ilac, bugun=None):
    bugun = bugun or date.today()
    kalan = (ilac['son_tarih'] - bugun).days
    if kalan < 0:
        tarih_durumu = 'SURESI DOLMUS'
    elif kalan <= 30:
        tarih_durumu = '30 GUN ICINDE'
    else:
        tarih_durumu = 'NORMAL'
    if ilac['stok'] == 0:
        stok_durumu = 'STOK YOK'
    elif ilac['stok'] <= ilac['minimum']:
        stok_durumu = 'KRITIK STOK'
    else:
        stok_durumu = 'YETERLI'
    return tarih_durumu, stok_durumu, kalan

def ilac_ekle():
    while True:
        ad = input('Ilac adi: ').strip()
        if ad:
            break
        print('Uyari: Ilac adi bos olamaz.')
    stok = pozitif_tamsayi_oku('Stok adedi: ')
    minimum = pozitif_tamsayi_oku('Minimum stok adedi: ')
    son_tarih = tarih_oku('Son kullanma tarihi (YYYY-AA-GG): ')
    ilaclar.append({'ad': ad, 'stok': stok, 'minimum': minimum, 'son_tarih': son_tarih})
    print('Ilac kaydedildi.')

def rapor_satirlari():
    satirlar = []
    for ilac in ilaclar:
        tarih_durumu, stok_durumu, kalan = durum_hesapla(ilac)
        satirlar.append([ilac['ad'], ilac['stok'], ilac['minimum'], ilac['son_tarih'].isoformat(), kalan, tarih_durumu, stok_durumu])
    return satirlar

def rapor_goster():
    if not ilaclar:
        print('Kayitli ilac bulunmuyor.')
        return
    print(f"{'ILAC':20} {'STOK':>5} {'MIN':>5} {'SKT':12} {'GUN':>6} {'TARIH DURUMU':17} STOK DURUMU")
    for ad, stok, minimum, skt, kalan, tarih_durumu, stok_durumu in rapor_satirlari():
        print(f'{ad[:20]:20} {stok:>5} {minimum:>5} {skt:12} {kalan:>6} {tarih_durumu:17} {stok_durumu}')

def rapor_kaydet(dosya='eczane_raporu.csv'):
    with open(dosya, 'w', encoding='utf-8-sig', newline='') as f:
        yazici = csv.writer(f)
        yazici.writerow(['Ilac', 'Stok', 'Minimum', 'SKT', 'Kalan gun', 'Tarih durumu', 'Stok durumu'])
        yazici.writerows(rapor_satirlari())
    print(f'Rapor kaydedildi: {dosya}')

def main():
    while True:
        print('\n1- Ilac ekle | 2- Rapor goster | 3- CSV kaydet | 4- Cikis')
        secim = input('Secim: ').strip()
        if secim == '1':
            ilac_ekle()
        elif secim == '2':
            rapor_goster()
        elif secim == '3':
            rapor_kaydet()
        elif secim == '4':
            print('Program kapatildi.')
            break
        else:
            print('Uyari: 1-4 arasinda secim yapiniz.')

if __name__ == '__main__':
    main()
