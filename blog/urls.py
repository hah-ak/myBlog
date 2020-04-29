from django.urls import path

from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('Algorithm/<slug:sort>/<int:pk>/', views.CodeDetailView.as_view(), name='codes-detail'),
    path('Algorithm/',views.AlgorithmVeiw.as_view(),name='Algorithm'),
    path('Algorithm/SSEA/', views.SSEAView.as_view(), name='SSEA'),
    path('Algorithm/programmers/',views.programmersView.as_view(),name='programmers'),
    path('fashion/', views.fashion, name='fashion'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name = 'about'),
    path('result/',views.Search,name='search'),
]