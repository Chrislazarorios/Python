import app  # Asegúrate de que este sea el nombre del archivo que contiene tu código
from unittest.mock import patch

# Test para agregar productos
@patch('builtins.input', side_effect=["1", "Manzana", "10", "3"])  # Simulamos la secuencia de inputs
def test_agregar_producto(mock_input):
    app.productos = []  # Reseteamos la lista de productos
    app.main()  # Llamamos a la función principal
    assert len(app.productos) == 1  # Verificamos que se haya agregado el producto
    assert app.productos[0] == ["Manzana", 10]  # Verificamos que los datos sean correctos

