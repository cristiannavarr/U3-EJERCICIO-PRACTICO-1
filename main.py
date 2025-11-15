import csv
from math_operations import calculate
from data_processor import read_math_file, write_results

def main():
    print("=== Math Calculator ===")
    
    # File to read
    input_file = 'data/math_operations.csv'
    
    # Step 1: Read the file
    print("\nStep 1: Reading file...")
    operations = read_math_file(input_file)
    
    # Step 2: Do the math
    print("\nStep 2: Calculating...")
    results = []
    
    for i, op in enumerate(operations):
        operation = op['operation']
        num1 = op['num1']
        num2 = op['num2']
        
        # Calculate the result
        result = calculate(operation, num1, num2)
        results.append(result)
    
    print(f"Finished calculating {len(operations)} problems.")
    
    # Step 3: Save results
    print("\nStep 3: Saving results...")
    write_results(input_file, operations, results)
    
    print("\n=== Completed ===")

    # Preview first 10 results
    print("\nPreview of first 10 results:")
    for i, (op, result) in enumerate(zip(operations, results)):
        if i >= 10:
            break
        print(f"{op['operation']}({op['num1']}, {op['num2']}) = {result}")

# Run the program
if __name__ == "__main__":
    main()