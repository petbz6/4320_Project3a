import requests

# API KEY: 3ZGSJPRQA5AJFQ63

def get_stock_data(time_series, stock_symbol_input):
    while True:
        if time_series == 1:
            function = 'TIME_SERIES_INTRADAY&interval=5min'
        elif time_series == 2:
            function = 'TIME_SERIES_DAILY'
        elif time_series == 3:
            function = 'TIME_SERIES_WEEKLY'
        elif time_series == 4:
            function = 'TIME_SERIES_MONTHLY'
        else:
            print("Invalid time series selection.")
            return None

        url = f'https://www.alphavantage.co/query?function={function}&symbol={stock_symbol_input}&apikey=3ZGSJPRQA5AJFQ63'
        
        r = requests.get(url)
        
        if r.status_code == 200:
            data = r.json()
            if "Error Message" in data:
                print("Invalid stock symbol. Please enter a valid stock symbol.")
            else:
                return data



# Get chart function prompting users for desired chart type
def get_chart_type():
    while True:
        print("\nSelect the chart type:")
        print("1. Bar")
        print("2. Line")
        chart_type_input = input("Enter selection (1-2): ")
        if chart_type_input in ["1", "2"]:
            return int(chart_type_input)
        else:
            print("Invalid input. Please enter either 1 or 2.")

# Function prompting users for desired time series function
def get_time_series():
    while True:
        print("\nSelect the time series function:")
        print("1. INTRADAY")
        print("2. DAILY")
        print("3. WEEKLY")
        print("4. MONTHLY")
        time_series_function_input = input("Enter time series options (1-4): ")
        if time_series_function_input in ["1", "2", "3", "4"]:
            return int(time_series_function_input)
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
