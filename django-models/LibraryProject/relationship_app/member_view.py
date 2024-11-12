from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

@method_decorator(permission_required, name="dispatch")
class ProtectedView(TemplateView):
    template_name = "member.html"