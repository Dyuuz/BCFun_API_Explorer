# BC.FUN API Explorer

## Overview
This project demonstrates a minimal Python client for interacting with the reverse-engineered BC.FUN betting API. It allows placing a bet by providing `event_id`, `market_id`, `outcome_id`, `stake_amount`, `odds`, and `bet_type_specifier`. The `place_bet` function handles payload generation, request submission, and response parsing.

## Tools & Methods Used
- **Browser DevTools** to inspect network requests and capture API endpoints.
- **Python `requests` library** for sending HTTP POST requests.
- **JSON** for payload construction and response handling.
- Session headers (including authorization token) where required to authenticate requests.

## API Request & Response
- **Request:** JSON payload containing bet details and selections, including timestamps in milliseconds for server synchronization, event_id, market_id, outcome_id, stake_amount, odds, bet_type_specifier.
- **Response:** JSON object from the API indicating success, failure, or errors such as insufficient funds, expired_token etc

## Example header:
**The is a sample header used for placing a bet via the BCFUN API:**

```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Token",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36",
    "Accept": "*/*",
    "Origin": "https://bc.fun",
    "Referer": "https://bc.fun/"
}
```

## Example payload:
**The is a sample full payload used for placing a bet via the BCFUN API:**

```json
{
  "type": "1/1",
  "sum": "150",
  "k": "1.25",
  "global_id": null,
  "bonus_id": null,
  "bet_request_id": "2598967605851201569-1--1",
  "odds_change": "any",
  "selections": [
    {
      "event_id": "2598967605851201569",
      "market_id": "1",
      "outcome_id": "1",
      "k": "1.25",
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
      "promo_id": null,
      "bonus_id": null,
      "timestamp": 1764490156935
    }
  ]
}
```
## Example payload for place_bet function:
**The is a sample payload for placing 1x2 bet**

```json
{
    "market_type": "1x2",
    "event_id": "2604063478348128301",
    "market_id": "1",
    "outcome_id": "1",
    "stake_amount": "150000",
    "odds": "3.25",
    "bet_type_specifier": "1/1"
}
```

**The is a sample payload for placing total bet**

```json
{
    "market_type": "total",
    "total": "1.5",
    "event_id": "2604063478348128301",
    "market_id": "18",
    "outcome_id": "12",
    "stake_amount": "150000",
    "odds": "3.25",
    "bet_type_specifier": "1/1"
}
```

**The is a sample payload for placing handicap bet**

```json
{
    "market_type": "hcp",
    "handicap": "-3.25",
    "event_id": "2604063478348128301",
    "market_id": "16",
    "outcome_id": "1715",
    "stake_amount": "150000",
    "odds": "7.0",
    "bet_type_specifier": "1/1"
}
```

## Example Response:
**The is a sample success message for 1x2 bet**

```json
{
  "accepted": [
    {
      "bet_request_id": "2598967605851201569-1--1",
      "bet_id": "2606902585277420123",
      "bonus_id": null
    }
  ],
  "error": []
}
```

**The is a sample success message for total bet**
```json
{
  "accepted": [
    {
      "bet_request_id": "2604063478348128301-18-total=1.5-12",
      "bet_id": "2607900395879674442",
      "bonus_id": null
    }
  ],
  "error": []
}
```

**The is a sample success message for handicap bet**
```json
{
  "accepted": [
      {
          "bet_request_id": "2604063478348128301-16-hcp=-3.25-1715",
          "bet_id": "2607894871545090778",
          "bonus_id": null
      }
  ],
  "error": []
}
```

**Example of failed response:**
```json
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

```json
{
  "error": "expired_token",
  "error_description": "Token expired."
}
```

```json
{
  "error": "invalid_token",
  "error_description": "Illegal base64 character 20"
}
```

## How to Run

1. Install **Python 3.10+**.

2. Clone the repository:

```bash
git clone https://github.com/Dyuuz/BCFun_API_Explorer.git
```

3. Open `BC_FUN.py` and update the authorization token in `set_headers`.

4. Run the script:

```bash
python BC_FUN.py
```