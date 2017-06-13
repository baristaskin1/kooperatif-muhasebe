from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Birim(models.Model):
	birim_adi = models.CharField(max_length=50)
	def __str__(self):
		return self.birim_adi

class GiderTipi(models.Model):
	gider_adi = models.CharField(max_length=50)
	def __str__(self):
		return self.gider_adi

class StokHareketiTipi(models.Model):
	stok_hareket_tipi_adi = models.CharField(max_length=50)
	def __str__(self):
		return self.stok_hareket_tipi_adi

class UrunKategorisi(models.Model):
	urun_kategori_adi = models.CharField(max_length=50)
	def __str__(self):
		return self.urun_kategori_adi
		
###

class uretici(models.Model):
	uretici_adi = models.CharField(max_length=200)
	adres = models.CharField(max_length=500)
	banka_bilgileri = models.CharField(max_length=500)
	kullanici = models.ForeignKey(User)
	tarih = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.uretici_adi
	


class urun(models.Model):
	urun_kategorisi = models.ForeignKey(UrunKategorisi)
	urun_adi = models.CharField(max_length=200)
	uretici = models.ForeignKey(uretici)
	uye_fiyati = models.DecimalField(null=True,  max_digits=7,decimal_places=2)
	musteri_fiyati = models.DecimalField(null=True,   max_digits=7,decimal_places=2)
	birim = models.ForeignKey(Birim, null=True)
	kdv_orani = models.IntegerField(null=True)	
	dayanisma_urunu = models.BooleanField()
	
	def __str__(self):
		return self.urun_adi
		
class Gider(models.Model):
	tarih  = models.DateTimeField()
	gider_tipi = models.ForeignKey(GiderTipi)
	tutar = models.DecimalField(null=True,  max_digits=7,decimal_places=2)
	notlar = models.CharField(max_length=500)

class StokGirisi(models.Model):
	stok_hareketi_tipi = models.ForeignKey(StokHareketiTipi)
	tarih = models.DateTimeField()
	urun = models.ForeignKey(urun)
	miktar = models.IntegerField()
	agirlik = models.DecimalField(null=True,  max_digits=5,decimal_places=2)
	notlar = models.CharField(max_length=500)
	
class Satis(models.Model):
	tarih = models.DateTimeField()
	kullanici = models.ForeignKey(User)
	def __str__(self):
		return str(self.tarih)

class SatisStokHareketleri(models.Model):
	satis = models.ForeignKey(Satis, on_delete=models.CASCADE)
	urun = models.ForeignKey(urun)
	miktar = models.IntegerField()
	tutar = models.DecimalField(null=True,   max_digits=7,decimal_places=2)	
	def __str__(self):
		return self.urun

class VirmanVeDuzeltmeHesaplari(models.Model):
	hesap_adi = models.CharField(max_length=50)
	def __str__(self):
		return self.hesap_adi
		
class VirmanVeDuzeltme(models.Model):
	tarih  = models.DateTimeField()
	cikis_hesabi = models.ForeignKey(VirmanVeDuzeltmeHesaplari, related_name='cikis_hesabi', null=True)
	giris_hesabi = models.ForeignKey(VirmanVeDuzeltmeHesaplari, related_name='giris_hesabi', null=True)
	tutar = models.DecimalField(max_digits=7,decimal_places=2)	
	notlar = models.CharField(max_length=500)
	kullanici = models.ForeignKey(User, null=True)
	