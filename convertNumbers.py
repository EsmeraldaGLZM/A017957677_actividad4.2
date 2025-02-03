import sys

import time

def read_numbers_from_file(filename):
    """Lee un archivo y extrae los valores numéricos, ignorando líneas inválidas."""
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                numbers.append(int(line.strip()))
            except ValueError:
                print(f"Dato inválido: {line.strip()} - Omitiendo")
    return numbers

def decimal_to_binary(number):
    """Convierte un número decimal a binario."""
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

def decimal_to_hexadecimal(number):
    """Convierte un número decimal a hexadecimal."""
    if number == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while number > 0:
        remainder = number % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        number //= 16
    return hexadecimal

def write_results(filename, results, elapsed_time):
    """Escribe los resultados en un archivo de texto."""
    with open(filename, 'w', encoding='utf-8') as file:
        for decimal, binary, hexadecimal in results:
            file.write(f"Decimal: {decimal} | Binario: {binary} | Hexadecimal: {hexadecimal}\n")
        file.write(f"Tiempo de Ejecución: {elapsed_time:.6f} segundos\n")

def main():
    """Función principal que lee un archivo, convierte los números y muestra los resultados."""
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py archivo_con_datos.txt")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_filename = "ConvertionResults.txt"
    
    start_time = time.time()
    numbers = read_numbers_from_file(input_filename)
    if not numbers:
        print("No se encontraron números válidos en el archivo.")
        sys.exit(1)
    
    results = [(num, decimal_to_binary(num), decimal_to_hexadecimal(num)) for num in numbers]
    elapsed_time = time.time() - start_time
    
    for decimal, binary, hexadecimal in results:
        print(f"Decimal: {decimal} | Binario: {binary} | Hexadecimal: {hexadecimal}")
    print(f"Tiempo de Ejecución: {elapsed_time:.6f} segundos")
    
    write_results(output_filename, results, elapsed_time)

if __name__ == "__main__":
    main()
