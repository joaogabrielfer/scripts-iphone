import sys

lines = sys.stdin.readlines()

for line in lines:
    if line.strip().startswith('|'):
        columns = [col.strip() for col in line.split('|')]
        if columns[5].isnumeric():
            number = int(columns[5])
            if number > 1:
                number -= 1
            elif number == 1:
                number -= 1
                columns[4] = "Inativo"
            elif number == 0 and not columns[4] == "Inativo":
                columns[4] = "Inativo"

            columns[5] = str(number)
            line = '|'.join(columns)
            line += "\n"

    sys.stdout.write(line)
