# Verificando os virtual envs existentes
# conda info --envs

# Criação do virtual env no conda (pra facilitar)
# conda create - -name chatBotWhatsApp python = 3.6
# conda activate chatBotWhatsApp

# Instalação de pacotes necessários

# pip install chatterbot
# pip install spacy
# pip install pyautogui
# pip install opencv-python
# pip install pynput

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download
import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep

download("en_core_web_sm")


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


chatbot = ChatBot("Celso", tagger_language=ENGSM)

conversa = [
    "Ola, bom dia",
    "Sim, tudo bem, bom dia pra você também",
    "Quem é você",
    "Eu sou um chatbot para whatsapp",
    "O que você faz? ",
    "Eu tento responder as perguntas com alguma lógica",
    "E funciona?",
    "Não sei... responde você"
]
