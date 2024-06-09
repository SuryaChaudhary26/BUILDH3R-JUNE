# Import necessary modules for interacting with the Algorand blockchain
from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams,
)

# Client to connect to localnet
algorand = AlgorandClient.default_local_net()

# Import dispenser from KMD - Key management daemon is our local net wallet/handler of keys
dispenser = algorand.account.dispenser()
print(dispenser.address)

# Create a wallet for the creator of the token and print it
creator = algorand.account.random()
#print(creator.address)

# Get account info about creator and print it
print(algorand.account.get_information(creator.address))

# Fund creator address to begin using the Algorand blockchain
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000
    )
)

# Get account info post funding 
print(algorand.account.get_information(creator.address))

# Create asset
sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total= 2000,
        asset_name="Myalgorandtoken",
        unit_name="ALGO" 
    )
)

# Extract the asset ID from the confirmation of the sent transaction and print it
asset_id= sent_txn["confirmation"]["asset-index"]
print(asset_id)

# Create reciver account
receiver_acct = algorand.account.random()
print(receiver_acct.address)

# Showcase error whithout opt-in
""" asset_transfer = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=receiver_acct.address,
        asset_id=asset_id,
        amount=50
    )
) """


#  Showcase Opt-in

#1 fund reciever account
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=receiver_acct.address,
        amount=10_000_000
    )
)

#2 Optin to the asset
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=receiver_acct.address,
        asset_id=asset_id
    )
)

#3 Send asset from creator to receiver
asset_transfer = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=receiver_acct.address,
        asset_id=asset_id,
        amount=750
    )
)

print(algorand.account.get_information(receiver_acct.address))
