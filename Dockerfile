FROM python:3.8
WORKDIR /Users/Asus tuf/Desktop/cloud_assigment2
COPY . .
RUN pip install nltk
CMD ["python", "./cloud_assigment2.py"]
