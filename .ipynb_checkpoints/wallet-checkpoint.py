import subprocess
import json
from constant import *
import os
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from eth_account import Account

from getpass import getpass


#mnemonic = os.getenv('MNEMONIC', 'culture envelope disagree measure until seven prevent object holiday case gentle search')

# mnemonic = 'culture envelope disagree measure until seven prevent object holiday case gentle search'

#command = f'./hd-wallet-derive/derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --{ETH} --numdrive=3 --format=json'
def derive_wallets(coin=ETH, mnemonic=menmonic, depth=3):
    command = './hd-wallet-derive/derive -g --mnemonic="culture envelope disagree measure until seven prevent object holiday case gentle search" --cols=path,address,privkey,pubkey --eth --numdrive=3 --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return keys

priv_key = Account.from_key(os.getenv("PRIVATE_KEY"))

def priv_key_to_account(coin, priv_key):
    pass
    
def create_tx():
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }

def send_tx():
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()

