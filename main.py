from hashlib import sha256
import time

# http://tcpschool.com/webbasic/bitcoin

MAX_NONCE = int(1e10)
DIFFICULTY = 5

# https://www.blockchain.com/btc/block/00000000000000000006dfdf4ae77bc817ae825858884e68c016fbf36298e793
block_number = 668861
transactions = '''
A->B:10
D->A:999
C->Z:1
'''
previous_hash = '00000000000000000006dfdf4ae77bc817ae825858884e68c016fbf36298e793'

new_hash = None

start_time = time.time()

for nonce in range(MAX_NONCE):
    text = str(block_number) + transactions + previous_hash + str(nonce)
    new_hash = sha256(text.encode('ascii')).hexdigest()

    if new_hash.startswith('0' * DIFFICULTY):
        print(f'Hash: {new_hash}')
        print(f'Nonce: {nonce}')
        break

if new_hash is None:
    print('Cannot find new hash')

print(f'Mining took {time.time() - start_time}s!')
