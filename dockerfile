FROM PYTHON:3.8-alpine
RUN mkdir /app
ADD . /app
WoRKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
