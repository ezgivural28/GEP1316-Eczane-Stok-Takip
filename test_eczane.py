import unittest
from datetime import date
from unittest.mock import patch
import eczane

class TestEczane(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(eczane.durum_hesapla({'son_tarih':date(2030, 12, 31),'stok':20,'minimum':5},date(2030,1,1))[:2], ('NORMAL','YETERLI'))
    def test_son_gun(self):
        self.assertEqual(eczane.durum_hesapla({'son_tarih':date(2030,1,1),'stok':5,'minimum':5},date(2030,1,1))[:2], ('30 GUN ICINDE','KRITIK STOK'))
    def test_suresi_dolmus(self):
        self.assertEqual(eczane.durum_hesapla({'son_tarih':date(2029,12,31),'stok':1,'minimum':5},date(2030,1,1))[0], 'SURESI DOLMUS')
    def test_stok_sifir(self):
        self.assertEqual(eczane.durum_hesapla({'son_tarih':date(2031,1,1),'stok':0,'minimum':5},date(2030,1,1))[1], 'STOK YOK')
    def test_hatalı_sayi(self):
        with patch('builtins.input',side_effect=['abc','-3','4']):
            self.assertEqual(eczane.pozitif_tamsayi_oku('Stok: '),4)
    def test_hatalı_tarih(self):
        with patch('builtins.input',side_effect=['2030-02-30','2030-03-01']):
            self.assertEqual(eczane.tarih_oku('SKT: '),date(2030,3,1))
    def test_bos_ad(self):
        eczane.ilaclar.clear()
        with patch('builtins.input',side_effect=['','Ornek Ilac','3','2','2030-03-01']):
            eczane.ilac_ekle()
        self.assertEqual(eczane.ilaclar[0]['ad'],'Ornek Ilac')

if __name__ == '__main__':
    unittest.main()
