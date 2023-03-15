# Тестовое задание

## 1. Конфигурация

Для запуска программы вам потребуются установленные python 3.10+ (https://www.python.org/downloads/) и git 
(https://git-scm.com/downloads). На windows исполняемые файлы нужно добавить в системную переменную PATH.
(https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows).

Все действия выполняются в терминале:

1. Перейти в директорию для загрузки проекта. Например:
    ```shell
    # Linux
    cd ~
    
    # Windows
    cd /d C:/
    ```
2. Клонировать и перейти в репозиторий с проектом:
    ```shell
    git clone https://github.com/Azqii/carbis_test_task.git
   
    cd carbis_test_task
    ```
3. Создать виртуальное окружение:
    ```shell
    # Linux
    python3 -m venv venv
   
    # Windows
    python -m venv venv
    ```
4. Активировать виртуальное окружение:
    ```shell
    # Linux
    source ./venv/bin/activate
   
    # Windows
    ./venv/Scripts/activate.bat
    ```
5. Установить зависимости:
    ```shell
    pip install -r requirements.txt
    ```

## 2. Запуск

Все действия выполняются в терминале, в корневой папке проекта, с активированным виртуальным окружением (см. пункт 1.4)

1. Перед ***первым*** запуском выполнить:
    ```shell
    python ./src/main.py createdb    
    ```
2. Запуск:
    ```shell
    python ./src/main.py start    
    ```