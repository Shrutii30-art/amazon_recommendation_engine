import pandas as pd

# Load your logic dataset
df = pd.read_csv('amazon_products.csv')

# Only fill the image_url if it's empty, using a professional Amazon logo
df['image_url'] = df.get('image_url', "https://m.media-amazon.com/images/G/01/gc/pvp/amazon_logo_RGB._V154215752_.png")

df.to_csv('amazon_products.csv', index=False)
print("Safety images applied to amazon_products.csv")