from django.shortcuts import render, get_object_or_404 ,redirect,HttpResponseRedirect
from .models import Product,Order,OrderItem
from .forms import SearchForm

# Create your views here.


def product_list(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(name__icontains=query)
    else:
        results = Product.objects.all()
    return render(request, 'product_list.html', {'form': form, 'query': query, 'results': results})

def product_detail(request,id):
    product=get_object_or_404(Product,id=id)
    return render ( request,'product_detail.html',{'product':product})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(completed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if not created:
        order_item.quantity += 1
    order_item.save()
    return redirect('cart_detail')


def cart_detail(request):
    order, created = Order.objects.get_or_create(completed=False)
    return render(request, 'cart_detail.html', {'order': order})


def update_cart(request, item_id):
    order_item = get_object_or_404(OrderItem, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > 0:
            order_item.quantity = quantity
            order_item.save()
        else:
            order_item.delete()
    return redirect('cart_detail')

def checkout(request):
    order, created = Order.objects.get_or_create(completed=False)
    order.completed = True
    order.save()
    return render(request, 'checkout.html', {'order': order})