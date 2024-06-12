import re


def remove_time_strings_and_tags_from_teams_transcript(input_file, output_file):
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

input_file = 'input'
output_file = 'output'

remove_time_strings_and_tags_from_teams_transcript(input_file, output_file)