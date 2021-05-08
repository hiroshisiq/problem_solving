import pytest

from tests.run_script import run_script, read_text

RESOURCES_PATH = './tests/unicamp/resources/2016p1f1'
EXECUTABLE_PATH = './problems/unicamp/uni_2016p1f1_tacos_de_bilhar.py'


@pytest.mark.parametrize(
    'input_path, output_path',
    [(f'{RESOURCES_PATH}/case_1.in', f'{RESOURCES_PATH}/case_1.out'),
     (f'{RESOURCES_PATH}/case_2.in', f'{RESOURCES_PATH}/case_2.out')]
)
def test_2016p1f1_tacos_de_bilhar(input_path: str, output_path: str):
    got = run_script(EXECUTABLE_PATH, input_path)
    expected = read_text(output_path)

    assert got == expected
