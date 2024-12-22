import app  # Asegúrate de que este sea el nombre del archivo que contiene tu código
from unittest.mock import patch

# Test para la opción de salir
@patch('builtins.input', side_effect=["3"])  # Simulamos la opción de salida
def test_salir(mock_input):
    app.main()  # Ejecutamos el programa
    assert True  # Verificamos que el programa termina sin errores

