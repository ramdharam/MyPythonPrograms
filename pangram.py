def pangram(s):
    if len(s) == 0:
        return 'not pangram'
    for i in xrange(97,124):
        if chr(i) not in s.lower():
            return 'not pangram'
    return 'pangram'


s='We promptly judged antique ivory buckles for the next prize'
print(pangram(s))