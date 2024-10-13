# Required Python Libraries

- [Python]([https://www.python.org/))
- requests : **pip install requests** : Simplifies making HTTP requests, allowing developers to send and receive data from web services with easy-to-use functions for GET, POST, and other HTTP methods.
- PIL (Pillow) : **pip install Pillow** : Imaging library that adds support for opening, manipulating, and saving various image file formats, making it easier to work with images.
- pyqrcode : **pip install pyqrcode** : Allows for the generation of QR codes, providing a simple interface to create and save QR codes as SVG, PNG, or other image formats.
- nltk : **pip install nltk** : NLTK (Natural Language Toolkit) library is a powerful platform for working with human language data, offering tools for text processing, linguistic analysis, and natural language processing (NLP).
- yt_dlp : **pip install yt_dlp** : Allows for the downloading of videos from various video platforms, including YouTube.
- pyperclip : **pip install pyperclip** : Allows for handling of copying text to the user's clipboard.
- gtts (Google Text-to-Speech) : **pip install gtts** : a Python library and CLI tool to interface with Google Translate's text-to-speech API.

## Pre-Installed Python Libraries

- random: Provides functions to generate random numbers, select random elements, and perform random operations like shuffling sequences.
- os: Provides a way to interact with the operating system, allowing for tasks like file and directory manipulation, environment management, and running system commands.
- time: Provides functions for working with time, including retrieving the current time, pausing execution, and formatting time data.
- subprocess: Allows to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
- platform: Access various platform-specific parameters and functions to identity the operating system the script is operating on.
- tkinter : **pip install tk** : Allows for the easiest creation of Graphic User Interfaces (GUI)
- pypng : **pip install pypng** : Pure Python implementation for reading and writing PNG files, and allowing the ability to create and manipulate PNG images easily.
- logging : **pip install logging** : Flexible framework for tracking and recording log messages, monitoring, and troubleshooting.

## Library Usage

- random: Generate random words based on a sample, numbers, or a set of words
- os: Determine if a file exists, obtain current directory, and append/join text
- time: Halt code
- nltk: Download and load a large list of words.
- logging: Suppress the NLTK output.
- requests: Retrieve **words** from a dictionary.
- pyqrcode: Generate a fully functional QR codes.
- pypng: Save a newly generated QR code as a PNG file to the current available directory.
- PIL (pillow): Specifically used the Image class | Convert the QR code image to a color format, create a new image with a transparent background, and save the modified image.
- subprocess: Open the generated QR code file with the default application for the specific operating system.
- platform: Used to determine the current operating system so that the appropriate command can be executed.
- yt_dlp: Download the specified video and merge the video and audio streams based on the chosen format.
- tkinter: Graphic User Interfaces (GUI) such as checkbox/toggles, labels, textboxes, etc.
- pyperclip: Copying text to the user's clipboard. 
- gtts (Google Text-to-Speech): Convert simple text strings to robotic words/pronounications using Google's Text-to-Speech API.
