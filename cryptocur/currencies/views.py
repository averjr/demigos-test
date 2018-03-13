from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Pair, Price, Currency

from django.db import IntegrityError

from .forms import NewPairForm
from django.core.exceptions import ValidationError

from django.http import JsonResponse


def index(request):
    if request.method == 'POST':
        form = NewPairForm(request.POST)
        try:
            if form.is_valid():
                currency_first = form.cleaned_data['one']
                currency_second = form.cleaned_data['two']
                Pair.objects.create(
                        currency_first=currency_first,
                        currency_second=currency_second
                    )
                return JsonResponse({"status": "success"})
            else:
                return HttpResponse(form.errors.as_json())
        except IntegrityError as e:
            return JsonResponse({"status": "error", "message": e.args})

    else:
        form = NewPairForm()
        results = []
        pairs = Pair.objects.all()
        for one in pairs:
            price = Price.objects.filter(pair=one).order_by('-id')
            if price:
                results.append(price[0])

        context = {
            'pairs': results,
            'form': form
        }
        return render(request, 'index.html', context)
