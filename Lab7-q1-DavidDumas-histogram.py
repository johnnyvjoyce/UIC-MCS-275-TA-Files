"""Histogram example for debugging"""
# MCS 275 Spring 2021 - David Dumas

def update_char_histogram(s,hist = dict()):
    """Take a string `s` and look at the non-space characters in it. If `hist` is not given,
    compose a histogram of the characters in `s` and return it.  If `hist` is given, assume it contains
    a histogram of another part of the same text, and update it to take into account the text in `s`."""
    for c in s:
        if c.isspace():
            continue
        if c not in hist:
            hist[c] = 0
        hist[c] += 1
    return hist


print("Histogram of 'first line example':")
h = update_char_histogram("first line example") # no hist given, so start from scratch
print(h)
print("Histogram of previous line and 'renewed interest in debugging':")
h = update_char_histogram("renewed interest in debugging",h)
print(h)
print("Histogram of the word 'Mississippi':") # no hist given, so start from scratch
h = update_char_histogram("Mississippi")
print(h) # Unexpected output here; why isn't the default argument of dict() honored?