from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Word

# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'flashcards/index.html.j2', context)

# Return all questions for category
def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    words = Word.objects.filter(categories=category)
    context = {'category': category, 'words': words}
    return render(request, 'flashcards/words.html.j2', context)