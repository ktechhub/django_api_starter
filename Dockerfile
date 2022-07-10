FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "setup.wsgi"]