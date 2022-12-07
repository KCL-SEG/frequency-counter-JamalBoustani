"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in items:
        if frequencies.get(str(i)) == None:
            frequencies[str(i)]= 1 
        else:
            frequencies[str(i)]+= 1
    return frequencies
