from django.urls import path
from admin-multilanguage import views

app_name = "admin-multilanguage"
urlpatterns = [
    path('change_language/', views.ChangeLanguageView.as_view(), name='change_language'),
]
