# Подготовка модели для предсказания сердечных приступов

1. Анализ содержится в файле `notebook.ipynb`
2. Приложение в директории `app`
3. Результат предсказания модели в `result/predictions.csv`


Для запуска приложения необходимо:
1. перейти в директорию `app/backend`
2. Для сборки образа выполните `docker build --tag rfcapp .`
3. Для запуска API выполните команду `docker run --rm -it -p 8020:8000 --name app rfcapp`


Есть 2 способа взаимодействия с API:
1. Через swagger веб интерфейс:
   1. Перейдите на страницу `http://localhost:8020/docs` 
   2. Затем нажмите на `/api/predict/csv`.
   3. Нажмите на кнопку `Try it out`.
   4. Выбирите csv-файл с тестовыми данными.
   5. Нажмите `Execute` и загрузите файл.
   6. Открыть полученный файл.
2. Через CURL:
   1. выполнить команду
   ```commandline
   curl -v -X POST "http://localhost:8020/api/predict/csv" -F "file=@./datasets/heart_test.csv" -o result.csv
   ```
   2. Открыть файл `result.csv`