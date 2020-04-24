from django.urls import path

from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('<slug:sort>/<int:pk>/', views.CodeDetailView.as_view(), name='codes-detail'),
    path('SSEA/', views.SSEAView.as_view(), name='SSEA'),
    path('programmers/',views.programmersView.as_view(),name='programmers'),
    path('fashion/', views.fashion, name='fashion'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name = 'about'),
    path('result/',views.SearchView.as_view(),name='search'),
]