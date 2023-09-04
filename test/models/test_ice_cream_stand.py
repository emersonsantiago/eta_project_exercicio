import unittest
from io import StringIO

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand(unittest.TestCase):
    def test_flavors_available(self):
        # Setup
        restaurant_name = "Tio Beto Sorvetes"
        cuisine_type = "Sorvetes Naturais"
        flavors_list = ["Milho verde", "Chocolate", "Morango ao leite"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
<<<<<<< HEAD
        expected_result = "No momento temos os seguintes sabores de sorvete disponíveis: Milho verde, Chocolate, Morango ao leite"

        # Chamada
        result = ice_cream_stand.flavors_available()


        # Validação
        assert expected_result == result
=======
        expected_result = "No momento temos os seguintes sabores de sorvete disponíveis:"

        # Chamada
        with StringIO() as out, unittest.mock.patch('sys.stdout', out):
            ice_cream_stand.flavors_available()
            result = out.getvalue().strip()

        # Validação
        self.assertIn(expected_result, result)
>>>>>>> origin/main

    def test_find_flavor(self):
        # Setup
        restaurant_name = "Tio Beto Sorvetes"
        cuisine_type = "Sorvetes Naturais"
        flavors_list = ["Milho verde", "Chocolate", "Morango ao leite"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
<<<<<<< HEAD
        expected_result = "Temos no momento Chocolate"

        # Chamada
        result = ice_cream_stand.find_flavor("Chocolate")

        # Validação
        assert expected_result == result
=======
        flavor_to_find = "Chocolate"
        expected_result = f"Temos no momento {flavor_to_find}!"

        # Chamada
        with StringIO() as out, unittest.mock.patch('sys.stdout', out):
            ice_cream_stand.find_flavor(flavor_to_find)
            result = out.getvalue().strip()

        # Validação
        self.assertIn(expected_result, result)
>>>>>>> origin/main

    def test_add_flavor(self):
        # Setup
        restaurant_name = "Tio Beto Sorvetes"
        cuisine_type = "Sorvetes Naturais"
        flavors_list = ["Milho verde", "Chocolate", "Morango ao leite"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
<<<<<<< HEAD
        expected_result = f"Baunilha adicionado ao estoque!"

        # Chamada
        result = ice_cream_stand.add_flavor("Baunilha")

        # Validação
        assert expected_result == result
=======
        flavor_to_add = "Baunilha"
        expected_result = f"{flavor_to_add} adicionado ao estoque!"

        # Chamada
        with StringIO() as out, unittest.mock.patch('sys.stdout', out):
            ice_cream_stand.add_flavor(flavor_to_add)
            result = out.getvalue().strip()

        # Validação
        self.assertIn(expected_result, result)
>>>>>>> origin/main
