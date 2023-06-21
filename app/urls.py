from django.contrib import admin
from django.urls import path
from . import views
from .views import SearchResultsView


handler500 = 'app.views.error_500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('towar/<int:pk>/', views.towar_details, name='towar'),
    # path('zdjecie/<int:pk>/', views.towar_photo, name='towar_photo'),
    path('zdjecie/<int:pk>/', views.image_view, name='image_view'),
    path('stan/<int:pk>/', views.towar_stan, name='towar_stan'),
    path('search/', SearchResultsView.as_view(), name='search_results')
]
