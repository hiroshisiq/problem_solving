import pytest

from tests.run_script import run_script, read_text

RESOURCES_PATH = './tests/codeforces/resources/101879'
EXECUTABLE_PATH = './problems/codeforces/cd_101879_a_story_about_tea.py'


@pytest.mark.parametrize(
    'input_path, output_path',
    [(f'{RESOURCES_PATH}/case_1.in', f'{RESOURCES_PATH}/case_1.out'),
     (f'{RESOURCES_PATH}/case_2.in', f'{RESOURCES_PATH}/case_2.out'),
     (f'{RESOURCES_PATH}/case_3.in', f'{RESOURCES_PATH}/case_3.out')]
)
def test_cd_101879_a_story_about_tea(input_path: str, output_path: str):
    got = run_script(EXECUTABLE_PATH, input_path)
    expected = read_text(output_path)

    assert got == expected
