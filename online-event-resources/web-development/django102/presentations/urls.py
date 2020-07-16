from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('submit', views.CreateView.as_view(), name='submit'),
    path('edit/<int:pk>', views.EditView.as_view(), name='edit'),
]