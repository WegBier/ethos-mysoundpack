import csv
import argparse

def count_characters_to_speak(csv_path):
    # Read the CSV file
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        characters = 0
        for row in reader:
            text_to_speak = row['text to play']
            # Count the characters in the sentence/word to speak
            characters = characters + len(text_to_speak)
        print(f"This CSV File will submit {characters} characters for Cloud TTS!")

def main():
    parser = argparse.ArgumentParser(description="Count the characters for Cloud TTS")
    parser.add_argument("--csv", help="Path to the CSV file")
    args = parser.parse_args()

    # Call the function to count the characters to speak
    count_characters_to_speak(args.csv_file)

if __name__ == "__main__":
    main()
