from django import forms

class CocktailSearchForm(forms.Form):
    SEARCH_TYPE_CHOICES = [
        ('name', 'Cocktail '),
        ('ingredient', 'Ingredient'),
    ]
    search_type = forms.ChoiceField(choices=SEARCH_TYPE_CHOICES, label='Search By')
    query = forms.CharField(label='Search')
    


