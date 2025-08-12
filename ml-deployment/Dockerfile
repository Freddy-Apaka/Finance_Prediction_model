# Use a slim python base
FROM python:3.10-slim

# set workdir
WORKDIR /app

# copy requirement and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy app and model
COPY ./app ./app
COPY ./model ./model
COPY example_client.py ./

# expose port
EXPOSE 80

# default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
