#instructions: write ten random numbers to a file

import random
import os

def write_10_random_numbers_to_a_file():
    #first, create a sample file
    sample_file = open('samplefile.txt', 'w')
    #next let's practice lists and make a list of 10 random numbers
    my_randoms = []
    for i in range(10):
        my_randoms.append(random.randrange(1,10000, 1))
    print(my_randoms)
    #now let's append this list to the file we created
    sample_file.write(str(my_randoms))
    sample_file.close()



def main():
    write_10_random_numbers_to_a_file()

if __name__ == '__main__':
    main()