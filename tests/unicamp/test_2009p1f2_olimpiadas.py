import pytest

from tests.run_script import run_script, read_text

RESOURCES_PATH = './tests/unicamp/resources/2009p1f2'
EXECUTABLE_PATH = './problems/unicamp/2009p1f2_olimpiadas.py'


@pytest.mark.parametrize(
    'input_path, output_path',
    [(f'{RESOURCES_PATH}/case_1.in', f'{RESOURCES_PATH}/case_1.out'),
     (f'{RESOURCES_PATH}/case_2.in', f'{RESOURCES_PATH}/case_2.out'),
     (f'{RESOURCES_PATH}/case_3.in', f'{RESOURCES_PATH}/case_3.out')]
)
def test_2009p1f2_olimpiadas(input_path: str, output_path: str):
    got = run_script(EXECUTABLE_PATH, input_path)
    expected = read_text(output_path)

    assert got == expected
