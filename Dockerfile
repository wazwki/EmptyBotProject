FROM python:3.12.3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
RUN git clone https://github.com/wazwki/EmptyBotProject.git
WORKDIR /EmptyBotProject/bot_app
RUN pip install --no-cache-dir -r /EmptyBotProject/requirements.txt