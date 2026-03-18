import sys
from datetime import datetime

if len(sys.argv) < 2:
    sys.exit("Argumento faltando.")

target_status = sys.argv[1]
current_date = datetime.now().strftime("%d/%m")

lines = sys.stdin.readlines()

for line in lines:
    if line.strip().startswith('|'):
        columns =[col.strip() for col in line.split('|')]
        
        if len(columns) >= 5 and columns[3] == target_status:
            val = columns[1]
            title = columns[2]
            
            if target_status == "Pessoal":
                new_line = f"| {val} | {title} | Recorrente | {current_date} |\n"
            else:
                new_line = f"| {val} | {title} | {current_date} |\n"
            
            sys.stdout.write(new_line)
            continue
