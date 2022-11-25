from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')

def product(request):
    test =  [{'name':'Geovana', 'old': 22}]
    return render(request, 'product/product.html', {'test': test})
