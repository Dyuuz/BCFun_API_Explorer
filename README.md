# BC.FUN API Explorer

## Overview
This project demonstrates a minimal Python client for interacting with the reverse-engineered BC.FUN betting API. It allows placing a test bet by providing `event_id`, `market_id`, `outcome_id`, `stake_amount`, `odds`, and `bet_type_specifier`. The `place_bet` function handles payload generation, request submission, and response parsing.

## Tools & Methods Used
- **Browser DevTools** to inspect network requests and capture API endpoints.
- **Python `requests` library** for sending HTTP POST requests.
- **JSON** for payload construction and response handling.
- Session headers (including authorization token) where required to authenticate requests.

## API Request & Response
- **Request:** JSON payload containing bet details and selections, including timestamps in milliseconds for server synchronization.  
- **Response:** JSON object from the API indicating success, failure, or errors such as insufficient funds, expired_token etc

**Example payload:**
```json
[
  {
    "type": "1/1",
    "sum": "150",
    "k": "1.25",
    "bet_request_id": "2598967605851201569-1--1",
    "odds_change": "any",
    "selections": [
      {
        "event_id": "2598967605851201569",
        "market_id": "1",
        "outcome_id": "1",
        "k": "1.25",
        "timestamp": 1764490156935
      }
    ]
  }
]
```

**Example response:**
```
 {
  "accepted": [],
  "error": [
    {
      "bet_request_id": "2598967605851201569-1--1",
      "code": 2001,
      "message": "Not enough funds to make a bet. Top up your account to bet more!",
      "bet_id": "2606858774924898916",
      "alt_stake": null,
      "vip_request_available": null
    }
  ]
}
```