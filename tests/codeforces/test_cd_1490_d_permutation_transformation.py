import pytest

from tests.run_script import run_script, read_text

RESOURCES_PATH = './tests/codeforces/resources/1490'
EXECUTABLE_PATH = './problems/codeforces/cf_1490_d_permutation_transformation.py'


@pytest.mark.parametrize(
    'input_path, output_path',
    [(f'{RESOURCES_PATH}/case_1.in', f'{RESOURCES_PATH}/case_1.out'),
     (f'{RESOURCES_PATH}/case_2.in', f'{RESOURCES_PATH}/case_2.out')]
)
def test_cd_1490_d_permutation_transformation(input_path: str, output_path: str):
    got = run_script(EXECUTABLE_PATH, input_path)
    expected = read_text(output_path)

    assert got == expected
