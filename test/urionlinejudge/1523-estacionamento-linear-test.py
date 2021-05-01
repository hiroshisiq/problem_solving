import pytest

from ..run_script import run_script, read_text

RESOURCES_PATH = './test/urionlinejudge/resources/1523/'
EXECUTABLE_PATH = './problems/urionlinejudge/1523-estacionamento-linear.py'

@pytest.mark.parametrize(
    'input_path, output_path',
    [(f'{RESOURCES_PATH}/case-1.in', f'{RESOURCES_PATH}/case-1.out')]
)
def test_1523_estacionamento_linear(input_path: str, output_path: str):
    got = run_script(EXECUTABLE_PATH, input_path)
    expected = read_text(output_path)

    assert got == expected
