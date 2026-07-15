# Binance Futures Trading Bot (Python)

## Overview

This project is a Python-based CLI application that places BUY and SELL orders on the Binance USDT-M Futures Testnet. It is designed with a modular architecture, input validation, logging, and exception handling to provide a clean and reusable trading bot.

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports **BUY** and **SELL**
- Command Line Interface (CLI) using `argparse`
- Input validation
- Structured code architecture
- API request and response logging
- Exception handling for invalid input, API errors, and network failures

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.9+
- Binance API Key
- Binance Secret Key

---

## Installation

Clone the repository

```bash
git clone https://github.com/SanketKolhe2005/trading_bot.git
cd trading_bot
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
```

---

## How to Run

### Place a MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 110000
```

---

## Sample Output

```
ORDER REQUEST BTCUSDT BUY MARKET 0.001

Order ID: 123456789
Status: NEW
Executed Quantity: 0.001
Average Price: 108500
```

If an error occurs:

```
FAILED: Invalid order parameters
```

---

## Logging

All API requests, responses, and errors are stored in:

```
logs/trading.log
```

---

## Error Handling

The application handles:

- Invalid order type
- Invalid side
- Missing LIMIT order price
- API authentication errors
- Network failures
- Binance API exceptions

---

## Assumptions

- Binance API credentials are stored in a `.env` file.
- Internet connection is available.
- User has enabled Futures API access.

---

## Note

This project was implemented according to the assignment requirements for Binance USDT-M Futures Testnet.

During testing, authenticated requests to the legacy Binance Futures Testnet endpoint (`https://testnet.binancefuture.com`) returned HTTP **401 Unauthorized** (`APIError -2015`) with the currently available Binance API credentials. Public endpoints were accessible, indicating network connectivity was successful. The application's request signing, validation, logging, and exception handling are fully implemented and can be used with valid Binance-compatible Futures Testnet or Demo Trading API credentials.

---

## Dependencies

- requests
- python-dotenv

Install them using:

```bash
pip install -r requirements.txt
```

---

## Author

**Sanket Kolhe**

GitHub: https://github.com/SanketKolhe2005
