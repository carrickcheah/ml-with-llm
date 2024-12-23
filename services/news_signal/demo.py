import pandas as pd

# Read the CSV file
df = pd.read_csv('./data/cryptopanic_news.csv')

# Convert the 'title' column to a list
news = df['title'].tolist()

# Print the first 5 titles
print(news[:5])
