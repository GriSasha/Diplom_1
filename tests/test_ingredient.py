from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_FILLING, 
    INGREDIENT_TYPE_SAUCE)
import pytest

class TestIngredient:

    @pytest.mark.parametrize('name', 
            ['Котлета', 
             'dinosaur', 
             '101ютуб'])
    def test_ingredient_get_name(self, name):
        ingr = Ingredient('Sosage', name, 9.99)
        
        assert ingr.get_name() == name

    @pytest.mark.parametrize('price', [11.99, 0.99, 11])
    def test_ingredient_get_price(self, price):
        ingr = Ingredient('Sosage', 'name', price)
        
        assert ingr.get_price() == price

    @pytest.mark.parametrize('ing_type', 
                [INGREDIENT_TYPE_SAUCE, 
                 INGREDIENT_TYPE_FILLING])
    def test_ingredient_get_type(self, ing_type):
        ingr = Ingredient(ing_type, 'name', 9.99)

        assert ingr.get_type() == ing_type
        

