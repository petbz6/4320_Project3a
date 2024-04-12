import pygal
from datetime import datetime

def generate_graph(data, chart_type, time_series, begin, end, stock_symbol):
    dates = []
    low = []
    high = []
    open = []
    close = []

    if time_series == 1:  
        time_series_data = data["Time Series (5min)"]
    elif time_series == 2:  
        time_series_data = data["Time Series (Daily)"]
    elif time_series == 3:  
        time_series_data = data["Weekly Time Series"]
    elif time_series == 4: 
        time_series_data = data["Monthly Time Series"]
    else:
        print("Invalid selection")
        return

    for date, values in time_series_data.items():
        if begin <= datetime.strptime(date, "%Y-%m-%d") <= end:
            dates.append(date)
            low.append(float(values["1. open"]))
            high.append(float(values["2. high"]))
            open.append(float(values["3. low"]))
            close.append(float(values["4. close"]))

    if chart_type == 1: 
        chart = pygal.Bar()
    elif chart_type == 2:  
        chart = pygal.Line()
    else:
        print("Invalid selection")
        return

    chart.x_labels = dates
    chart.add("Low", low)
    chart.add("High", high)
    chart.add("Open", open)
    chart.add("Close", close)

    chart.title = f"Stock Data for {stock_symbol}: {begin.strftime('%Y-%m-%d')} - {end.strftime('%Y-%m-%d')}"

    return chart.render(is_unicode=True)