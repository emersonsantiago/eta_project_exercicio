import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):

    def test_describe_restaurant(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
<<<<<<< HEAD
        expected_result = f"Esse restaurante se chama {restaurant_name} e serve {cuisine_type}.\nEsse restaurante serviu 0 consumidores desde que abriu."

        # Chamada
        result = restaurant.describe_restaurant()

        # Validação
        assert expected_result == result
=======
        expected_output = f"Esse restaurante se chama {restaurant_name} and serve {cuisine_type}.\nEsse restaurante serviu 0 consumidores desde que abriu."

        # Chamada
        with unittest.mock.patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
            restaurant.describe_restaurant()
            result = mock_stdout.getvalue().strip()

        # Validação
        self.assertEqual(result, expected_output)
>>>>>>> origin/main

    def test_open_restaurant(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
<<<<<<< HEAD
        expected_result = "Tio Beto Restaurante agora está aberto!"

        # Chamada
        result = restaurant.open_restaurant(True)

        # Validação
        assert expected_result == result
=======

        # Chamada
        restaurant.open_restaurant()

        # Validação
        self.assertTrue(restaurant.open)
>>>>>>> origin/main

    def test_close_restaurant(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
<<<<<<< HEAD
        expected_result = "Tio Beto Restaurante agora está fechado!"
        # Chamada
        result = restaurant.close_restaurant(False)

        # Validação
        assert expected_result == result
=======

        # Chamada
        restaurant.close_restaurant()

        # Validação
        self.assertFalse(restaurant.open)
>>>>>>> origin/main

    def test_set_number_served(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
<<<<<<< HEAD
        number_served = 10

        # Chamada
        result = restaurant.set_number_served(10)

        # Validação
        assert number_served == result
=======
        total_customers = 10

        # Chamada
        restaurant.set_number_served(total_customers)

        # Validação
        self.assertEqual(restaurant.number_served, total_customers)
>>>>>>> origin/main

    def test_increment_number_served(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        initial_customers = 5
        increment_customers = 3
        expected_customers = initial_customers + increment_customers

        # Chamada
        restaurant.number_served = initial_customers
        restaurant.increment_number_served(increment_customers)

        # Validação
<<<<<<< HEAD
        assert restaurant.number_served == expected_customers
=======
        self.assertEqual(restaurant.number_served, expected_customers)
>>>>>>> origin/main

