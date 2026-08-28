# 文件 3：indicators.py
# 作用：富途牛牛指標計算模塊
import pandas as pd

def calculate_ma(df, short_period=5, long_period=20):
    """
    計算雙均線指標（對標富途牛牛 MA 公式）
    """
    try:
        if df is None or df.empty:
            return df
        df[f"MA_{short_period}"] = df["Close"].rolling(window=short_period).mean()
        df[f"MA_{long_period}"] = df["Close"].rolling(window=long_period).mean()
        return df
    except Exception as e:
        print(f"指標計算異常: {str(e)}")
        return df
