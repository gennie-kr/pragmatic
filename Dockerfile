FROM python:3.9.0
WORKDIR /home/

RUN git clone https://github.com/gennie-kr/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SELECT_KEY=django-insecure-=(u9g(cwspv(*n_j8&xhscd4m_lql%-^)mlomeo=)i_jdjhyq#" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
