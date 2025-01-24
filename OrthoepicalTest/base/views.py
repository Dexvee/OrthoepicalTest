from django.shortcuts import render
from OrthoepicalTest.settings import STATIC_ROOT
import json, random


def index_view(request):
    if not request.session.get('words', ''):
        with open((STATIC_ROOT + '/OrthoepicalDictionary.json'), 'r', encoding='utf-8') as file:
            request.session['words'] = json.load(file)
            return render(request, 'base/index.html')
    else:
        words = list(request.session['words'].values())
        words = sum(words, [])
        random.shuffle(words)
        words = ';'.join(words[0:20])
            
        return render(request, 'base/index.html', {'words': words})


def dict_view(request):
    if not request.session.get('words', ''):
        with open((STATIC_ROOT + '/OrthoepicalDictionary.json'), 'r', encoding='utf-8') as file:
            request.session['words'] = json.load(file)
            return render(request, 'base/dict.html')
    else:
        words = request.session['words']
        context = {
            'nouns': words['Существительные'],
            'verbs': words['Глаголы'],
            'adjectives': words['Прилагательные'],
            'participles': words['Причастия'],
            'adverbs': words['Деепричастия'],
        }
        
        return render(request, 'base/dict.html', context=context)

