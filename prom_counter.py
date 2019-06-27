from prometheus_client import start_http_server, Counter
from prometheus_client.parser import text_string_to_metric_families
import random
import time
import logging
import sys
import requests
import logging
import sys

#logging
log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)


if __name__ == '__main__':
    start_http_server(8000)

    c = Counter('static_increment_counter', 'Counter that increments by 2 every 2 seconds')
    g = Counter('static_increment_gauge', 'Gauge that increments by 2 every 2 seconds')


    c_lin = Counter('linear_increment_counter', 'Counter that increments in a linear fashion 2 every 2 seconds')
    g_lin = Counter('linear_increment_gauge', 'Gauge that increments in a linear fashion every 2 seconds')
    i  = 1
    run = 0
    while True:
    	
    	log.info("*******RUN %i **********",run)

    	# Increment the counter and gauge by the same value at each run
    	c.inc(2)
    	g.inc(2)

    	# Increment the counter and gauge by an increasing increment
    	c_lin.inc(i)
    	g_lin.inc(i)

    	 # Scrape endpoint to get metric values logged to stdout
    	metrics = requests.get("http://localhost:8000/").content
    	for family in text_string_to_metric_families(metrics.decode()):
    		for sample in family.samples:
    			log.info("Name: {0} Labels: {1}  Value: {2}".format(*sample))

    	time.sleep(2)


    	i+=2
    	run+=1




        