class FuturesSales:
    # todo import modules
    import pandas as pd
    import numpy as np
    import tkinter as tk

    # ----------------------------- plotting data on graph

    def __init__(self, url):
        self.sales_data = self.pd.read_csv(url)
        self.product_price = None




# - - - - - - - - - - - - todo main model
    def future_sales_predict(self, features):
        """
        :return: a prediction of futures product units sales
        """
        # ----------------------------- machine learning modules
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression

        x = self.np.array(self.sales_data.drop(["Sales"], axis=1))
        y = self.np.array(self.sales_data["Sales"])

        xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                        test_size=0.2,
                                                        random_state=42)

        model = LinearRegression()
        model.fit(xtrain, ytrain)
        d = round(model.predict(features)[0])
        return f"expected units to be sold :{d}" \
               f"\nexpected profit : {d*self.product_price}$"




# - - - - - - - - - - - - - - -  todo windows GUI
    def window_init(self):
        """
        intiate an input window for the ad spending details
        """
        # continue the data opening method
        import tkinter as tk
        wind = tk.Tk()
        features = []

        wind.geometry('500x300')
        wind.title("future sales predecitions")

        labels = [tk.Label(wind, text="TV ads spending:"), tk.Label(wind, text="NewsPaper Ads spending:"),
                  tk.Label(wind, text="Radio ads spending:")]
        entries = [tk.Entry(wind), tk.Entry(wind), tk.Entry(wind)]
        for label, entry in zip(labels, entries):
            label.pack()
            entry.pack()

        def commando():
            features.append([int(element.get()) for element in entries])

        def call_function():
            commando()
            print(self.future_sales_predict(features))
            wind.destroy()

        tk.Button(wind, text='Predict', command=call_function).pack(expand=True)
        wind.mainloop()


# - - - - - - - - - - -- - - - -
    def start_here(self):
        """
        intiate a window for the product price input
        """
        self.price_windo = self.tk.Tk()
        self.price_windo.geometry('300x150')
        self.price_windo.title("Product Price Input")
        self.tk.Label(self.price_windo, font='arial 12 bold', text='Product Price').pack()
        self.price_entry = self.tk.Entry(self.price_windo, font='arial 12')
        button = self.tk.Button(self.price_windo, text="Confirm Price", command=self.on_button)
        self.price_entry.pack()
        button.pack()
        self.price_windo.mainloop()

    def on_button(self):
        self.product_price = int(self.price_entry.get())
        self.price_windo.destroy()
        self.window_init()





# - - - - - - - - - - - - todo graph plotting
    def graph_plotting(self, y_axis: str):
        """
        :param y_axis: the y-axis in the graph
        :return: a graph of Sales and y_axis input
        """
        # plotting modules
        import plotly.express as px

        figure = px.scatter(data_frame=self.sales_data, x="Sales", y=y_axis,
                            size=y_axis, trendline="ols")
        figure.show()




# - - - - - - - - - - - - todo additional methods
    def check_null(self):
        """
        :return: return if any of the data has no values
        """
        return self.sales_data.isnull().sum()

    def check_correlation(self, column: str):
        """
        :param column: the data we would like to check its correlation
        :return: check correlation between Sales and the input column
        """
        correlation = self.sales_data.corr()
        return correlation[column].sort_values(ascending=False)
