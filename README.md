# Banking System

## Overview
This is a simplified banking system implemented following clean architecture principles using Flask.

## Setup
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt

## Can Run with Docker:
docker-compose run



## Endpoints
# Create Account
Endpoint: /create_account (POST)
Parameters:
customer_id
name
email
phone_number
Response: JSON with account_id.


# Make Transaction
Endpoint: /make_transaction (POST)
Parameters:
account_id
amount
transaction_type ('deposit' or 'withdraw')
Response: JSON with success message.


# Generate Account Statement
Endpoint: /generate_account_statement (GET)
Parameters:
account_id
Response: JSON with account_statement.




