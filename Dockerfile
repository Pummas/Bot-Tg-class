FROM python:3.8
WORKDIR /app
ADD . .
RUN pip3 install -r requirements.txt
CMD ["python3","bot3_class.py"]