from random import *
from deep_translator import GoogleTranslator

def make_a_poetry(lista, vari):
    palavras = []
    for i in range(vari):
        palavras.append(choice(lista))
        if len(palavras) > 1:
            while(palavras[i-1] == palavras[i]):
                palavras[i] = choice(lista)     

    return palavras

noun = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla",
]
verb = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles",
]
adjective = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening",
]
preposition = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]
adverb = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously",
]


nouns = make_a_poetry(noun,3)
verbs = make_a_poetry(verb,3)
adjectives = make_a_poetry(adjective,3)
preps = make_a_poetry(preposition,2)
adverbs = make_a_poetry(adverb,1)

if "aeiou".find(adjectives[0]) != -1:  
    artigo = "An"
else:
    artigo = "A"

poema = (
    f"{artigo} {adjectives[0]}\n\n"
    f"{artigo} {adjectives[0]} {nouns[0]} {verbs[0]} {preps[0]} the {adjectives[1]} {nouns[1]}\n"
    f"{adverbs[0]}, the {nouns[0]} {verbs[1]}\n"
    f"the {nouns[1]} {verbs[2]} {preps[1]} a {adjectives[2]} {nouns[2]}"
)

print(poema+'\n\n')

poema_port = GoogleTranslator(source='auto', target='pt').translate(poema)

print(poema_port)
