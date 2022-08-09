from django.shortcuts import render

from home.models import Term
# Create your views here.
def index(request):
    return render(request, 'home/index.html', {'terms': Term.objects.all()})
