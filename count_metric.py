'''
The flush interval in datadog by default is 10 seconds,
 if you use a gauge metric and the metric is reported more than
 once in a flush interval, datadog agent only sends the last
  value ignoring the previous ones. For count metric in contrast,
  the agent sums up all the values reported in the flush interval.
'''
from datadog import initialize, statsd
import time

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

while(1):
  statsd.increment('mycustom.count.increment', tags=["environment:dev"])
  # statsd.decrement('mia.count.decrement', tags=["environment:dev"])
  time.sleep(10)
