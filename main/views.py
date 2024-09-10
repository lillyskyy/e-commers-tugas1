from django.shortcuts import render

def item_list(request):
    context = {
        'name': 'Vintage Flower Dress',
        'price': 'Rp 250.000',
        'description': 'The Vintage Flower Dress is a timeless piece featuring a classic floral print.',
        'era': '80s',
        'condition': '60% ',
        'stock': '5'
    }
    return render(request, 'main.html', context)