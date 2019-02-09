import logging
import asyncio
import time

from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_1, QOS_2


async def main(loop):
    allClient = []
    total_client = 0
    for count in range(100):
        Clients = [MQTTClient(config=dict(keep_alive=900))
                              for n in range(100)]
        task = [loop.create_task(
            c.connect("ws://127.0.0.1:9010")) for c in Clients]
        a = await asyncio.gather(*task)
        allClient.append(Clients)
        total_client += len(a)
        print(total_client)
    while True:
        total_msg = 0
        for Clients in allClient:
            task = [loop.create_task(c.publish("test",b"lorem ipsum",QOS_1)) for c in Clients]
            a = await asyncio.gather(*task)
            total_msg += len(a)
            print(total_msg)
            print(time.time())

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.run_forever()
