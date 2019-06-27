# prometheus_counter
A simple app exposing an ever increasing prometheus counter

## Description
This is a simple application exposing a prometheus /metrics endpoint on `localhost:8000`.
The application increments a [prometheus counter](https://github.com/prometheus/client_python#counter) every 2 seconds, increasing the value of 2.

The application has been packaged in a container, which you can pull from here :https://cloud.docker.com/repository/registry-1.docker.io/hfaivresaito/prometheus_counter_test
