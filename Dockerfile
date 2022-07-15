FROM python:3.10

RUN pip install pyTelegramBotAPI

CMD ["python3", "main.py"]
