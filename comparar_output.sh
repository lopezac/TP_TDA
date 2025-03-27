#!/bin/bash

# Directory containing the generated results
dir_generados="Resultados"

# Directory containing the expected results
dir_esperados="tests/Esperados"

# Loop through each file in the generated directory that contains "es" in its name
for arch_genereado in "$dir_generados"/*es*; do
    # Extract the filename
    filename=$(basename "$arch_genereado")
    
    # Define the corresponding expected file path
    expected_file="$dir_esperados/$filename"
    
    # Check if the expected file exists
    if [ -f "$expected_file" ]; then
        # Compare the generated file with the expected file
        diff "$arch_genereado" "$expected_file"
        
        # Check the result of the diff command
        if [ $? -eq 0 ]; then
            echo "Comparison for $filename: OK"
        else
            echo "Comparison for $filename: FAIL"
        fi
    else
        echo "Expected file $expected_file not found"
    fi
done