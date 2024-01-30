from flask import Flask, request, jsonify
from service.account_service import AccountService
from service.transaction_service import TransactionService
from service.statement_service import StatementService
from infra.account_repository import AccountRepository
from infra.sqlalchemy_session import create_session
from domain.account import Base as AccountBase
from domain.customer import Base as CustomerBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
DATABASE_URL = "postgresql://admin:admin123@postgres:5432/banking_system_test"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

AccountBase.metadata.create_all(engine)
CustomerBase.metadata.create_all(engine)

account_repository = AccountRepository(Session)
account_repository.create_tables()
account_repository.initialize_data()  # Initialize sample data on app startup
account_service = AccountService(account_repository)
transaction_service = TransactionService(account_repository)
statement_service = StatementService(account_repository)

@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.get_json()
    customer_id = data.get('customer_id')
    account_number = data.get('account_number')

    account = account_service.create_account(customer_id, account_number)
    return jsonify({'account_id': account.account_id})

@app.route('/make_transaction', methods=['POST'])
def make_transaction():
    data = request.get_json()
    account_id = data.get('account_id')
    amount = data.get('amount')
    transaction_type = data.get('transaction_type')

    transaction_service.make_transaction(account_id, amount, transaction_type)
    return jsonify({'message': 'Transaction successful'})

@app.route('/generate_account_statement', methods=['GET'])
def generate_account_statement():
    account_id = request.args.get('account_id')
    statement = statement_service.generate_account_statement(account_id)
    return jsonify({'account_statement': statement})

if __name__ == '__main__':
    app.run(debug=True)
