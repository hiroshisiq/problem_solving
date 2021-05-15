import argparse
from os import path, mkdir
import sys

parser = argparse.ArgumentParser()

parser.add_argument('--provider', help='Name of the problem provider')
parser.add_argument('--id', help='Problem\'s ID')
parser.add_argument('--name', help='Problem\'s name')
parser.add_argument('--url', help='Problem\'s URL (optional)')
parser.add_argument('--cases', help='Number of test cases (optional)')

args = parser.parse_args()

# Check if it's being called from the root of the repository
assert path.exists('problems')

# Check if has all required parameters
assert args.provider
assert args.id
assert args.name

# Create provider problem directory and readme if don't exists
if not path.exists(f'problems/{args.provider}'):
    mkdir(f'problems/{args.provider}')

    with open(f'problems/{args.provider}/readme.md', "w") as f:
        f.write(
            f'### {args.provider}\n'
            f'The challenges included in this section can all be found at https://{args.provider}.com/\n\n'
        )

# Add problem to readme
with open(f'problems/{args.provider}/readme.md', "a") as f:
    f.write(
        f'- [{args.id}]({args.url}) {args.name};\n'
    )

# Create solution boiler plate
with open(f'problems/{args.provider}/{args.provider[:3]}_{args.id}_{args.name}.py', "w") as f:
    f.write(
        "#!/usr/bin/env python3\n"
        "\n"
        "\n"
        "def solve_problem():\n"
        "    print(\'Not implemented\')\n"
        "\n"
        "\n"
        "if __name__ == \"__main__\":\n"
        "    solve_problem()\n"
    )

# Create provider test directory if don't exists
if not path.exists(f'tests/{args.provider}'):
    mkdir(f'tests/{args.provider}')
    open(f'tests/{args.provider}/__init__.py', 'x')

# Create provider resources directory if don't exists
if not path.exists(f'tests/{args.provider}/resources'):
    mkdir(f'tests/{args.provider}/resources')

# Create problem resources directory if don't exists
if not path.exists(f'tests/{args.provider}/resources/{args.id}'):
    mkdir(f'tests/{args.provider}/resources/{args.id}')

# Create empty file for test cases
number_of_test_cases = int(args.cases) if args.cases else 1
for i in range(number_of_test_cases):
    open(f'tests/{args.provider}/resources/{args.id}/case_{i+1}.in', 'x')
    open(f'tests/{args.provider}/resources/{args.id}/case_{i+1}.out', 'x')

# Create test file
with open(f'tests/{args.provider}/test_{args.provider[:3]}_{args.id}_{args.name}.py', "w") as f:
    f.write(
        "#!/usr/bin/env python3\n"
        "import pytest\n"
        "from tests.run_script import run_script, read_text\n"
        "\n"
        f'RESOURCES_PATH = \'./tests/{args.provider}/resources/{args.id}\'\n'
        f'EXECUTABLE_PATH = \'./problems/{args.provider}/{args.provider[:3]}_{args.id}_{args.name}.py\'\n'
        "\n"
        "\n"
        "@pytest.mark.parametrize(\n"
        "    'input_path, output_path',"
        "    [(f\'{RESOURCES_PATH}/case_1.in\', f\'{RESOURCES_PATH}/case_1.out\')]\n"
        ")\n"
        f'def test_{args.provider[:3]}_{args.id}_{args.name}(input_path: str, output_path: str):\n'
        "    got = run_script(EXECUTABLE_PATH, input_path)\n"
        "    expected = read_text(output_path)\n"
        "\n"
        "    assert got == expected\n"
    )

print(args.provider)
print('Finished!')
