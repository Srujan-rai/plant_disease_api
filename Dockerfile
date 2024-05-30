FROM python:3.9-slim
gWORKDIR 

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]