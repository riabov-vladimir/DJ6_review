from django.shortcuts import redirect, render, get_object_or_404
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

    reviews = Review.objects.filter(product_id=pk)

    request.session['reviewed_products'] = []
    products = Review.objects.all()
    for x in products:
        request.session['reviewed_products'].append(x.product_id)
    print(request.session['reviewed_products'])

    print(products)
    if pk in request.session['reviewed_products']:
        is_review_exist = True
    else:
        is_review_exist = False

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.is_valid())
            print(form.cleaned_data)
            Review.objects.create(text=form.cleaned_data['text'], product_id=pk)
            return redirect('product_detail', pk)
    else:
        form = ReviewForm

    context = {
        'form': form,
        'product': product,
        'is_review_exist': is_review_exist,
        'reviews': reviews
    }
    print(context['is_review_exist'])
    return render(request, template, context)
