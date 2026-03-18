import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Argumento faltando.")
    exit()

target_title = sys.argv[1]

output = []
outputs = []
lines = sys.stdin.readlines()

for line in lines:
    if line.strip().startswith('|'):
        columns = [col.strip() for col in line.split('|')]
        if columns[3] == target_title:
            output.append(columns[1])  
            output.append(columns[2])  
            if target_title == "Pessoal":
                output.append("Recorrente")  
            output.append(datetime.now().strftime("%d/%m"))
    output_str = "|".join(output)
    outputs.append(output_str)

print(outputs)
