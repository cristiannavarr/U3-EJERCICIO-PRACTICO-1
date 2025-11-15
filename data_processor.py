import csv

def read_math_file(filename):
    # Read the math operations from CSV file
    operations = []
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        for i, row in enumerate(reader):
            if i == 0:  # skip header
                continue
            
            operation = row[0]
            num1 = float(row[1])
            num2 = float(row[2])
            
            operations.append({
                'operation': operation,
                'num1': num1,
                'num2': num2
            })

    
    print(f"Found {len(operations)} math problems in {filename}")
    return operations


def write_results(filename, operations, results):
    # Write the results to CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers
        writer.writerow(['operation', 'operand_1', 'operand_2', 'calculated_result'])
        
        # Write each operation with its result
        for i in range(len(operations)):
            op = operations[i]
            result = results[i]
            
            writer.writerow([
                op['operation'],
                op['num1'],
                op['num2'],
                result
            ])
    
    print(f"Saved {len(results)} results to {filename}")
