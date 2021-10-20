import pdb
import leons_functions
import random
import time
import rpoems

pdb.set_trace()

corpus = rpoems.build_corpus(limit=2000)
poem = rpoems.couplet_rhyming_poem(corpus)
print(poem)

print(random.randint(15, 2047))
print(time.sleep(6))
print(random.randint(15, 2047))
#testNum1 = int(input('Type NUM1'))

#resultVar = test_z(testNum1)
#print(resultVar)


print(leons_functions.dice())