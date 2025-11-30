import requests
import json
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

class BCFUNClient:
    """ 
    - Thsi is a minimal class for API client which is used to interact with the 
        reverse-engineered BC.FUN bet endpoint.
        
    - It has class methods that handles headers, payload generation, post requests, and bet 
        placement using the API discovered.
    """

    def __init__(self):
        """ 
        Initialize session, headers, and endpoint
        """
        self.session = requests.Session()
        self.headers = {}
        self.bet_endpoint = ""


    def set_headers(self, headers: dict):
        """
        This sets and apply headers to the session
        """
        self.headers = headers
        self.session.headers.update(headers)


    def build_bet_payload(self, bet_data: dict) -> list:
        """
        This will build the bet payload using dynamic data for subsequent request
        e.g event_id, market_id, outcome_id, stake_amount, odds, bet_type_specifier
        
        TIme library is used to generate the current time in milliseconds to validate 
        every request as recent and to make it sync with server-side event timing.
        """
        
        selection = {
            "event_id": bet_data["event_id"],
            "market_id": bet_data["market_id"],
            "outcome_id": bet_data["outcome_id"],
            "k": bet_data["odds"],
            "specifiers": "",
            "source": {
                "layout": "tile",
                "page": "/",
                "section": "Top",
                "extra": {
                    "market": "Event Plate",
                    "timeFilter": "",
                    "banner_type": "BetbyAI",
                    "tab": "1"
                }
            },
            "promo_id": None,
            "bonus_id": None,
            "timestamp": int(time.time() * 1000)
        }

        payload = [
            {
                "type": bet_data["bet_type_specifier"],
                "sum": bet_data["stake_amount"],
                "k": bet_data["odds"],
                "global_id": None,
                "bonus_id": None,
                "bet_request_id": f"{bet_data['event_id']}-1--1",
                "odds_change": "any",
                "selections": [selection]
            }
        ]

        return payload


    def _post(self, payload: dict, timeout=15):
        """
        POST requests method with safe logging and exception handling.
        """
        try:
            response = self.session.post(
                self.bet_endpoint,
                headers=self.headers,
                json=payload,
                timeout=timeout
            )

            try:
                details = json.dumps(response.json(), indent=2)
                logging.info(f"Response [{response.status_code}]: {details}")
                
                return response.json()
            
            except ValueError:
                logging.error("Non-JSON response received.")
                return {"error": "Invalid JSON", "raw": response.text}

        except requests.exceptions.RequestException as e:
            logging.error(f"Network/Session error: {e}")
            return {"error": str(e)}
        
        except Exception as e:
            logging.error(f"Unexpected exception: {e}")
            return {"error": str(e)}

    
    def place_bet(self, bet_data: dict) -> dict:
        """
        This accepts a dictionary to fully build the payload and then submits the
        bet payload to the API using the _post method.
        """
        payload = self.build_bet_payload(bet_data)
        response = self._post(payload)
        
        return response


if __name__ == "__main__":
    """ 
    Execute a sample bet on the BCFUN API with python BC_FUN.py
    """
    client = BCFUNClient()

    # Set headers (authentication, device spoofing, etc.)
    client.set_headers({
        "Content-Type": "application/json",
        "Authorization": "Bearer Token",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36",
        "Accept": "*/*",
        "Origin": "https://bc.fun",
        "Referer": "https://bc.fun/"
    })
    
    # place bet API
    client.bet_endpoint = (
            "https://api-k-c7818b61-623.sptpub.com/api/v2/coupon/brand/"
            "2103509236163162112/bet/place"
        )

    # payload - bet data argument for subsequent request
    bet_data = {
        "event_id": "2598967605851201569",
        "market_id": "1",
        "outcome_id": "1",
        "stake_amount": "150",
        "odds": "1.25",
        "bet_type_specifier": "1/1"
    }

    response = client.place_bet(bet_data)
