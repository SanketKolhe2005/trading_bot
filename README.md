# Assumptions / Notes

This project implements the Binance USDT-M Futures Trading Bot using authenticated REST API requests, including:

- Market Orders
- Limit Orders
- BUY / SELL
- CLI using argparse
- Input validation
- Logging
- Exception handling

## Testing Note

The assignment specifies the legacy Binance Futures Testnet endpoint:

https://testnet.binancefuture.com

During testing, authenticated requests to the legacy endpoint returned HTTP 401 / APIError -2015 using the currently available Binance API credentials. Public endpoints (time endpoint) were reachable successfully.

The project structure, request signing, validation, logging, and error handling are complete and can be executed with valid Binance Futures Testnet credentials.