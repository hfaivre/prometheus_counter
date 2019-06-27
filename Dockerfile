FROM python:3
ADD prom_counter.py /
RUN pip install prometheus_client
EXPOSE 8000
CMD [ "python", "./prom_counter.py" ]
