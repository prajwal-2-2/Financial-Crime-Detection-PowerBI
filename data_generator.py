import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# 1. SETUP THE TOOLS
fake = Faker()
Faker.seed(101) 

print("--- Banking System Started: Generating Transactions ---")

# 2. DEFINE SETTINGS
num_customers = 200    
num_transactions = 5000 

# 3. CREATE CUSTOMERS (Now with City!)
customer_list = []

for _ in range(num_customers):
    customer_profile = {
        'CustomerID': fake.uuid4()[:8],       
        'Name': fake.name(),                   
        'Age': random.randint(18, 90), 
        'City': fake.city(),                   # <--- NEW COLUMN ADDED
        'Primary_IP': fake.ipv4(),             
        'Risk_Score': random.randint(300, 850) 
    }
    customer_list.append(customer_profile)

df_customers = pd.DataFrame(customer_list)
print(f"✅ Created {num_customers} Customer Profiles with Cities")


# 4. CREATE TRANSACTIONS 
transactions = []

for _ in range(num_transactions):
    
    # Pick a random customer
    customer = df_customers.sample(1).iloc[0]
    
    # Transaction details
    tx_date = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23))
    amount = round(random.uniform(5.0, 10000.0), 2) 
    merchant = fake.company()
    category = random.choice(['Groceries', 'Tech', 'Travel', 'Jewelry', 'Utilities'])
    
    # Fraud Logic
    is_fraud = 0 
    fraud_type = 'None'
    tx_ip = customer['Primary_IP'] 

    if random.random() < 0.05: 
        tx_ip = fake.ipv4() 
        is_fraud = 1        
        fraud_type = 'Account Takeover'

    if amount > 8000 and amount % 1000 == 0:
        is_fraud = 1
        fraud_type = 'Money Laundering'

    # Save transaction (Adding Customer City here)
    transactions.append({
        'TransactionID': fake.uuid4(),
        'Timestamp': tx_date,
        'CustomerID': customer['CustomerID'],
        'Name': customer['Name'],
        'Customer_Location': customer['City'], # <--- NEW COLUMN MAPPED HERE
        'Amount': amount,
        'Merchant': merchant,
        'Category': category,
        'Transaction_IP': tx_ip,            
        'Primary_IP': customer['Primary_IP'], 
        'Is_Fraud': is_fraud,
        'Fraud_Reason': fraud_type
    })

# 5. SAVE TO CSV
df_transactions = pd.DataFrame(transactions)
df_transactions.to_csv('Bank_Transactions.csv', index=False)

print("✅ Success! 'Bank_Transactions.csv' has been UPDATED.")