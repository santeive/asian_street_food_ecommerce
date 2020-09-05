from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product


def home(request):
    categories = Category.objects.all()
    return render(request, 'shop/product/index.html', {'categories': categories})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list2.html',
                  {'category': category,
                   'products': products,
                   'categories': categories})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
                                
    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product/detail2.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})