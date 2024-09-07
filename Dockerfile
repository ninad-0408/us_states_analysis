FROM python:3.7

COPY requirements.txt /
RUN python3 install -r /requirements.txt

EXPOSE 8501
COPY . /app
WORKDIR /app

CMD ["streamlit", "run", "main.py"]