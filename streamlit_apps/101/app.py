import streamlit as st
import pandas as pd
import altair as alt

# Read data from CSV file
df = pd.read_csv("stock_prices.csv")

# Filter data by stock name
def filter_data(stock_name):
    return df[df["Stock"] == stock_name]

# Create bar chart
def create_bar_chart(stock_name):
    data = filter_data(stock_name)
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X("Date:T", axis=alt.Axis(title="Date")),
        y=alt.Y("Close:Q", axis=alt.Axis(title="Closing Price")),
        color=alt.Color("Stock:N", legend=alt.Legend(title="Stock"))
    ).properties(width=600, height=400, title=f"{stock_name} Closing Prices (Bar Chart)")
    return chart

# Create line chart
def create_line_chart(stock_name):
    data = filter_data(stock_name)
    chart = alt.Chart(data).mark_line().encode(
        x=alt.X("Date:T", axis=alt.Axis(title="Date")),
        y=alt.Y("Close:Q", axis=alt.Axis(title="Closing Price")),
        color=alt.Color("Stock:N", legend=alt.Legend(title="Stock"))
    ).properties(width=600, height=400, title=f"{stock_name} Closing Prices (Line Chart)")
    return chart

# Streamlit app
def main():
    st.title("Apple and Tesla Stock Prices")
    stock_names = ["Apple", "Tesla"]
    stock_name = st.sidebar.selectbox("Select a stock", stock_names)
    chart_type = st.sidebar.radio("Select a chart type", ["Bar Chart", "Line Chart"])
    if chart_type == "Bar Chart":
        chart = create_bar_chart(stock_name)
    else:
        chart = create_line_chart(stock_name)
    st.altair_chart(chart, use_container_width=True)

if __name__ == "__main__":
    main()
