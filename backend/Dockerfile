# select souce image where container run

FROM  python:3.9-slim

#defile the workDIR

WORKDIR /app

#copy the code into container DIR

COPY . /app

#run the dependency services

RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000

EXPOSE 5000

#run the container

CMD ["python","app.py"]




