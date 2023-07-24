import yaml
import sys
from yaml.loader import SafeLoader
from googletrans import Translator

'''
pip install googletrans==3.1.0a0     
pip install pyyaml==6.0b1
'''

def yaml_translator(src, lang, key='translation'):
    new_file = open(f'{lang}.yaml', 'w', encoding='utf-8')
    file = open(src, 'r', encoding='utf-8')
    file = file.read()
    data = yaml.load(file, Loader=SafeLoader)
    print('[translating', end='')
    try:
        for item in data:
            translation = item[key]
            translator = Translator()
            result = translator.translate(translation, dest=lang)
            item[key] = result.text
            print('.', end='')
        print(yaml.dump(data, allow_unicode=True), file=new_file)
        print(']')
        print('Translation is over')
    except:
        print('ex')

if __name__ == '__main__':
    from_lang = sys.argv[1]
    to_langs = sys.argv[2].split(',')

    for l in to_langs:
        yaml_translator(f'{from_lang}.yaml', l)
