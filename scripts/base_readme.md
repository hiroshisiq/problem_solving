# Problem Solving
A repository to keep track of my solutions for algorithms and data structure problems.

## Setup
```bash
# Create virtual environment
virtualenv venv --python python3
source venv/bin/activate

# Install requirements
pip install -r requirements.txt 
```

## Running
```bash
python -vv
```
## Updating content section
There is a script at `/scripts` to collect all internal `readme.md` and append it's content to the Content section bellow.
```shell
python scripts/update_readme.py
```

## Contributing to the repository 
There is a script at `/scripts` to create a boilerplate for you problem.
```shell
python scripts/create_boilerplate.py --provider <problem_provider> --id <problem_id> --name <problem_name_with_underscore> --url <problem_url>
```

Use example:
```shell
python scripts/create_boilerplate.py --provider urionlinejudge --id 1076 --name drawing_mazes --url https://www.urionlinejudge.com.br/judge/pt/problems/view/1076
```

## Content
