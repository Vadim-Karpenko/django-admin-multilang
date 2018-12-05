from django.views.generic import View
from django.shortcuts import redirect
from django.conf import settings

class ChangeLanguageView(View):
    def get(self, request):
        language = request.GET.get('language', None)
        current_path = request.GET.get('current_path', None)
        for setting_language in settings.LANGUAGES:
            if language == setting_language[0]:
                if current_path:
                    request.session['_language'] = language
                    return redirect(current_path)
                else:
                    raise ValidationError("\"current_path\" is impoperly configured")
