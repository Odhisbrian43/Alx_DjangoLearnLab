from django.contrib.auth.decorators import permission_required, user_passes_test
from django.views.generic import TemplateView

#Decorator function

@user_passes_test(permission_required, name="Member")
class ProtectedView(TemplateView):
    template_name = "member.html"