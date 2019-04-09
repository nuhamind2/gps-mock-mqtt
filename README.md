# gps-mock-mqtt
Mock gps data by publishing to mqtt broker

These script generate mock gps data then publish it through mqtt broker. The gps location centered around Yogyakarta. By default it send 100 gps point updated every second (so 100 message / second)
Each point published through dedicated mqtt connection, so the server need to be able to handle 100 concurent connection (which is not very difficult). You might need to modify the script to adjust for server host, port and etc.

**patternmock.py** use paho mqtt client, which in this setup create 1 thread per connection, **patternmock2.py** use hbmqtt client which use asyncio. patternmock2 is more efficient in resource usage due to asyncio.

#### mqttbench.py
This script purpose is to benchmark mqtt broker (and the network performance). It create tenth-thousands concurrent connection to server. Each connection publish dummy in a loop without additional delay. If error related to file descriptor occur, you might need to adjust your OS fd limit. This vary between OS.
