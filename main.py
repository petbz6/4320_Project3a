import stock_query
import date
import graph

while True:
    print("Stock Data Visualizer")
    print("--------------------------- \n")

    stock = stock_query.get_stock()
    chart_type = stock_query.get_chart_type()
    time_series = stock_query.get_time_series()
    start, end = date.main()
    data = stock_query.get_stock_data(time_series, stock)
    graph.generate_graph(data, chart_type, time_series, start, end)

    response = input("Would you like to view more stock data? Press 'y' to continue: ")
    if response != "y":
        break

# Reads the first column of the stocks.csv file to get the stock symbols
def get_stock_symbols():
    stock_symbols = []
    with open("stocks.csv", newline='') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for row in csvFile:
            stock_symbols.append(row[0])
    return stock_symbols