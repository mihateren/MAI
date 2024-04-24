import pandas as pd


a, b = map(int, input().split())
c, d = map(int, input().split())
data = pd.read_csv('data.csv')
print(data[(a <= data['x']) & (data['x'] <= c) & (d <= data['y']) & (data['y'] <= b)])