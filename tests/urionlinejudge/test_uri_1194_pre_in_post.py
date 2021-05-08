import pytest

from tests.run_script import run_script, read_text

RESOURCES_PATH = './tests/urionlinejudge/resources/1194'
EXECUTABLE_PATH = './problems/urionlinejudge/uri_1194_pre_in_pos.py'


@pytest.mark.parametrize(
    'input_path, output_path',
    [(f'{RESOURCES_PATH}/case_1.in', f'{RESOURCES_PATH}/case_1.out'),
     (f'{RESOURCES_PATH}/case_2.in', f'{RESOURCES_PATH}/case_2.out')]
)
def test_1194_prefix_infix_postfix(input_path: str, output_path: str):
    got = run_script(EXECUTABLE_PATH, input_path)
    expected = read_text(output_path)

    assert got == expected