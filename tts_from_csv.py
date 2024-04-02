import csv
import os
import subprocess
import argparse

def create_wav_files_from_csv(csv_path, voice):
    # Read the CSV file
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filename = row['path']
            text_to_speak = row['text to play']
            if filename and text_to_speak:
                # Extract the directory path from the filename
                directory, _ = os.path.split(filename)
                
                # Create the directory if it does not exist
                if directory and not os.path.exists(directory):
                    os.makedirs(directory)
                
                # Create the WAV file using macOS `say` command with specified voice
                subprocess.run(['say', '-v', voice, '--data-format=LEF32@22050', '-o', filename, text_to_speak])
                print(f"Created {filename} with text: {text_to_speak}")

def main():
    parser = argparse.ArgumentParser(description="Create WAV files from a CSV file using macOS TTS (say command)")
    parser.add_argument("--csv", help="Path to the CSV file")
    parser.add_argument("--voice", help="Voice to use for TTS (e.g., Alex, Victoria, Fred, etc.)")
    args = parser.parse_args()

    # Call the function to create WAV files
    create_wav_files_from_csv(args.csv, args.voice)

if __name__ == "__main__":
    main()
