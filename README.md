# ethos-mysoundpack
Collection of three Python scripts that can help in generating custom sound packs for FrSky Ethos RC Transmitters.

1. `tts_from_csv.py` which uses Mac OS `say` to generate WAV files based on the CSV content.
1. `googletts_from_csv.py` which uses the Google Cloud TTS Service to generate the WAV files based on the CSV content
1. `count_chars_in_csv.py` which counts the number of characters that will be sent to Google Cloud TTS (as the service is not free for unlimited characters per month)

## CSV File Format
All three scripts are using the CSV File format that is present in Ethos 1.5.x releases in the default soundpacks. This allows to use the provided CSV files to create your own soundpack using your preferred voice.

All CSV files need to provide a header in the first row:
```
path,text to play,options,description
```
The `path` column needs to contain the filename with the `.wav` extension, if folders are included in the path that do not exist, they will be created.

The scripts currently ignore everything provided in the `options` and `description` columns.

## Usage of `tts_from_csv.py`
The script only uses standard Python libraries and should not require any additional packages to be installed except for Python.

To run the script execute the following command:
```
python3 tts_from_csv.py --csv PATH_TO_YOUR_CSV --voice VOICE_TO_USE
```
Your will need to replace `PATH_TO_YOUR_CSV` with the path and filename for your CSV file. `VOICE_TO_USE` needs to be replaced with a supported and installed voice for the Mac OS `say` command. You can get a list of supported voices using `say -v "?"`. In case of premium and enhanced voices make sure to put the voice into `""`.

The output files will be written into the current working directory or the specified absolute path from the CSV file.

## Usage of `googletts_from_csv.py`

### Prerequisites
This script uses the Google Cloud Python library for text to speech. If not already installed you will need to install it using the following command.
```
pip3 install google-cloud-texttospeech
```
You will also need a Google Cloud account and project with Google TTS API enabled and a service account JSON key file. The Google Cloud docs can give you guidance on who to do that.

### Script usage
To run the script use the following command:
```
python3 googletts_from_csv.py --csv PATH_TO_YOUR_CSV --voice VOICE_TO_USE --language YOUR_LANGUAGE --credentials PATH_TO_JSON_KEY
```
Make sure to replace `PATH_TO_YOUR_CSV` with the path to your CSV input file. Change `VOICE_TO_USE` with your selected voice, a preview of voices is available [here](https://cloud.google.com/text-to-speech#demo). `YOUR_LANGUAGE` needs to be replaced with the language matching the voice and `PATH_TO_JSON_KEY` needs to point to your service accounts JSON keyfile for authentication.

The output files will be written into the current working directory or the specified absolute path from the CSV file.

## Usage of `count_chars_in_csv.py`
As the Google Cloud TTS service is charging per characters submitted it can be useful to get an idea of the amount of characters that will be transmitted to Google TTS, but don't worry depending on the voice it is in between 1 million and 4 million characters are free every month. The German official soundpack has less than 3 thousand characters.

```
python3 count_chars_in_csv.py --csv PATH_TO_YOUR_CSV
```
Make sure to replace `PATH_TO_YOUR_CSV` with the path to your CSV input file.

The number of characters will be printed on the console.