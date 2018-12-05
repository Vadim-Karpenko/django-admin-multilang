from django.urls import path
from languages import views

app_name = "languages"
urlpatterns = [
    path('change_language/', views.ChangeLanguageView.as_view(), name='change_language'),
]
