# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TwTowar(models.Model):
    tw_id = models.IntegerField(db_column='tw_Id', primary_key=True)  # Field name made lowercase.
    tw_zablokowany = models.BooleanField(db_column='tw_Zablokowany')  # Field name made lowercase.
    tw_rodzaj = models.IntegerField(db_column='tw_Rodzaj')  # Field name made lowercase.
    tw_symbol = models.CharField(db_column='tw_Symbol', max_length=20)  # Field name made lowercase.
    tw_nazwa = models.CharField(db_column='tw_Nazwa', max_length=50)  # Field name made lowercase.
    tw_opis = models.CharField(db_column='tw_Opis', max_length=255)  # Field name made lowercase.
    tw_idvatsp = models.ForeignKey('SlStawkavat', models.DO_NOTHING, db_column='tw_IdVatSp', blank=True, null=True)  # Field name made lowercase.
    tw_idvatzak = models.ForeignKey('SlStawkavat', models.DO_NOTHING, db_column='tw_IdVatZak', blank=True, null=True)  # Field name made lowercase.
    tw_jakprzysp = models.BooleanField(db_column='tw_JakPrzySp')  # Field name made lowercase.
    tw_jednmiary = models.CharField(db_column='tw_JednMiary', max_length=10)  # Field name made lowercase.
    tw_pkwiu = models.CharField(db_column='tw_PKWiU', max_length=20)  # Field name made lowercase.
    tw_sww = models.CharField(db_column='tw_SWW', max_length=20)  # Field name made lowercase.
    tw_idrabat = models.ForeignKey('SlRabat', models.DO_NOTHING, db_column='tw_IdRabat', blank=True, null=True)  # Field name made lowercase.
    tw_idopakowanie = models.ForeignKey('self', models.DO_NOTHING, db_column='tw_IdOpakowanie', blank=True, null=True)  # Field name made lowercase.
    tw_przezwartosc = models.BooleanField(db_column='tw_PrzezWartosc')  # Field name made lowercase.
    tw_idpodstdostawca = models.ForeignKey('KhKontrahent', models.DO_NOTHING, db_column='tw_IdPodstDostawca', blank=True, null=True)  # Field name made lowercase.
    tw_dostsymbol = models.CharField(db_column='tw_DostSymbol', max_length=20)  # Field name made lowercase.
    tw_czasdostawy = models.IntegerField(db_column='tw_CzasDostawy', blank=True, null=True)  # Field name made lowercase.
    tw_urznazwa = models.CharField(db_column='tw_UrzNazwa', max_length=50)  # Field name made lowercase.
    tw_plu = models.IntegerField(db_column='tw_PLU', blank=True, null=True)  # Field name made lowercase.
    tw_podstkodkresk = models.CharField(db_column='tw_PodstKodKresk', max_length=20)  # Field name made lowercase.
    tw_idtypkodu = models.IntegerField(db_column='tw_IdTypKodu', blank=True, null=True)  # Field name made lowercase.
    tw_cenaotwarta = models.BooleanField(db_column='tw_CenaOtwarta')  # Field name made lowercase.
    tw_wagaetykiet = models.BooleanField(db_column='tw_WagaEtykiet', blank=True, null=True)  # Field name made lowercase.
    tw_kontrolatw = models.BooleanField(db_column='tw_KontrolaTW')  # Field name made lowercase.
    tw_stanmin = models.DecimalField(db_column='tw_StanMin', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_jednstanmin = models.CharField(db_column='tw_JednStanMin', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tw_dniwaznosc = models.IntegerField(db_column='tw_DniWaznosc', blank=True, null=True)  # Field name made lowercase.
    tw_idgrupa = models.ForeignKey('SlGrupatw', models.DO_NOTHING, db_column='tw_IdGrupa', blank=True, null=True)  # Field name made lowercase.
    tw_www = models.CharField(db_column='tw_WWW', max_length=255)  # Field name made lowercase.
    tw_sklepinternet = models.BooleanField(db_column='tw_SklepInternet')  # Field name made lowercase.
    tw_pole1 = models.CharField(db_column='tw_Pole1', max_length=50)  # Field name made lowercase.
    tw_pole2 = models.CharField(db_column='tw_Pole2', max_length=50)  # Field name made lowercase.
    tw_pole3 = models.CharField(db_column='tw_Pole3', max_length=50)  # Field name made lowercase.
    tw_pole4 = models.CharField(db_column='tw_Pole4', max_length=50)  # Field name made lowercase.
    tw_pole5 = models.CharField(db_column='tw_Pole5', max_length=50)  # Field name made lowercase.
    tw_pole6 = models.CharField(db_column='tw_Pole6', max_length=50)  # Field name made lowercase.
    tw_pole7 = models.CharField(db_column='tw_Pole7', max_length=50)  # Field name made lowercase.
    tw_pole8 = models.CharField(db_column='tw_Pole8', max_length=50)  # Field name made lowercase.
    tw_uwagi = models.CharField(db_column='tw_Uwagi', max_length=255)  # Field name made lowercase.
    tw_logo = models.TextField(db_column='tw_Logo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tw_usuniety = models.BooleanField(db_column='tw_Usuniety')  # Field name made lowercase.
    tw_objetosc = models.DecimalField(db_column='tw_Objetosc', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_masa = models.DecimalField(db_column='tw_Masa', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_charakter = models.TextField(db_column='tw_Charakter', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tw_jednmiaryzak = models.CharField(db_column='tw_JednMiaryZak', max_length=10)  # Field name made lowercase.
    tw_jmzakinna = models.BooleanField(db_column='tw_JMZakInna')  # Field name made lowercase.
    tw_kodtowaru = models.CharField(db_column='tw_KodTowaru', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tw_idkrajupochodzenia = models.ForeignKey('SlKrajpochodzenia', models.DO_NOTHING, db_column='tw_IdKrajuPochodzenia', blank=True, null=True)  # Field name made lowercase.
    tw_idujm = models.IntegerField(db_column='tw_IdUJM', blank=True, null=True)  # Field name made lowercase.
    tw_jednmiarysprz = models.CharField(db_column='tw_JednMiarySprz', max_length=10)  # Field name made lowercase.
    tw_jmsprzinna = models.BooleanField(db_column='tw_JMSprzInna')  # Field name made lowercase.
    tw_serwisaukcyjny = models.BooleanField(db_column='tw_SerwisAukcyjny')  # Field name made lowercase.
    tw_idproducenta = models.ForeignKey('KhKontrahent', models.DO_NOTHING, db_column='tw_IdProducenta', blank=True, null=True)  # Field name made lowercase.
    tw_sprzedazmobilna = models.BooleanField(db_column='tw_SprzedazMobilna')  # Field name made lowercase.
    tw_isfundpromocji = models.BooleanField(db_column='tw_IsFundPromocji', blank=True, null=True)  # Field name made lowercase.
    tw_idfundpromocji = models.IntegerField(db_column='tw_IdFundPromocji', blank=True, null=True)  # Field name made lowercase.
    tw_domyslnakategoria = models.IntegerField(db_column='tw_DomyslnaKategoria', blank=True, null=True)  # Field name made lowercase.
    tw_wysokosc = models.DecimalField(db_column='tw_Wysokosc', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_szerokosc = models.DecimalField(db_column='tw_Szerokosc', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_glebokosc = models.DecimalField(db_column='tw_Glebokosc', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_stanmaks = models.DecimalField(db_column='tw_StanMaks', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_akcyza = models.BooleanField(db_column='tw_Akcyza')  # Field name made lowercase.
    tw_akcyzazaznacz = models.BooleanField(db_column='tw_AkcyzaZaznacz')  # Field name made lowercase.
    tw_akcyzakwota = models.DecimalField(db_column='tw_AkcyzaKwota', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_obrotmarza = models.BooleanField(db_column='tw_ObrotMarza')  # Field name made lowercase.
    tw_odwrotneobciazenie = models.BooleanField(db_column='tw_OdwrotneObciazenie')  # Field name made lowercase.
    tw_progkwotowyoo = models.IntegerField(db_column='tw_ProgKwotowyOO')  # Field name made lowercase.
    tw_dodawalnydozw = models.BooleanField(db_column='tw_DodawalnyDoZW')  # Field name made lowercase.
    tw_isbn = models.CharField(max_length=255, blank=True, null=True)
    tw_bloz_7 = models.CharField(max_length=255, blank=True, null=True)
    tw_bloz_12 = models.CharField(max_length=255, blank=True, null=True)
    tw_koduproducenta = models.CharField(db_column='tw_KodUProducenta', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tw_komunikat = models.CharField(db_column='tw_Komunikat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tw_komunikatod = models.DateTimeField(db_column='tw_KomunikatOd', blank=True, null=True)  # Field name made lowercase.
    tw_komunikatdokumenty = models.IntegerField(db_column='tw_KomunikatDokumenty')  # Field name made lowercase.
    tw_mechanizmpodzielonejplatnosci = models.BooleanField(db_column='tw_MechanizmPodzielonejPlatnosci')  # Field name made lowercase.
    tw_grupajpkvat = models.IntegerField(db_column='tw_GrupaJpkVat')  # Field name made lowercase.
    tw_oplcukrowapodlega = models.BooleanField(db_column='tw_OplCukrowaPodlega')  # Field name made lowercase.
    tw_oplcukrowaobj = models.DecimalField(db_column='tw_OplCukrowaObj', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_oplcukrowazawartosccukru = models.DecimalField(db_column='tw_OplCukrowaZawartoscCukru', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_oplcukrowainneslodzace = models.BooleanField(db_column='tw_OplCukrowaInneSlodzace')  # Field name made lowercase.
    tw_oplcukrowasok = models.BooleanField(db_column='tw_OplCukrowaSok')  # Field name made lowercase.
    tw_oplcukrowakwota = models.DecimalField(db_column='tw_OplCukrowaKwota', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_oplcukrowakofeinapodlega = models.BooleanField(db_column='tw_OplCukrowaKofeinaPodlega')  # Field name made lowercase.
    tw_oplcukrowakofeinakwota = models.DecimalField(db_column='tw_OplCukrowaKofeinaKwota', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_oplcukrowanapojweglelektr = models.BooleanField(db_column='tw_OplCukrowaNapojWeglElektr')  # Field name made lowercase.
    tw_oplcukrowakwotapowyzej = models.DecimalField(db_column='tw_OplCukrowaKwotaPowyzej', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_datazmianyvatsprzedazy = models.DateTimeField(db_column='tw_DataZmianyVatSprzedazy', blank=True, null=True)  # Field name made lowercase.
    tw_masanetto = models.DecimalField(db_column='tw_MasaNetto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tw_idkoduwyrobuakcyzowego = models.ForeignKey('SlKodwyrobuakcyzowego', models.DO_NOTHING, db_column='tw_IdKoduWyrobuAkcyzowego', blank=True, null=True)  # Field name made lowercase.
    tw_akcyzamarkawyrobow = models.CharField(db_column='tw_AkcyzaMarkaWyrobow', max_length=350)  # Field name made lowercase.
    tw_akcyzawielkoscproducenta = models.CharField(db_column='tw_AkcyzaWielkoscProducenta', max_length=15)  # Field name made lowercase.
    tw_znakiakcyzy = models.IntegerField(db_column='tw_ZnakiAkcyzy', blank=True, null=True)  # Field name made lowercase.
    tw_wegielpodlegaoswiadczeniu = models.BooleanField(db_column='tw_WegielPodlegaOswiadczeniu')  # Field name made lowercase.
    tw_wegielopispochodzenia = models.CharField(db_column='tw_WegielOpisPochodzenia', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tw__Towar'


class TwStan(models.Model):
    st_towid = models.OneToOneField(TwTowar, models.DO_NOTHING, db_column='st_TowId', primary_key=True)  # Field name made lowercase.
    st_magid = models.ForeignKey('SlMagazyn', models.DO_NOTHING, db_column='st_MagId')  # Field name made lowercase.
    st_stan = models.DecimalField(db_column='st_Stan', max_digits=19, decimal_places=4)  # Field name made lowercase.
    st_stanmin = models.DecimalField(db_column='st_StanMin', max_digits=19, decimal_places=4)  # Field name made lowercase.
    st_stanrez = models.DecimalField(db_column='st_StanRez', max_digits=19, decimal_places=4)  # Field name made lowercase.
    st_stanmax = models.DecimalField(db_column='st_StanMax', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tw_Stan'
        unique_together = (('st_towid', 'st_magid'), ('st_towid', 'st_magid'),)


class TwZdjecietw(models.Model):
    zd_id = models.IntegerField(db_column='zd_Id', primary_key=True)  # Field name made lowercase.
    zd_idtowar = models.ForeignKey(TwTowar, models.DO_NOTHING, db_column='zd_IdTowar')  # Field name made lowercase.
    zd_zdjecie = models.BinaryField(db_column='zd_Zdjecie', blank=True, null=True)  # Field name made lowercase.
    zd_glowne = models.BooleanField(db_column='zd_Glowne')  # Field name made lowercase.
    zd_crc = models.IntegerField(db_column='zd_CRC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tw_ZdjecieTw'
