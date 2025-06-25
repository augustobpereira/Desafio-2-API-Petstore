import requests

class OrdemDeCompra:
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"

    def criar_ordem_de_compra(self, payload):
        url = f"{self.base_url}/store/order"
        response = requests.post(url, json=payload)
        return response

    def obter_ordem_de_compra(self, order_id):
        url = f"{self.base_url}/store/order/{order_id}"
        response = requests.get(url)
        return response