# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TwKodkreskowy(models.Model):
    kk_id = models.IntegerField(db_column='kk_Id', primary_key=True)  # Field name made lowercase.
    kk_idtowar = models.ForeignKey('TwTowar', models.DO_NOTHING, db_column='kk_IdTowar')  # Field name made lowercase.
    kk_kod = models.CharField(db_column='kk_Kod', max_length=20)  # Field name made lowercase.
    kk_ilosc = models.DecimalField(db_column='kk_Ilosc', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tw_KodKreskowy'
        unique_together = (('kk_idtowar', 'kk_kod'),)
