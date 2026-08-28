# 文件 2：data_loader.py
# 作用：免費抓取行情數據模塊
import pandas as pd
import yfinance as yf

def fetch_stock_data(symbol="1155.KL", period="1y"):
    """
    抓取股票歷史行情數據
    """
    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period=period)
        if df.empty:
            return None, "未獲取到有效數據，請檢查代碼是否正確"
        return df, "數據獲取成功"
    except Exception as e:
        return None, f"獲取數據異常: {str(e)}"
