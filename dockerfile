FROM python:3
WORKDIR /usr/src/app

RUN python -m venv .venv
RUN . .venv/bin

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "./main.py" ] 