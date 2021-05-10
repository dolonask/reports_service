from django.shortcuts import render
from .forms import *

# Create your views here.
def create_card(request):
    if request.method == 'POST':
        form = CardsForm(request.POST)
        test = request.POST.getlist('files')
        if form.is_valid():
            # card = Cards.objects.create(**form.cleaned_data)
            print(test)
            # print(request.POST)
            # card = form.save()
    else:
        form = CardsForm()
    return render(request, 'card.html', {'form': form})