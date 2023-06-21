# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TwZdjecietw(models.Model):
    zd_id = models.IntegerField(db_column='zd_Id', primary_key=True)  # Field name made lowercase.
    zd_idtowar = models.ForeignKey('TwTowar', models.DO_NOTHING, db_column='zd_IdTowar')  # Field name made lowercase.
    zd_zdjecie = models.BinaryField(db_column='zd_Zdjecie', blank=True, null=True)  # Field name made lowercase.
    zd_glowne = models.BooleanField(db_column='zd_Glowne')  # Field name made lowercase.
    zd_crc = models.IntegerField(db_column='zd_CRC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tw_ZdjecieTw'
