FROM python:3.12
EXPOSE 5000
WORKDIR /app
ENV FLASK_APP=app.py
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]