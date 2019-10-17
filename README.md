# csgo-gsi-python

python library to interact with CS:GO Game State Integration.

## Simple usage
Copy the **gamestate_integration_GSI.cfg** file to *C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg*
```py
server = GSIServer(("127.0.0.1", 3000), "S8RL9Z6Y22TYQK45JB4V8PHRJJMD9DS9")
server.start_server()

server.get_info("map", "name")
server.get_info("player", "state", "flashed)
```
