from django.contrib.auth.decorators import permission_required, user_passes_test
from django.views.generic import TemplateView

#Decorator function

@user_passes_test(permission_required, name="Admin")
class ProtectedView(TemplateView):
    template_name = "admin.html"