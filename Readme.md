# Vocabot AI Assistant

This Python script implements a basic AI assistant named Vocabot using various libraries. Below is a breakdown of the functionalities and features implemented in the code:

## Libraries Used
- `pyttsx3`: Text-to-speech conversion library.
- `datetime`: Library for working with dates and times.
- `speech_recognition`: Library for performing speech recognition.
- `wikipedia`: Python library to access Wikipedia articles.
- `webbrowser`: Library to control web browsers.
- `os`: Module providing a way to interact with the operating system.
- `random`: Module for generating pseudo-random numbers.
- `pywhatkit`: Library to automate WhatsApp messages.

## Features

### Initialization and Greeting
- Initializes the text-to-speech engine with `pyttsx3`.
- Greets the user based on the current time of the day (Good Morning/Afternoon/Evening/Night).

### Voice Input
- Uses the `speech_recognition` library to capture voice input from the user.

### Wikipedia Search
- If the user's query contains "wikipedia," the assistant searches Wikipedia for information and reads a summary.

### Web Browsing
- Opens various websites based on user commands, such as Google, Stack Overflow, Wikipedia, Facebook, and YouTube.

### Time Inquiry
- Tells the current time when the user asks for it.

### Code Editor Launch
- Opens Visual Studio Code using the specified file path.

### Photo Viewer
- Opens a random photo from a specified directory.

### Search
- Performs a search using the `pywhatkit` library when the user includes the keyword "search" in their query.

### Quit
- Exits the program when the user says "quit."

## How to Use
1. Install the required libraries using `pip install pyttsx3 speech_recognition wikipedia pywhatkit`.
2. Adjust the file paths and directories as needed for your system.
3. Run the script and interact with Vocabot using voice commands.

## Notes
- The script uses the default voice (index 0) from the available voices.
- Some functionalities, like playing music or handling undefined queries, are commented out or incomplete.
- The script runs in an infinite loop, continuously waiting for user commands until the user says "quit."

Feel free to modify and extend the code to suit your specific requirements or add additional features.
