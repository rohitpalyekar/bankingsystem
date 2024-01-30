from sqlalchemy.orm import Session
from domain.account import Account
from domain.customer import Customer

class AccountRepository:
    def __init__(self, session: Session):
        self.session = session

    def save_account(self, account):
        self.session.add(account)
        self.session.commit()

    def find_account_by_id(self, account_id):
        return self.session.query(Account).filter_by(account_id=account_id).first()

    def find_accounts_by_customer_id(self, customer_id):
        return self.session.query(Account).filter_by(customer_id=customer_id).all()

    def create_tables(self):
        Account.__table__.create(self.session.bind)
        Customer.__table__.create(self.session.bind)

    def initialize_data(self):
        # Add sample data initialization
        customer = Customer(name='John Doe', email='john.doe@example.com', phone_number='123-456-7890')
        self.session.add(customer)
        self.session.commit()

        account = Account(customer_id=customer.customer_id, account_number='A123', balance=0.0)
        self.session.add(account)
        self.session.commit()
