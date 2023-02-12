from .import views
from django.urls import path

app_name='pollApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('pollApp/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('signin/', views.signin, name='poll-login'),
    path('signout/', views.signout, name='poll-logout'),
    path('count/', views.voted, name='voted'),
]