from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category
from rest_framework import viewsets
from .serializer import CategorySerializer

# Create your views here.

def add_category(request):
    template_name = 'categories/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
