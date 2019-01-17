from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Word

# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'index.html', context)