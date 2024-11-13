from django.views.decorators.csrf import csrf_protect

@csrf_protect
def ExampleForm(requst): ...