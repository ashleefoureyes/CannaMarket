from load_dataframes import close_dataframe
from pandas_datareader import data, wb
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bkcharts import Scatter, output_file, show, Horizon, Line, TimeSeries


# heatmap to visualize correlation FIX ALL THIS CORRELATION


correlated = close_dataframe.corr()
correlated_matrix = correlated.as_matrix()

print(correlated_matrix)



N = 3
factors = ["WEED","ACB" "APH"]
x = []
y = []
colors = []

for i in range(N):
    for j in range(N):
        x.append(factors[j])
        y.append(factors[i])
        cor = correlated_matrix[i,j]
        rgb = (int(abs(cor) * 255), 0, int((1 - abs(cor)) * 255))
        colors.append('#%02x%02x%02x' % rgb)

p2 = figure(x_range=factors, y_range=factors)
p2.rect(x, y, color=colors, width=1, height=1)
output_file("correlation_heatmap.html")





