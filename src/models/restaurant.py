class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        print(f"Esse restaurante se chama {self.restaurant_name} and serve {self.cuisine_type}.") #corrigi a exibição do nome do restaurante e erro ortográfico
        print(f"Esse restaurante serviu {self.number_served} consumidores desde que abriu.") # corrigi erro ortográfico e gramática

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True # estava false antes para indicar que o restaurante estava aberto, mas o certo é true para restaurante aberto
            self.number_served = 0 #corrigi aqui, pois antes estava -2 como número inicial de clientes servidos, mas não faz sentido ser -2
            print(f"{self.restaurant_name} agora está aberto!")
        else:
            print(f"{self.restaurant_name} já está aberto!")

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            print(f"{self.restaurant_name} agora está fechado!")
        else:
            print(f"{self.restaurant_name} já está fechado!")

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
        else:
            print(f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served += more_customers # corrigi o operador de atribuição para += para fazer o incremento corretamente no número de pessoas atendidas
        else:
            print(f"{self.restaurant_name} está fechado!")
