from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)

    form = ReviewForm
    if request.method == 'POST':
        # логика для добавления отзыва
        pass

    is_review_exist = ''

    context = {
        'form': form,
        'product': product,
        'is_review_exist': is_review_exist
    }

    return render(request, template, context)
