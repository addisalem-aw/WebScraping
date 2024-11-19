import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a GET request to the website
url = 'https://addisalem-aw.github.io/Products/'  
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Extract product data (e.g., name, price)
products = []
for product_div in soup.find_all('div', class_='product'):  # Adjust class based on actual site
    name = product_div.find('h2').text
    price = product_div.find('span', class_='price').text
    products.append({'name': name, 'price': price})

# Step 3: Convert data to a DataFrame for easy manipulation
df = pd.DataFrame(products)

# Clean and preprocess data
df['price'] = df['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

# Step 4: Sort the data by price
df_sorted = df.sort_values(by='price', ascending=False)

# Step 5: Output the sorted data
print(df_sorted)
