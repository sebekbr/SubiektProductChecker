from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Towar, Ean, Stan
from django.views.generic.list import ListView
import pyodbc
import base64


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def error_500(request):
    data = {}
    return render(request, '500.html', data)


def image_view(request, pk):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOST\\INSERTGT;DATABASE=astra;UID=sa;PWD=')
    cursor = conn.cursor()  # inicjalizacja kursora SQL
    cursor.execute(
        "SELECT zd_Zdjecie FROM tw_ZdjecieTw WHERE zd_IdTowar = ? AND zd_Glowne = 1", pk)  # wykonanie kursora
    row = cursor.fetchone()
    image_data = row[0]
    encoded_image = base64.b64encode(image_data).decode('utf-8')  # dekodowanie obrazu
    conn.close()

    return render(request, 'zdjecie.html', {'photo': encoded_image})


def towar_details(request, pk):
    towar = get_object_or_404(Towar, pk=pk)  # pobranie danych produktu
    stan = get_object_or_404(Stan, pk=pk, st_MagId=1)  # pobranie danych na temat stanu produktu
    kod_dodatkowy = get_object_or_404(Ean, pk=pk)

    # pobieranie obrazu
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-SB\\INSERTGT;DATABASE=testowa;UID=sa;PWD=')
    cursor = conn.cursor()  # inicjalizacja kursora SQL
    # pobieranie obrazu
    cursor.execute(
        "SELECT zd_Zdjecie FROM tw_ZdjecieTw WHERE zd_IdTowar=? AND zd_Glowne=1", pk)  # wykonanie kursora
    row = cursor.fetchone()
    image_data = row[0]
    encoded_image = base64.b64encode(image_data).decode('utf-8')  # dekodowanie obrazu

    context = {'item': towar,
               'quantity': stan,
               'photo': encoded_image,
               'kod_dodatkowy': kod_dodatkowy,
               }

    # # listowanie dodatkowych kodów EAN
    # cursor.execute(
    #     "SELECT kk_Kod FROM tw_KodKreskowy WHERE kk_IdTowar=?", pk
    # )
    # result = cursor.fetchall()
    # ean = ', '.join(str(*item) for item in result)
    conn.close()

    return render(request, 'towar.html', context)


# Wyświetlenie stanu na Nowogrodzkiej
def towar_stan(request, pk):
    form = get_object_or_404(Stan, pk=pk, st_MagId=1)
    return render(request, 'stan.html', {'quantity': form})


# wyszukiwanie towarów
class SearchResultsView(ListView):
    model = Towar
    template_name = "search.html"
    paginate_by = 50
    # queryset = super(Stan).get_queryset()

    def get_queryset(self):  #
        query = self.request.GET.get("q")
        object_list = Towar.objects.filter(
            Q(tw_Nazwa__icontains=query) | Q(tw_Symbol__icontains=query) | Q(tw_PodstKodKresk__icontains=query)
        ).order_by('tw_Nazwa')
        return object_list
