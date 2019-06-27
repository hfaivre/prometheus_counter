# prometheus_counter
A simple app exposing an ever increasing prometheus counter

## Description
This is a simple application exposing a prometheus /metrics endpoint on `localhost:8000`.
The application exposes 4 metrics
1. `static_increment_counter`, a [prometheus counter](https://github.com/prometheus/client_python#counter) incremented every 2 seconds by 2.
2. `static_increment_gauge`, a [prometheus gauge](https://github.com/prometheus/client_python#gauge) incremented every 2 seconds by 2.
3. `linear_increment_counter`, a [prometheus counter](https://github.com/prometheus/client_python#counter) incremented in a linear fashion every 2 seconds.
4. `linear_increment_gauge`, a [prometheus gauge](https://github.com/prometheus/client_python#gauge) incremented in a linear fashion every 2 seconds.

The application has been packaged in a container, which you can pull from here :https://cloud.docker.com/repository/registry-1.docker.io/hfaivresaito/prometheus_counter_test
