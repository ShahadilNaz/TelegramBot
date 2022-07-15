FROM python:3.10

RUN pip install pyTelegramBotAPI

COPY main.py .

CMD ["python3", "main.py"]
