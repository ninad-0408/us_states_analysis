FROM python:3.10

COPY requirements.txt /
RUN pip install -r /requirements.txt

EXPOSE 8501
COPY . /app
WORKDIR /app

CMD ["streamlit", "run", "main.py"]