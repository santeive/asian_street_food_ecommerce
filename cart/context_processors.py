"""Cart context processors"""

# Cart manager
from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}
