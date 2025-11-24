# dashboard.py
import streamlit as st
import sqlite3
import pandas as pd
import os

st.title("Green Light — Software MVP Dashboard")

DB_PATH = "greenlight.db"   # SAME NAME AS LOGGER.PY

def load_logs():
    if not os.path.exists(DB_PATH):
        st.error("Database not found. Run system first!")
        return pd.DataFrame()

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM logs ORDER BY timestamp DESC", conn)
    conn.close()

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    return df

df = load_logs()

st.subheader("Latest Logs")
st.dataframe(df)

if not df.empty:
    st.subheader("Action Distribution")
    st.bar_chart(df["action"].value_counts())