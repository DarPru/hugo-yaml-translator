## При первом запуске

Работаем через *power shell*

1. Создаем папку с названием проекта
2. Помещаем туда файл **main.py**
3. Введим команду:

````
python -m venv venv
````

4. Прописываем команду

````
venv/Scripts/activate
````

После этой команды в самом начале строки перед именем вашего компьютера и адреса до папки должна появится зеленая надпись *venv* 

5. Построчно пишем команды ниже, ждем установки библиотек

````
pip install googletrans==3.1.0a0     
pip install pyyaml==6.0b1
````

6. Запускаем скрипт

## Как запустить скрипт

Все пункты выше кроме 4 и 6 больше повторять не надо. При повторном использовании, можно нажимать стрелку вверх чтобы не набирать команды из пунктов 4 и 6.

Чтобы запустить скрипт пишем:

````
python main.py ru en,uz,uk,az
````

- Ключевое слово **python** неизменно
- **main.py** - название скрипта, тоже менять не нужно
- После *main.py* ставим ПРОБЕЛ и пишем код языка **с которого идет перевод**
- После кода языка ставим еще ПРОБЕЛ и далее через запятую **без пробела** перечисляем языки на которые нужен перевод

> **!!Важно!!** - файл исходного языка должен лежать в этой же папке. Например, я перевожу с русского, значит файл **ru.yaml** будет лежать в корневой рядом с main.py


Коды языков можно посмотреть [тут](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages)


## Если выходит ошибка прав доступа к Power Shell

1. Запускаем Power Shell от имени администратора
2. Прописываем

````
Set-ExecutionPolicy RemoteSigned
````