from tradingview_ta import TA_Handler, Interval, Exchange

Stock_Name = input("Enter Stock Ticker Symbol: ").upper()
Stock_Name = TA_Handler(
    symbol= Stock_Name,
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY
)
print(Stock_Name.get_analysis().summary)
