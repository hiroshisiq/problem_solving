import subprocess

def run_script(script_path: str, input_path: str) -> str:
    with open(input_path, 'r') as input_file:
        result: CompletedProcess = subprocess.run(
            ['python', script_path],
            stdin=input_file,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

    result.check_returncode()
    return result.stdout.decode("utf-8")

def read_text(path: str) -> str:
    with open(path, 'r') as file:
        text = file.read()
    return text
