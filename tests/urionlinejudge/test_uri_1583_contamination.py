#!/usr/bin/env python3
import pytest
from tests.run_script import run_script, read_text

RESOURCES_PATH = './tests/urionlinejudge/resources/1583'
EXECUTABLE_PATH = './problems/urionlinejudge/uri_1583_contamination.py'


@pytest.mark.parametrize(
    'input_path, output_path',
    [(f'{RESOURCES_PATH}/case_1.in', f'{RESOURCES_PATH}/case_1.out'),
     (f'{RESOURCES_PATH}/case_2.in', f'{RESOURCES_PATH}/case_2.out')]
)
def test_uri_1583_contamination(input_path: str, output_path: str):
    got = run_script(EXECUTABLE_PATH, input_path)
    expected = read_text(output_path)

    assert got == expected
