from django.db import models


# Model towarów
class Towar(models.Model):
    tw_Id = models.IntegerField(db_column='tw_Id', primary_key=True)
    tw_Nazwa = models.CharField(db_column='tw_Nazwa', max_length=45, blank=False)
    tw_Symbol = models.CharField(db_column='tw_Symbol', max_length=13, blank=False)
    tw_PodstKodKresk = models.CharField(db_column='tw_PodstKodKresk', max_length=20, blank=True)

    #
    class Meta:
        managed = True
        db_table = 'tw__Towar'

    def __str__(self):
        return self.tw_Symbol, self.tw_Nazwa, self.tw_PodstKodKresk


class Stan(models.Model):
    st_TowId = models.IntegerField(db_column='st_TowId', primary_key=True)
    st_MagId = models.IntegerField(db_column='st_MagId', blank=False)
    st_Stan = models.FloatField(db_column='st_Stan', max_length=8, blank=False, )

    class Meta:
        managed = True
        db_table = 'tw_Stan'

    def __str__(self):
        return self.st_Stan


class Magazyn(models.Model):
    mag_Id = models.ManyToManyField(to='Stan')
    mag_Nazwa = models.CharField(max_length=50, blank=False)

    class Meta:
        managed = True
        db_table = 'sl_Magazyn'

    def __str__(self):
        return self.mag_Nazwa


# Model zdjęć towarów
class Zdjecie(models.Model):
    zd_Id = models.IntegerField(db_column='zd_Id', primary_key=True)
    zd_IdTowar = models.ForeignKey(Towar, models.DO_NOTHING, db_column='zd_IdTowar')
    zd_Zdjecie = models.ImageField(db_column='zd_Zdjecie', blank=True, null=True)
    zd_Glowne = models.BooleanField(db_column='zd_Glowne', blank=False)
    zd_CRC = models.IntegerField(db_column='zd_CRC', blank=True)

    class Meta:
        managed = True
        db_table = 'tw_ZdjecieTw'

    def __str__(self):
        return self.zd_Zdjecie

