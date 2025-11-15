import csv

def read_math_file(filename):
    # Leer las operaciones matemáticas
    operations = []
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        for i, row in enumerate(reader):
            if i == 0:  # omitir header
                continue
            
            operation = row[0]
            num1 = float(row[1])
            num2 = float(row[2])
            
            operations.append({
                'operation': operation,
                'num1': num1,
                'num2': num2
            })

    
    print(f"Se encontró {len(operations)} operaciones en {filename}")
    return operations


def write_results(filename, operations, results):
    # Escribir los resultados en el CSV
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Actualizar el header
        writer.writerow(['operation', 'operand_1', 'operand_2', 'calculated_result'])
        
        # Escribir cada operación con su resultado
        for i in range(len(operations)):
            op = operations[i]
            result = results[i]
            
            writer.writerow([
                op['operation'],
                op['num1'],
                op['num2'],
                result
            ])
    
    print(f"Se guardaron {len(results)} resultados en {filename}")
