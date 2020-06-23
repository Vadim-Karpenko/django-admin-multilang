from django.views.generic import View
from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import activate

class ChangeLanguageView(View):
    """
    View to change language of the admin page by changing it's value that is stored in sessions.

    **GET PARAMS**

    ``language``
        str: A unique code of the language

    ``current_path``
        str: The current path of the user when request was made. It used to redirect user back to the same place.
    """

    def get(self, request):
        # Get request parameters
        language = request.GET.get('language', settings.LANGUAGE_CODE)
        current_path = request.GET.get('current_path', None)
        # Check if settings.LANGUAGES is valid
        if not settings.LANGUAGES:
            raise ValidationError("\"settings.LANGUAGES\" is empty or impoperly configured")
        # Check if new language code is available in settings.LANGUAGES
        for setting_language in settings.LANGUAGES:
            if language.lower() == setting_language[0].lower():
                request.session['_language'] = language
                activate(language)
                if current_path:
                    return redirect(current_path)
        # If no current_path specified, user will be redirected to the admin main page
        return redirect("admin:index")
