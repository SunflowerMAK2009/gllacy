from django.shortcuts import render
from .models import Product
from .forms import FilterForm

# Create your views here.
def catalog_view(request):
    products = Product.objects.all()
    filter_form = FilterForm(request.GET)
    if filter_form.is_valid():
        if filter_form.cleaned_data["fat"]:
            fat_value = filter_form.cleaned_data["fat"]
            if fat_value == "zero":
                products = products.filter(fat=0)
            elif fat_value == "up_to_ten":
                products = products.filter(fat__lte=10)
            elif fat_value == "up_to_thirty":
                products = products.filter(fat__lt=30)
            else:
                products = products.filter(fat__gte=30)
        if filter_form.cleaned_data["fillers"]:
            selected_fillers = filter_form.cleaned_data["fillers"]
            products = products.filter(fillers__name__in=selected_fillers).distinct()
            # filter(fillers__name__in=selected_fillers): Фильтрует мороженки,
            # у которых название хотя бы одного из наполнителей совпадает с выбранными.
    #- distinct(): Удаляет дублирующиеся записи из результатов.
    #Например пользователь выбрал "Фрукты" и "Сиропы". Сначала Django поищет мороженки с фруктами и добавит их в итоговый список,
    # потом поищет мороженки с сиропами и тоже добавит их в итоговый список.
    # Если у нас есть мороженки у которых есть и сироп и фрукты они попадут в итоговый список дважды.
    # distinct() позволяет не дублировать эти мороженки.
        if filter_form.cleaned_data["min_price"] and filter_form.cleaned_data["max_price"]:
            min_price = filter_form.cleaned_data["min_price"]
            max_price = filter_form.cleaned_data["max_price"]
            products = products.filter(price__gte=min_price)
            products = products.filter(price__lte=max_price)
    return render(request, 'catalog/catalog.html', context={"products": products})

