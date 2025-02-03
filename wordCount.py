import sys

import time


def read_words_from_file(filename):
    """Lee un archivo y extrae palabras, ignorando líneas vacías o inválidas."""
    words = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            clean_line = line.strip()
            if clean_line:
                words.extend(clean_line.split())
    return words

def count_word_frequencies(words):
    """Cuenta la frecuencia de cada palabra en la lista."""
    unique_words = []
    frequencies = []
    
    for word in words:
        if word in unique_words:
            index = unique_words.index(word)
            frequencies[index] += 1
        else:
            unique_words.append(word)
            frequencies.append(1)
    
    return list(zip(unique_words, frequencies))

def write_results(filename, word_counts, elapsed_time):
    """Escribe los resultados en un archivo de texto."""
    with open(filename, 'w', encoding='utf-8') as file:
        for word, count in word_counts:
            file.write(f"Palabra: {word} | Frecuencia: {count}\n")
        file.write(f"Tiempo de Ejecución: {elapsed_time:.6f} segundos\n")

def main():
    """Función principal que lee un archivo, cuenta palabras y muestra los resultados."""
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py archivo_con_datos.txt")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_filename = "WordCountResults.txt"
    
    start_time = time.time()
    words = read_words_from_file(input_filename)
    if not words:
        print("No se encontraron palabras en el archivo.")
        sys.exit(1)
    
    word_counts = count_word_frequencies(words)
    elapsed_time = time.time() - start_time
    
    for word, count in word_counts:
        print(f"Palabra: {word} | Frecuencia: {count}")
    print(f"Tiempo de Ejecución: {elapsed_time:.6f} segundos")
    
    write_results(output_filename, word_counts, elapsed_time)

if __name__ == "__main__":
    main()