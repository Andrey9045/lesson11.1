# Обрезка ссылок с помощью VK
## Создание виртуального окружения
Откройте командную строку и перейдите в скачанный вами репозиторий
Перейти в директорию можно следующей командой:
```
cd C:\ваш\путь
```
Вместо C:\ваш\путь укажите фактический путь.
Далее для создания виртуального окружения введите следующую команду
```
python -m venv myvenv
```
Для активации ВО введите следующую команду
```
myvenv\Scripts\activate
```
## Подготовка к запуску скрипта - установка необходимых модулей
Далее введите следующую команду для установки необходимых модулей
```
pip install -r requirements.txt
```
## Переменные окружения
- Для выполнения скрипта нам понадобится VK API key, который можно получить зарегестрировавшись на [сайте](https://api.vk.ru), он будет выглядеть примерно так "16b61b4c16b61b4c16b61b4ca2159fe2cb116b616b61b4c7107ac133d82bb3d503b3eb3"
- Далее в папке проекта необходимо создать файл .env и прописать в нем TOKEN_VK
```
TOKEN_VK = "***"
```
Вместо ***-ваш VK API key
## Запуск скрипта
Скрипт выполняет сокращение ссылок припомощи сервиса VK.
При запуске скрипта необходимо ввсести ссылку в качестве аргумета.
```
python mein.py https://yandex.ru/
```
Скрипт распознает какая ссылка введена(обычная или сокращенная), в случае requests.exceptions.HTTPErr, выведется error.Запускается функция проверки на сокращение is_shorten_link(url, token). Скрипт разобъёт ссылку на составные части, оставит только \path и уберет из него \.
Сделает запрос к API https://api.vk.ru/method/utils.getLinkStats c PATH и заданными параметрами.
Если выявится 'error', значит ссылка не сокрашенная, если ошибка есть, ссылка сокращенная.

Если ссылка не сокращенная, то запускается функция shorten_link(url, token). Которая делает запрос API https://api.vk.ru/method/utils.getShortLink c заданными параметрами. Ресурс сократит ссылку, резкльтат выведется в консоль.

![фото](https://raw.githubusercontent.com/Andrey9045/photo/refs/heads/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-04-16%20212139.png)

Если ссылка сокращенная, то запустится функция count_clicks(url, token), которая работает аналогично функции, которая проверяет ссылку на сокращенность. Сервис посчитает кол-во переходов по ссылке, и выведет в терминал.

![фото](https://raw.githubusercontent.com/Andrey9045/photo/refs/heads/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-04-16%20212149.png)



