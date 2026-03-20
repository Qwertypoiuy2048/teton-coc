# # bank_account.py

# def create_account(name, opening_balance=0):
#     """
#     Return a new account represented as a dict:
#       {"name": name, "balance": int, "transactions": list}
#     If opening_balance != 0, record ("opening_balance", opening_balance).
#     Notice this is a TUPLE () rather than a LIST []. 
#     A tuple is just an immutable version of a list.
#     """
#     # TODO: validate name and opening_balance when appropriate
#     acct = { 
#         "name": name,
#         # store integer balance
#         "balance": 0,
#         # transaction list
#         "transactions": [],
#     }
#     if opening_balance != 0:
#         # TODO: apply opening balance and record transaction
#         acct["balance"] = opening_balance
#         acct["transactions"].append(("opening_balance", opening_balance))
#     return acct

# def deposit(account, amount):
#     """
#     Add amount to account["balance"] and record ("deposit", amount).
#     - amount must be a positive integer; otherwise raise ValueError.
#     - modify account in-place and return True.
#     """
#     # TODO: implement deposit rules
#     if amount <= 0:
#         raise ValueError

#     account["balance"] += amount
#     account["transactions"].append(("deposit", amount))
#     return True
    

# def withdraw(account, amount):
#     """
#     Subtract amount from account["balance"] and record ("withdraw", amount).
#     - amount must be a positive integer and <= balance; otherwise raise ValueError.
#     - modify account in-place and return True.
#     """
#     # TODO: implement withdraw
#     if amount <= 0 or amount > account["balance"]:
#         raise ValueError
#     account["balance"] -= amount
#     account["transactions"].append(("withdraw", amount))
#     return True


# def transfer(from_account, to_account, amount):
#     """
#     Transfer amount from from_account to to_account.
#     - both accounts must be valid account dicts (created by create_account)
#     - amount must be positive integer and <= from_account balance
#     - on success: mutate both accounts, record ("transfer_out", amount)
#       in from_account and ("transfer_in", amount) in to_account, then return True.
#     - on failure: raise ValueError without mutating accounts.
#     """
#     # TODO: implement transfer safely (validate before mutating)
#     try:
#         assert isinstance(from_account, dict)
#         assert isinstance(to_account, dict)
#     except AssertionError:
#         raise ValueError

#     if amount <= 0 or amount > from_account["balance"]:
#         raise ValueError
#     from_account["balance"] -= amount
#     from_account["transactions"].append(("transfer_out", amount))
#     to_account["balance"] += amount
#     to_account["transactions"].append(("transfer_in", amount))
#     return True



# def account_str(account):
#     """
#     Return a readable single-line summary like "Alice: 100"
#     """
#     # TODO: create and return the string
#     return f"{account['name']}: {account['balance']}"

# # acct = create_account("Leo", opening_balance=30)
# # s = account_str(acct)
