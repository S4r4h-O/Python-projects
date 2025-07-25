import pandas as pd
from pdf_gen import generate_receipt_pdf

df = pd.read_csv("articles.csv", dtype={"id": str})


class Products:
    def __init__(self, product_id):
        self.product_name = df.loc[df["id"] == product_id, "name"].squeeze()
        self.product_price = df.loc[df["id"] == product_id, "price"].squeeze()
        self.stock = df.loc[df["id"] == product_id, "in stock"].squeeze()
        self.product_id = product_id

    def product_info(self):
        product_name = self.product_name
        
        return f"""
        Product bought: {product_name}
        Price: {self.product_price}
        """

    def generate_receipt(self):
        generate_receipt_pdf(self.product_name, self.product_price)
        

    def update_stock(self):
        stock = df.loc[df["id"] == self.product_id, "in stock"] = self.stock - 1
        df.to_csv("articles.csv", index=False)


print(df)

user_product = input("Select a product to buy: ")
product = Products(user_product)
print(product.product_info())
product.generate_receipt()
product.update_stock()
