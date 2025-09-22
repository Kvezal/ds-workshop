# Подготовка модели для предсказания сердечных приступов

1. Анализ содержится в файле `notebook.ipynb`
2. Приложение в директории `app`
3. Результат предсказания модели в `result/predictions.csv`


Для запуска приложения необходимо:
1. перейти в директорию `app/backend`
2. Выполнить команду `docker build --tag rfcapp .`
3. Выполнить команду `docker run --rm -it -p 8020:8000 --name app rfcapp`
4. После запуска докер контейнера перейдите на страницу `http://localhost:8020/docs`


Есть 2 способа взаимодействия с API:
1. Через swagger:
   1. Затем нажмите на `/api/predict/csv`.
   2. Нажмите на кнопку `Try it out`.
   3. Выбирите csv-файл с тестовыми данными.
   4. Нажмите `Execute` и загрузите файл.
   5. Открыть полученный файл.
2. Через CURL:
   1. выполнить команду
   ```commandline
   curl -v -X POST "http://localhost:8020/api/predict/csv" -F "file=@./datasets/heart_test.csv" -o result.csv
   ```
   2. Открыть файл `result.csv`