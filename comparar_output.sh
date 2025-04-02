#!/bin/bash

# Los colores que usamos para imprimir en pantalla
RED='\033[0;31m'
GREEN='\033[0;32m'
NO_COLOR='\033[0m'

# Directory containing the generated results
dir_generados="Resultados"

# Directory containing the expected results
dir_esperados="tests/Esperados"

if [ ! -d "$dir_esperados" ]; then
    mkdir "$dir_esperados"
fi

# Loop through each file in the generated directory that contains "es" in its name
for arch_genereado in "$dir_generados"/*es*; do
    # Extract the filename
    filename=$(basename "$arch_genereado")
    
    # Define the corresponding expected file path
    expected_file="$dir_esperados/$filename"
    
    # Check if the expected file exists
    if [ -f "$expected_file" ]; then
        # Compare the generated file with the expected file
        echo -e "\nDiferencias entre $arch_genereado y $expected_file"
        diff "$arch_genereado" "$expected_file"
        
        # Check the result of the diff command
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}Ninguna! :)${NO_COLOR}"
        else
            echo -e "${RED}Las de arriba :(${NO_COLOR}"
        fi
    else
        echo "Expected file $expected_file not found"
    fi
done