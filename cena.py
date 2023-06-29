# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TwCena(models.Model):
    tc_id = models.IntegerField(db_column='tc_Id', primary_key=True)  # Field name made lowercase.
    tc_idtowar = models.OneToOneField('TwTowar', models.DO_NOTHING, db_column='tc_IdTowar')  # Field name made lowercase.
    tc_cenanetto0 = models.DecimalField(db_column='tc_CenaNetto0', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenabrutto0 = models.DecimalField(db_column='tc_CenaBrutto0', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_walutaid = models.CharField(db_column='tc_WalutaId', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tc_idwalutakurs = models.IntegerField(db_column='tc_IdWalutaKurs', blank=True, null=True)  # Field name made lowercase.
    tc_walutakurs = models.DecimalField(db_column='tc_WalutaKurs', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenanettowaluta = models.DecimalField(db_column='tc_CenaNettoWaluta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenanettowaluta2 = models.DecimalField(db_column='tc_CenaNettoWaluta2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenawalutanarzut = models.DecimalField(db_column='tc_CenaWalutaNarzut', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_walutajedn = models.CharField(db_column='tc_WalutaJedn', max_length=10)  # Field name made lowercase.
    tc_podstawakc = models.IntegerField(db_column='tc_PodstawaKC', blank=True, null=True)  # Field name made lowercase.
    tc_cenanetto1 = models.DecimalField(db_column='tc_CenaNetto1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenanetto2 = models.DecimalField(db_column='tc_CenaNetto2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenanetto3 = models.DecimalField(db_column='tc_CenaNetto3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenanetto4 = models.DecimalField(db_column='tc_CenaNetto4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenanetto5 = models.DecimalField(db_column='tc_CenaNetto5', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenanetto6 = models.DecimalField(db_column='tc_CenaNetto6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenanetto7 = models.DecimalField(db_column='tc_CenaNetto7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenanetto8 = models.DecimalField(db_column='tc_CenaNetto8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenanetto9 = models.DecimalField(db_column='tc_CenaNetto9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenanetto10 = models.DecimalField(db_column='tc_CenaNetto10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenabrutto1 = models.DecimalField(db_column='tc_CenaBrutto1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenabrutto2 = models.DecimalField(db_column='tc_CenaBrutto2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenabrutto3 = models.DecimalField(db_column='tc_CenaBrutto3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenabrutto4 = models.DecimalField(db_column='tc_CenaBrutto4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenabrutto5 = models.DecimalField(db_column='tc_CenaBrutto5', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenabrutto6 = models.DecimalField(db_column='tc_CenaBrutto6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenabrutto7 = models.DecimalField(db_column='tc_CenaBrutto7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenabrutto8 = models.DecimalField(db_column='tc_CenaBrutto8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenabrutto9 = models.DecimalField(db_column='tc_CenaBrutto9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_cenabrutto10 = models.DecimalField(db_column='tc_CenaBrutto10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_zysk1 = models.DecimalField(db_column='tc_Zysk1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_zysk2 = models.DecimalField(db_column='tc_Zysk2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_zysk3 = models.DecimalField(db_column='tc_Zysk3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_zysk4 = models.DecimalField(db_column='tc_Zysk4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_zysk5 = models.DecimalField(db_column='tc_Zysk5', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_zysk6 = models.DecimalField(db_column='tc_Zysk6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_zysk7 = models.DecimalField(db_column='tc_Zysk7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_zysk8 = models.DecimalField(db_column='tc_Zysk8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_zysk9 = models.DecimalField(db_column='tc_Zysk9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_zysk10 = models.DecimalField(db_column='tc_Zysk10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_narzut1 = models.DecimalField(db_column='tc_Narzut1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_narzut2 = models.DecimalField(db_column='tc_Narzut2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_narzut3 = models.DecimalField(db_column='tc_Narzut3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_narzut4 = models.DecimalField(db_column='tc_Narzut4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_narzut5 = models.DecimalField(db_column='tc_Narzut5', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_narzut6 = models.DecimalField(db_column='tc_Narzut6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_narzut7 = models.DecimalField(db_column='tc_Narzut7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_narzut8 = models.DecimalField(db_column='tc_Narzut8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_narzut9 = models.DecimalField(db_column='tc_Narzut9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_narzut10 = models.DecimalField(db_column='tc_Narzut10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_marza1 = models.DecimalField(db_column='tc_Marza1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_marza2 = models.DecimalField(db_column='tc_Marza2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_marza3 = models.DecimalField(db_column='tc_Marza3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_marza4 = models.DecimalField(db_column='tc_Marza4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_marza5 = models.DecimalField(db_column='tc_Marza5', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_marza6 = models.DecimalField(db_column='tc_Marza6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_marza7 = models.DecimalField(db_column='tc_Marza7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_marza8 = models.DecimalField(db_column='tc_Marza8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_marza9 = models.DecimalField(db_column='tc_Marza9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_marza10 = models.DecimalField(db_column='tc_Marza10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tc_idwaluta0 = models.CharField(db_column='tc_IdWaluta0', max_length=3)  # Field name made lowercase.
    tc_idwaluta1 = models.CharField(db_column='tc_IdWaluta1', max_length=3)  # Field name made lowercase.
    tc_idwaluta2 = models.CharField(db_column='tc_IdWaluta2', max_length=3)  # Field name made lowercase.
    tc_idwaluta3 = models.CharField(db_column='tc_IdWaluta3', max_length=3)  # Field name made lowercase.
    tc_idwaluta4 = models.CharField(db_column='tc_IdWaluta4', max_length=3)  # Field name made lowercase.
    tc_idwaluta5 = models.CharField(db_column='tc_IdWaluta5', max_length=3)  # Field name made lowercase.
    tc_idwaluta6 = models.CharField(db_column='tc_IdWaluta6', max_length=3)  # Field name made lowercase.
    tc_idwaluta7 = models.CharField(db_column='tc_IdWaluta7', max_length=3)  # Field name made lowercase.
    tc_idwaluta8 = models.CharField(db_column='tc_IdWaluta8', max_length=3)  # Field name made lowercase.
    tc_idwaluta9 = models.CharField(db_column='tc_IdWaluta9', max_length=3)  # Field name made lowercase.
    tc_idwaluta10 = models.CharField(db_column='tc_IdWaluta10', max_length=3)  # Field name made lowercase.
    tc_kurswaluty1 = models.IntegerField(db_column='tc_KursWaluty1', blank=True, null=True)  # Field name made lowercase.
    tc_kurswaluty2 = models.IntegerField(db_column='tc_KursWaluty2', blank=True, null=True)  # Field name made lowercase.
    tc_kurswaluty3 = models.IntegerField(db_column='tc_KursWaluty3', blank=True, null=True)  # Field name made lowercase.
    tc_kurswaluty4 = models.IntegerField(db_column='tc_KursWaluty4', blank=True, null=True)  # Field name made lowercase.
    tc_kurswaluty5 = models.IntegerField(db_column='tc_KursWaluty5', blank=True, null=True)  # Field name made lowercase.
    tc_kurswaluty6 = models.IntegerField(db_column='tc_KursWaluty6', blank=True, null=True)  # Field name made lowercase.
    tc_kurswaluty7 = models.IntegerField(db_column='tc_KursWaluty7', blank=True, null=True)  # Field name made lowercase.
    tc_kurswaluty8 = models.IntegerField(db_column='tc_KursWaluty8', blank=True, null=True)  # Field name made lowercase.
    tc_kurswaluty9 = models.IntegerField(db_column='tc_KursWaluty9', blank=True, null=True)  # Field name made lowercase.
    tc_kurswaluty10 = models.IntegerField(db_column='tc_KursWaluty10', blank=True, null=True)  # Field name made lowercase.
    tc_datakursuwaluty = models.DateTimeField(db_column='tc_DataKursuWaluty', blank=True, null=True)  # Field name made lowercase.
    tc_bankkursuwaluty = models.IntegerField(db_column='tc_BankKursuWaluty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tw_Cena'
