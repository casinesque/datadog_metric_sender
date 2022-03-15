from datadog import initialize, statsd
import time

'''
The flush interval in datadog by default is 10 seconds, 
if you use a gauge metric and the metric is reported more than 
once in a flush interval, datadog agent only sends the last value ignoring the previous ones. 
'''

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

i = 0

while(1):
  i += 1
  statsd.gauge('mycustom.metric.gauge', i, tags=["environment:dev"])
  time.sleep(10)
