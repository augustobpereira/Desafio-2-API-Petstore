from behave import given, when, then
from features.impl.ordem_de_compra import OrdemDeCompra

@given("uma nova ordem de compra for enviada com sucesso")
def step_impl(context):
    context.ordem_api = OrdemDeCompra()

    payload = {
        "id": 123456,
        "petId": 789,
        "quantity": 3,
        "status": "placed",
        "complete": True
    }

    response = context.ordem_api.criar_ordem_de_compra(payload)

    assert response.status_code == 200, f"Erro ao criar ordem: {response.status_code}"

    context.order_id = payload["id"]
    context.pet_id = payload["petId"]
    context.quantidade = payload["quantity"]
    context.status = payload["status"]
    context.complete = payload["complete"]

@then("a ordem de compra deve ser armazenada corretamente")
def step_impl(context):
    response = context.ordem_api.obter_ordem_de_compra(context.order_id)

    assert response.status_code == 200, f"Erro ao obter ordem: {response.status_code}"

    dados = response.json()

    assert dados["id"] == context.order_id
    assert dados["petId"] == context.pet_id
    assert dados["quantity"] == context.quantidade
    assert dados["status"] == context.status
    assert dados["complete"] == context.complete