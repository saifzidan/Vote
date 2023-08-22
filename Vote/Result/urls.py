from django.urls import path
from Worker import views
from . import views as me
app_name = 'Result'
urlpatterns = [
    path('', me.IndexView.as_view(), name='index'),
    path('<int:pk>/', me.ResultsView.as_view(), name='results'),
]