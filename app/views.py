from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Towar, Zdjecie, Stan
from django.views.generic.list import ListView
import pyodbc
import base64


def detect_image_mime(image_data: bytes) -> str:
    """Wykrywa format obrazu na podstawie nagłówka (magic bytes)."""
    if image_data[:3] == b'\xff\xd8\xff':
        return 'image/jpeg'
    elif image_data[:8] == b'\x89PNG\r\n\x1a\n':
        return 'image/png'
    elif image_data[:4] in (b'GIF8', b'GIF9'):
        return 'image/gif'
    elif image_data[:4] == b'RIFF' and image_data[8:12] == b'WEBP':
        return 'image/webp'
    else:
        return 'image/jpeg'  # fallback


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def error_500(request):
    data = {}
    return render(request, '500.html', data)


def image_view(request, pk):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=10.0.0.10\\INSERTGT;'
        'DATABASE=astra_prod;'
        'UID=sa;'
        'PWD=')
    cursor = conn.cursor() # inicjalizacja kursora SQL
    cursor.execute(
        "SELECT zd_Zdjecie FROM tw_ZdjecieTw WHERE zd_IdTowar = ? AND zd_Glowne = 1", pk) # wykonanie kursora
    row = cursor.fetchone()
    image_data = bytes(row[0])
    mime_type = detect_image_mime(image_data)
    encoded_image = base64.b64encode(image_data).decode('utf-8')  # dekodowanie obrazu
    conn.close()

    return render(request, 'zdjecie.html', {'photo': encoded_image, 'photo_mime': mime_type})


def towar_details(request, pk):
    towar = get_object_or_404(Towar, pk=pk)     # pobranie danych produktu
    stan = get_object_or_404(Stan, pk=pk, st_MagId=1)   # pobranie danych na temat stanu produktu

    # pobieranie obrazu
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.0.0.10\\INSERTGT;DATABASE=astra_prod;UID=sa;PWD=')
    cursor = conn.cursor()  # inicjalizacja kursora SQL
    cursor.execute(
        "SELECT zd_Zdjecie FROM tw_ZdjecieTw WHERE zd_IdTowar = ? AND zd_Glowne = 1", pk)  # wykonanie kursora
    row = cursor.fetchone()
    image_data = bytes(row[0])
    mime_type = detect_image_mime(image_data)
    encoded_image = base64.b64encode(image_data).decode('utf-8')  # dekodowanie obrazu
    conn.close()

    return render(request, 'towar.html', {'item': towar,
                                          'quantity': stan,
                                          'photo': encoded_image,
                                          'photo_mime': mime_type,
                                          })


# Wyświetlenie stanu na Nowogrodzkiej
def towar_stan(request, pk):
    form = get_object_or_404(Stan, pk=pk, st_MagId=1)
    return render(request, 'stan.html', {'quantity': form})


# wyszukiwanie towarów
class SearchResultsView(ListView):
    model = Towar
    template_name = "search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Towar.objects.filter(
            Q(tw_Nazwa__icontains=query) | Q(tw_Symbol__icontains=query) | Q(tw_PodstKodKresk__icontains=query)
        ).order_by('tw_Nazwa')
        return object_list

