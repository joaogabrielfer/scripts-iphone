import sys

if len(sys.argv) < 2:
    sys.exit("Usage: cat file.md | python3 delete_row.py <title>")

target_title = sys.argv[1].strip()

lines = sys.stdin.readlines()

for line in lines:
    if line.strip().startswith('|'):
        columns = [col.strip() for col in line.split('|')]
        # Make sure it's a data row and the title matches (Index 2)
        if len(columns) >= 4 and target_title == columns[2]:
            continue # Skip this line (deleting it)
    
    # Write back to Standard Output (returned to Shortcuts)
    sys.stdout.write(line)
