#!/usr/bin/env python3
import pytest
from tests.run_script import run_script, read_text

RESOURCES_PATH = './tests/onlinejudge/resources/336'
EXECUTABLE_PATH = './problems/onlinejudge/onl_336_a_node_too_far.py'


@pytest.mark.parametrize(
    'input_path, output_path',
    [(f'{RESOURCES_PATH}/case_1.in', f'{RESOURCES_PATH}/case_1.out'),
     (f'{RESOURCES_PATH}/case_2.in', f'{RESOURCES_PATH}/case_2.out'),
     (f'{RESOURCES_PATH}/case_3.in', f'{RESOURCES_PATH}/case_3.out'),
     (f'{RESOURCES_PATH}/case_4.in', f'{RESOURCES_PATH}/case_4.out'),
     (f'{RESOURCES_PATH}/case_5.in', f'{RESOURCES_PATH}/case_5.out')]
)
def test_onl_336_a_node_too_far(input_path: str, output_path: str):
    got = run_script(EXECUTABLE_PATH, input_path)
    expected = read_text(output_path)

    assert got == expected
