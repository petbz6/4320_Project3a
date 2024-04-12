from datetime import datetime
from flask import Flask, render_template, request
import csv
import stock_query
import date
import graph

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        stock_symbol = request.form["stock_symbol"].upper()
        chart_type = int(request.form["chart_type"])  
        time_series = int(request.form["time_series"])
        start = datetime.strptime(request.form["start"], "%Y-%m-%d")
        end = datetime.strptime(request.form["end"], "%Y-%m-%d")
        data = stock_query.get_stock_data(time_series, stock_symbol)
        
        # After initially loading the page, the layout will consist of the default html structure
        # Once clicking submit button with the proper information filled, the layout will switch to display the generated graph
        if data is not None:
            graph_output = graph.generate_graph(data, chart_type, time_series, start, end, stock_symbol)
            return render_template("index.html", show_graph=True, graph_output=graph_output, stock_symbols=get_stock_symbols())
        else:
            return render_template("index.html", show_graph=False, stock_symbols=get_stock_symbols())
   
    return render_template("index.html", show_graph=False, stock_symbols=get_stock_symbols())

# Reads the first column of the stocks.csv file to get the stock symbols
def get_stock_symbols():
    stock_symbols = []
    with open('stocks.csv', newline='') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for row in csvFile:
            stock_symbols.append(row[0])
    return stock_symbols

if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1', port=5000)
