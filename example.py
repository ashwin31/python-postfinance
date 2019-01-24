from postfinance import PostFinance

client = PostFinance(psp_id="garagefoxDEMO", sha_password="SecretSig123?!")
payment = client.payments.create("test_order", "15", "CHF")

print(payment)
