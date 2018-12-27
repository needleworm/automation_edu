"""
Author : Byunghyun Ban
Last Modification : 2018.12.27.
"""
import time
import random
import os

ALPHABET_SAMPLES = "abcdefghijklmnopqrstuvwxyz"
NUMBER_SAMPLES = "0123456789"

# number of samples
NUM_SAMPLES = 2000


# a function to generate random string
def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(ALPHABET_SAMPLES)
    return result


# a function to generate random number
def random_number(length):
    result = ""
    for i in range(length):
        result += random.choice(NUMBER_SAMPLES)
    return result


# make a directory for sample files
os.popen("mkdir personal_info")
time.sleep(2)


# generating sample information
namespace = []
while len(namespace) < NUM_SAMPLES:
    filename = "personal_info/" + random_string(3) + str(random_number(5)) + ".txt"
    if filename in namespace:
        continue
    namespace.append(filename)
    outfile = open(filename, 'w')
    outfile.write("name : " + random_string(5) + "\n")
    outfile.write("age : " + str(random_number(2)) + "\n")
    outfile.write("e-mail : " + random_string(8) + "@needle.worm\n")
    outfile.write("division : " + random_string(3) + "\n")
    outfile.write("telephone : 010-" + str(random_number(4)) + "-" + str(random_number(4)) + '\n')
    outfile.write("sex : " + random.choice(["male", "female", "others"]))
    outfile.close()
