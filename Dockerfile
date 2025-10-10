FROM  python:3.12
EXPOSE 8000
WORKDIR /onlineshop 
COPY requirements.txt /onlineshop
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /onlineshop 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]