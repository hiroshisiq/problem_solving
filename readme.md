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
### Kattis
The challenges included in this section can all be found at https://open.kattis.com/

- [ferryloading4](https://open.kattis.com/problems/ferryloading4) Ferry Loading IV
### Online Judge
The challenges included in this section can all be found at https://onlinejudge.org

- [336](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=272) A Node Too Far
### Unicamp
The challenges included in this section can all be found at https://olimpiada.ic.unicamp.br/pratique/

- [2009p1f2](https://olimpiada.ic.unicamp.br/pratique/p1/2009/f2/olimp/) Olimpíadas;
- [2016p1f1](https://olimpiada.ic.unicamp.br/pratique/p1/2016/f1/tacos-bilhar/) Tacos de Bilhar;
### Uri Online Judge
The challenges included in this section can all be found at https://www.urionlinejudge.com.br/

- [1523](https://www.urionlinejudge.com.br/judge/pt/problems/view/1523) Estacionamento Linear
- [1252](https://www.urionlinejudge.com.br/judge/en/problems/view/1252) Sort!, Sort!! and Sort!!!
- [1194](https://www.urionlinejudge.com.br/judge/pt/problems/view/1194) Prefixa, Infixa e Posfixa
- [2448](https://www.urionlinejudge.com.br/judge/en/problems/view/2448) Postman
- [1076](https://www.urionlinejudge.com.br/judge/pt/problems/view/1076) Drawing Mazes
- [1583](https://www.urionlinejudge.com.br/judge/en/problems/view/1583) Contamination
- [1123](https://www.urionlinejudge.com.br/judge/en/problems/view/1123) Route Change
- [1152](https://www.urionlinejudge.com.br/judge/en/problems/view/1152) Dark Roads
### Code Forces
The challenges included in this section can all be found at https://codeforces.com/

- [1490](https://codeforces.com/problemset/problem/1490/D) D. Permutation Transformation;