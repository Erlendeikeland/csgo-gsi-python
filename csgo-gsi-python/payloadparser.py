import gamestate

class PayloadParser:
    def parse_payload(self, payload, gamestate):
        try:
            gamestate.map.name = payload["map"]["name"]
        except:
            pass
