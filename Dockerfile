FROM continuumio/anaconda3
COPY . /usr/app/
EXPOSE 8000
WORKDIR /usr/app/
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python","manage.py","runserver"]
