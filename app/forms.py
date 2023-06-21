from django import forms
from app.models import *


# Przekazywanie pól do wyświetlania w formularzach
class TowarDetail(forms.ModelForm):
    class Meta:
        model = Towar
        fields = ['tw_Nazwa', 'tw_Symbol', 'tw_PodstKodKresk']
        labels = {
            'tw_Nazwa': 'Nazwa',
            'tw_Symbol': 'Symbol',
            'tw_PodstKodKresk': 'EAN',
        }


# class TowarStan(forms.ModelForm):
#     class Meta:
#         model = Stan
#         fields = ['st_MagId', 'st_Stan']
#         labels = {
#             'st_MagId': 'Magazyn',
#             'st_Stan': 'Stan',
#         }


# class ZdjecieTowaru(forms.ModelForm):
#     class Meta:
#         model = Zdjecie
#         fields = ['zd_Zdjecie']
#         labels = {
#             'zd_Zdjecie': 'Zdjecie',
#         }


class SearchForms(forms.Form):
    query = forms.CharField()

