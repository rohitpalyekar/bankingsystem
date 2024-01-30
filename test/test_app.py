import json
import pytest
from app import app, account_repository

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_account(client):
    # Test create account endpoint
    response = client.post('/create_account', json={'customer_id': 1, 'account_number': 'A123'})
    assert response.status_code == 200

def test_make_transaction(client):
    # Test make transaction endpoint
    client.post('/create_account', json={'customer_id': 1, 'account_number': 'A123'})
    response = client.post('/make_transaction', json={'account_id': 1, 'amount': 100, 'transaction_type': 'deposit'})
    assert response.status_code == 200

def test_generate_account_statement(client):
    # Test generate account statement endpoint
    client.post('/create_account', json={'customer_id': 1, 'account_number': 'A123'})
    client.post('/make_transaction', json={'account_id': 1, 'amount': 100, 'transaction_type': 'deposit'})
    response = client.get('/generate_account_statement?account_id=1')
    assert response.status_code == 200
    assert "Account ID: 1, Balance: 100.0" in response.json['account_statement']
