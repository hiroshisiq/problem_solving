import pytest

from tests.run_script import run_script, read_text

RESOURCES_PATH = './tests/urionlinejudge/resources/1252/'
EXECUTABLE_PATH = './problems/urionlinejudge/1252_sort_sort_and_sort.py'

@pytest.mark.parametrize(
    'input_path, output_path',
    [(f'{RESOURCES_PATH}/case_1.in', f'{RESOURCES_PATH}/case_1.out')]
)
def test_1252_sort_sort_and_sort(input_path: str, output_path: str):
    got = run_script(EXECUTABLE_PATH, input_path)
    expected = read_text(output_path)

    assert got == expected
