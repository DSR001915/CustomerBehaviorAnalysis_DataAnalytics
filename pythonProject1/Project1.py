import pandas as pd

df = pd.read_csv('customer_shopping_behavior.csv')

print(df.head())

print(df.info())

print(df.describe(include='all'))

print(df.isnull().sum())

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

print(df.isnull().sum())

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})

print(df.columns)

# Create a column age_group

labels = ['Young Adult', 'Adult', 'Middle-Aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q = 4, labels = labels)

print(df[['age', 'age_group']].head(10))

#Create column purchase_frequency_days

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quaterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

print(df[['purchase_frequency_days', 'frequency_of_purchases']].head(10))

print(df.columns)

print(df[['discount_applied', 'promo_code_used']].head(10))

isTrue = df['discount_applied'] == df['promo_code_used'].all()
print(isTrue)

df = df.drop('promo_code_used', axis = 1)

print(df.columns)

from sqlalchemy import create_engine
from urllib.parse import quote_plus

#MySql connection
username = "root"
password = quote_plus("Dsr@2002")
host = "127.0.0.1"
port = "3306"
database = "mydatabase"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

#Write DataFrame to MySql

table_name = "customer" # choose any table name
df.to_sql(table_name, engine, if_exists = "replace", index = False)
print("Data inserted successfullly!")

# Read back sample
result = pd.read_sql("SELECT * FROM customer LIMIT 10;", engine)
print(result)