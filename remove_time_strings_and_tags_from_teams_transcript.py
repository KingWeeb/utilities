import os
import re

def remove_v_and_custom_strings(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            # Remove UUID/number-number pattern
            clean_line = re.sub(r'[a-f0-9\-]{36}/\d+-\d+', '', line)
            # Remove only the letter 'v' in <v name> tags but retain the name
            clean_line = re.sub(r'<v\s+([^>]+)>', r'<\1>', clean_line)
            # Remove </v> tags
            clean_line = re.sub(r'</v>', '', clean_line)
            file.write(clean_line)

def get_file_name_without_extension(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

def process_folder(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    for file in files:
        input_file = os.path.join(input_folder, file)
        # Create a systematic name for the output file
        base_name = get_file_name_without_extension(input_file)
        output_file = os.path.join(output_folder, f'{base_name}_cleaned.vtt')
        
        print(f'Processing {input_file} -> {output_file}')
        remove_v_and_custom_strings(input_file, output_file)

# Example usage
input_folder = './vtt'
output_folder = './vtt_out'

process_folder(input_folder, output_folder)