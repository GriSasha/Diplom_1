
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_FILLING, 
    INGREDIENT_TYPE_SAUCE)
import pytest

class TestBurger:

    def test_burger_add_ingridient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Кетчуп', 0.99)
        burger = Burger()
        burger.add_ingredient(ingredient)
        
        assert len(burger.ingredients) == 1

    def test_burger_remove_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Кетчуп', 0.99)
        burger = Burger()
        burger.add_ingredient(ingredient)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_burger_move_ingredient(self):
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, 'Кетчуп', 0.99)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, 'Котлетка', 2.00)
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        burger.move_ingredient(0, 1)

        
        assert burger.ingredients[0].type == INGREDIENT_TYPE_FILLING

    def test_burger_get_price(self):
        bun_mock = Mock()
        ingredient_mock = Mock()
        burger = Burger()

        bun_mock.get_price.return_value = 10
        ingredient_mock.get_price.return_value = 1
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)

        assert burger.get_price() == 21

    def test_burger_get_receipt(self):
        ingredient_mock = Mock()
        bun_mock = Mock()
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)

        bun_mock.get_name.return_value = 'Булка'
        ingredient_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient_mock.get_name.return_value = 'Котлетка'
        bun_mock.get_price.return_value = 10
        ingredient_mock.get_price.return_value = 1


        assert burger.get_receipt() == '(==== Булка ====)\n= filling Котлетка =\n(==== Булка ====)\n\nPrice: 21'

