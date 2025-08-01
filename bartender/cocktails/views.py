from django.shortcuts import render
from .forms import CocktailSearchForm
import requests

def search_cocktails(request):
    form = CocktailSearchForm()
    results = []

    if request.GET.get('query'):
        form = CocktailSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_type = form.cleaned_data['search_type']

            if search_type == 'name':
                url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}"
            else:
                url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={query}"

            response = requests.get(url)
            data = response.json()
            if data.get('drinks'):
                results = data['drinks']
    return render(request, 'cocktails/search.html', {'form': form, 'results': results})

def cocktail_detail(request, drink_id):
    response = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}')
    data = response.json()
    drink = data['drinks'][0] if data.get('drinks') else None

    ingredients = []
    if drink:
        for i in range(1, 4):
            ingredient = drink.get(f'strIngredient{i}')
            measure = drink.get(f'strMeasure{i}')
            if ingredient:
                ingredients.append({'ingredient': ingredient, 'measure': measure})

    return render(request, 'detail.html', {'drink': drink, 'ingredients': ingredients})




