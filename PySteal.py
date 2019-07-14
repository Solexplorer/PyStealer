from mnemonic_utils import mnemonic_to_private_key
from eth_account import Account
from random_words import RandomWords
from multiprocessing import Pool
import web3
import time


rw = RandomWords()
w = web3.Web3(web3.HTTPProvider('https://mainnet.infura.io/v3/PROJECT_ID'))
def searchPrivKey(nothing):
   for i in range(10):
    try:
        private_key = mnemonic_to_private_key(''.join(rw.random_words(count=12)))

        #From newer versions better use from_key()
        acct = Account.privateKeyToAccount(private_key)
        balance = w.eth.getBalance(acct.address)
        if int(balance) == 0:
            pass
        else:
            with open("keys.txt", "a") as myfile:
                myfile.write('\n ' + str(balance) + str(private_key) + acct.address)
    except Exception as e:
        print(e)



if __name__ == '__main__':
   pool = Pool()
   while True:
       starttime = time.time()
       result = pool.map(searchPrivKey, range(10) )
       print(time.time() - starttime)