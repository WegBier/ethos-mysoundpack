import csv
import os
import argparse
from google.cloud import texttospeech

def synthesize_text(text, output_file, voice, language_code):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()
    # Set the input text
    synthesis_input = texttospeech.SynthesisInput(text=text)
    # Set the voice parameters (customize as needed)
    voice_params = texttospeech.VoiceSelectionParams(
        language_code=language_code, name=voice
    )
    # Set the audio file type
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )
    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice_params, audio_config=audio_config
    )
    # Save the audio content to the output file
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
    print(f"Created {output_file} with with text: {text}")

def create_wav_files_from_csv(csv_path, voice, language_code):
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
                
                # Create the WAV file using Google Cloud TTS
                synthesize_text(text_to_speak, filename, voice, language_code)

def main():
    parser = argparse.ArgumentParser(description="Create WAV files from a CSV file using Google Cloud TTS")
    parser.add_argument("--csv", required=True, help="Path to the CSV file")
    parser.add_argument("--voice", required=True, help="Voice to use for TTS (e.g., en-US-Wavenet-A, en-US-Wavenet-B, etc.)")
    parser.add_argument("--credentials", required=True, help="Path to Google Application Credentials JSON file")
    parser.add_argument("--language", default="en-US", help="Language code (default: en-US)")
    args = parser.parse_args()

    # Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = args.credentials

    # Call the function to create WAV files
    create_wav_files_from_csv(args.csv, args.voice, args.language)

if __name__ == "__main__":
    main()
