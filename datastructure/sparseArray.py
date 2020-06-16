import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
string_dict = {}
results = []
def matchingStrings(strings, queries):
    
  for string in strings:
    try:
        if string_dict[string] is not None:
            string_dict[string] += 1
    except: 
        string_dict[string] = 1



  for query in queries:
    try:
        results.append(string_dict[query])
    except: 
        results.append(0)
        pass
  return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(raw_input())

    strings = []

    for _ in xrange(strings_count):
        strings_item = raw_input()
        strings.append(strings_item)

    queries_count = int(raw_input())

    queries = []

    for _ in xrange(queries_count):
        queries_item = raw_input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
