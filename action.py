import sys
import printdb
from printdb import *


def run(actions_path, repo):
    with open(actions_path) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            splitedLine = line.split(",")
            product_id = splitedLine[0]
            delta = splitedLine[1]
            actor_id = splitedLine[2]
            date = splitedLine[3]

            # Determine if it's sale or supply
            if '-' in delta:
                tran_type = 'sale'
            else:
                tran_type = 'supply'
            repo.reflect_transaction(actor_id, product_id, delta, date, tran_type)

            line = fp.readline()
            cnt += 1

    # # update when exit

if __name__ == '__main__':
    actions_path = sys.argv[1]
    repo = Repository()
    run(actions_path, repo)
    #atexit.register(repo._close)
    printdb.doprint()
