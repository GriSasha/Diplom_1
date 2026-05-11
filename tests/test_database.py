from praktikum.database import Database
import pytest


class TestDatabase:

    def test_database_available_buns(self):
        dat = Database()

        assert len(dat.available_buns()) == 3

    def test_database_available_ingredients(self):

        dat = Database()

        assert len(dat.available_ingredients()) == 6

        