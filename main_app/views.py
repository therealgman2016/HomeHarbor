from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def listings_index(request):
  return render(request, 'listings/index.html', {
    # 'listings': listings
  })

