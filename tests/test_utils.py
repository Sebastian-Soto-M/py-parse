import app.utils as utils


def test_build_csv_string():
    expected = 'Fecha, Actividad\n24/10, Reunion\n'
    initial_value: list[list[str]] = [
        ['Fecha', 'Actividad'], ['24/10', 'Reunion']]
    assert expected == utils.build_csv_string(initial_value)
