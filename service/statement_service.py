class StatementService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)

        if account:
            return f"Account ID: {account.account_id}, Balance: {account.get_balance()}"
        else:
            return "Account not found"
