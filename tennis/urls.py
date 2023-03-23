
from django.urls import path
from. import views

urlpatterns = [
    path('', views.tennis_home, name='tennis_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.tennisDetailView.as_view(), name='tennis-detail')


]