# do export PYTHONPATH=$PYTHONPATH:$(pwd)
# so this code could see app
# then use this dude just like normal app.py


import timeit
import sys
import copy

from app import main


if __name__ == "__main__":
    attempts = []
    attempts_amount = 100


    with open("/dev/null", "w") as sys.stdout:

        for i in range(attempts_amount):
            start = timeit.timeit()
            main()
            end = timeit.timeit()
            attempts.append(end - start)

    
    
    sys.stdout = open("/dev/stdout", "w")

    M = sum(attempts) / attempts_amount
    print(f"median time for {attempts_amount} attempts:", M)

