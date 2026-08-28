# 文件 4：app.py
# 作用：Streamlit 網頁主界面
import streamlit as st
from data_loader import fetch_stock_data
from indicators import calculate_ma

st.set_page_config(page_title="主子的專屬看盤小工具", layout="wide")
st.title("主子的專屬看盤小工具")

symbol_input = st.sidebar.text_input("請輸入股票代碼", value="1155.KL")
btn_query = st.sidebar.button("開始查詢")

if btn_query:
    st.info(f"正在為您獲取 {symbol_input} 的行情數據...")
    data, msg = fetch_stock_data(symbol_input)
    
    if data is not None:
        processed_data = calculate_ma(data)
        st.success(msg)
        
        st.subheader("價格與均線走勢圖")
        st.line_chart(processed_data[["Close", "MA_5", "MA_20"]])
        
        st.subheader("最新行情數據明細")
        st.dataframe(processed_data.tail(10))
    else:
        st.error(msg)
