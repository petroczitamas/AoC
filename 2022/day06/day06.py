import os
from collections import deque

with open(os.path.join(os.path.dirname(__file__), "day06.txt"), "r") as f:
    data = f.read()

packet_start = deque(maxlen=4)
message_start = deque(maxlen=14)

packet_found = False
message_found = False

for idx, i in enumerate(data):
    packet_start.append(i)
    message_start.append(i)
    if packet_found is False and len(set(packet_start)) == 4:
        print(
            "The first start-of-packet marker is detected after",
            idx + 1,
            "characters have been processed.",
        )
        packet_found = True
    if message_found is False and len(set(message_start)) == 14:
        print(
            "The first start-of-message marker is detected after",
            idx + 1,
            "characters have been processed.",
        )
        message_found = True
        break
