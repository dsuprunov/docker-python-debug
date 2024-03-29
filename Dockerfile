FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

CMD ["uvicorn", "src.service.main:app", "--host", "0.0.0.0", "--port", "8888", "--reload"]
