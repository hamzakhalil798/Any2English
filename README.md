# Any2English -  Multi-Lingual Video to English Dub with Lip Sync

This project is made in collaboration with [@waleed-27](https://github.com/waleed-27)

## Overview

The Multi-Lingual Video Dubber is a powerful tool designed to dub videos in various languages to English while ensuring lip sync. This GitHub repository contains the necessary code and resources to achieve this task. It utilizes several libraries and models, including Whisper for language translation, Tortoise TTS for text-to-speech conversion with customizable voices, and Wav2Lip for accurate lip synchronization. Please note that due to resource requirements, the current version only supports small videos.


## How it Works

1. **Audio Extraction**: The first step of the process involves extracting the audio from the input video file.

2. **Language Translation**: The extracted audio is then passed through Whisper, a language translation library, to convert it to English.

3. **Text-to-Speech Conversion**: Tortoise TTS is employed to convert the English text into speech. By default, the Tom voice is used, but users have the option to choose from a selection of other voices.

4. **Lip Synchronization**: Wav2Lip, a lip synchronization model, is used to sync the generated English speech with the input video, ensuring that the dubbed video's lip movements match the spoken words.


## Requirements

Due to resource-intensive processes, the current version supports only small videos. To use the tool, follow these steps:

1. Upload your video and audio files to Google Drive.
2. Use the provided notebook on Google Colab.
3. Follow the easy steps outlined in the notebook to generate the English-dubbed video with lip sync.

## Usage

To use this tool, simply follow these steps:

1. Clone this repository to your local machine or access the notebook on Google Colab.
2. Upload your video and audio files to your Google Drive.
3. Open the provided notebook and follow the instructions for dubbing your video.


## Results


**Input**


https://github.com/hamzakhalil798/Any2English/assets/103629235/191d8e6d-43ff-46d5-9893-92079d7c8c02





https://github.com/hamzakhalil798/Any2English/assets/103629235/9d8926c7-a39e-48c3-8237-72018d666529




**Output**


https://github.com/hamzakhalil798/Any2English/assets/103629235/988bb82b-6c18-4453-b2b5-194bbf03b0c1



https://github.com/hamzakhalil798/Any2English/assets/103629235/bc4d49f1-db23-41e6-b453-c18215873539


## Acknowledgements

- [Whisper](https://example-link-to-whisper.com) - The speech translation library used for translating audio to English.
- [Tortoise TTS](https://example-link-to-tortoise-tts.com) - The Text-to-Speech library used for generating audio.
- [Wav2Lip](https://example-link-to-wav2lip.com) - The lip syncing library used for synchronizing the voice to the input video.

## Contributing

Contributions to this project are welcome. If you find any issues or want to add new features, feel free to open a pull request.


## TODOs

- [ ] Allow bigger video files to be uploaded
- [ ] Dub into other languages


