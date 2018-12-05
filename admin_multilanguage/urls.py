from django.urls import path
from admin_multilanguage import views

app_name = "admin_multilanguage"
urlpatterns = [
    path('change_language/', views.ChangeLanguageView.as_view(), name='change_language'),
]
