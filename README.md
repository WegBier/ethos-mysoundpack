# ethos-mysoundpack
Small python script to create FrSky ETHOS soundpacks.

It takes a CSV file as input and will use Mac OS "say" command to create the output files. It accepts the ETHOS format CSV file and can be used to regenerate the shipped soundpacks, as well as creating any additional sounds.

Usage:
```
python3 tts_from_csv.py $inputCSVFile $Voice
```
To get a list of available voices execute:
```
say -v "?"
```

This also contains my additional sounds in German as a basis, but as you can specify the voice it can be used for any language.