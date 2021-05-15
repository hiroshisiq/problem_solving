import os

PATH = './problems'
content = ''

# Open base file
with open('./scripts/base_readme.md', 'r') as f:
    content += f.read()

# Get all readme.md files inside PATH and append its content
for path, dirs, files in os.walk(PATH):
    readme_list = [filename for filename in files if 'readme.md' in filename]

    if not readme_list:
        continue

    full_path_list = [os.path.join(path, readme) for readme in readme_list]
    for full_path in full_path_list:
        with open(full_path, 'r') as f:
            content += f.read()

# Write final readme to root directory
with open('./readme.md', 'w+') as f:
    f.write(content)



