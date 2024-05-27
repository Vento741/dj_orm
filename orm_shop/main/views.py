from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Car




def cars_list_view(request):
    # получите список авто
    query = request.GET.get('q','')
    if query:
        cars = Car.objects.filter(model__icontains=query)
    else:
        cars = Car.objects.all()

    context = {'cars': cars, 'query': query}
    template_name = 'main/list.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    car = get_object_or_404(Car, pk=car_id)
    context = {'car': car}
    template_name = 'main/details.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        car = get_object_or_404(Car, pk=car_id)
        sales = car.sales.all()
        context = {'car': car, 'sales': sales}
        template_name = 'main/sales.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
