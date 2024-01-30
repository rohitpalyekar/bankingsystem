from domain.account import Account

class AccountService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, customer_id, account_number):
        account = Account(customer_id=customer_id, account_number=account_number, balance=0.0)
        self.account_repository.save_account(account)
        return account
