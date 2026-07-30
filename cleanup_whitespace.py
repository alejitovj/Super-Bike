from pathlib import Path

root = Path(r'c:\Users\Alejandro\Desktop\Alejandro\Super-Bike')
allowed_extensions = {'.py', '.css', '.html', '.js', '.txt'}
skip_dirs = {'.git', 'venv'}

for path in root.rglob('*'):
    if not path.is_file():
        continue
    if any(part in skip_dirs for part in path.parts):
        continue
    if path.suffix.lower() not in allowed_extensions:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue

    had_final_newline = text.endswith(('\n', '\r'))
    newline = '\r\n' if '\r\n' in text else '\n'
    lines = text.splitlines()

    cleaned_lines = []
    prev_blank = False
    for line in lines:
        stripped = line.rstrip(' \t')
        if stripped == '':
            if not prev_blank and cleaned_lines:
                cleaned_lines.append('')
            prev_blank = True
        else:
            cleaned_lines.append(stripped)
            prev_blank = False

    while cleaned_lines and cleaned_lines[0] == '':
        cleaned_lines.pop(0)
    while cleaned_lines and cleaned_lines[-1] == '':
        cleaned_lines.pop()

    new_text = newline.join(cleaned_lines)
    if cleaned_lines and had_final_newline:
        new_text += newline

    path.write_text(new_text, encoding='utf-8', newline='')
