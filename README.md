# Desktop-Assistant
Short and Cute Siri you can presume!! Blood-Group: Python


## Introduction

This article was published as a part of the Data Science Blogathon.

Introduction
How cool is it to build your own personal assistants like Alexa or Siri? It’s not very complicated and can be easily achieved in Python. Personal digital assistants are capturing a lot of attention lately. Chatbots are common in most commercial websites. With growing advancements in artificial intelligence, training the machines to tackle day-to-day tasks is the norm.

Voice based personal assistants have gained a lot of popularity in this era of smart homes and smart devices. These personal assistants can be easily configured to perform many of your regular tasks by simply giving voice commands. Google has popularized voice-based search that is a boon for many like senior citizens who are not comfortable using the keypad/keyboard.

For building any voice based assistant you need two main functions. One for listening to your commands and another to respond to your commands. Along with these two core functions, you need the customized instructions that you will feed your assistant.

The first step is to install and import all the necessary libraries. Use pip install to install the libraries before importing them.

1. pip install SpeechRecognition
2. pip install wikipedia
3. pip install gTTS
4. pip install ecapture
5. pip install ipython
6. pip install pyinstaller
7. pip install selenium
8. pip install playsound #use 1.22

# Following are some of the key libraries used in this program:

1. The SpeechRecognition library allows Python to access audio from your system’s microphone, transcribe the audio, and save it.
2. Google’s text-to-speech package, gTTS converts your audio questions to text. The response from the look-up function that you write for fetching answer to the question is converted to an audio phrase by gTTS. This package interfaces with Google Translate’s API.
3. Playsound package is used to give voice to the answer. Playsound allows Python to play MP3 files.
4. Web browser package provides a high-level interface that allows displaying Web-based pages to users. Selenium is another option for displaying web pages. However, for using this you need to install and provide the browser-specific web driver.
5. Wikipedia is used to fetch a variety of information from the Wikipedia website.
6. Wolfram|Alpha is a computational knowledge engine or answer engine that can compute mathematical questions using Wolfram’s knowledge base and AI technology. You need to fetch the API to use this package.
