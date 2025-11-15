import csv
from math_operations import calculate
from data_processor import read_math_file, write_results

def main():
    print("=== Calculadora ===")
    
    # Archivo que se usará
    input_file = 'data/math_operations.csv'
    
    # Paso 1: Leer el archivo
    print("\nPaso 1: Leyendo el archivo...")
    operations = read_math_file(input_file)
    
    # Paso 2: Resolver las operaciones
    print("\nPaso 2: Calculando...")
    results = []
    
    for i, op in enumerate(operations):
        operation = op['operation']
        num1 = op['num1']
        num2 = op['num2']
        
        # Obtener el resultado
        result = calculate(operation, num1, num2)
        results.append(result)
    
    print(f"Se terminó de calcular {len(operations)} problemas.")
    
    # Paso 3: Guardar los resultados
    print("\nStep 3: Guardando resultados...")
    write_results(input_file, operations, results)
    
    print("\n=== Listo ===")

    # Ver los primeros 10 resultados
    print("\nVer primeros 10 resultados:")
    for i, (op, result) in enumerate(zip(operations, results)):
        if i >= 10:
            break
        print(f"{op['operation']}({op['num1']}, {op['num2']}) = {result}")

# Run the program
if __name__ == "__main__":
    main()