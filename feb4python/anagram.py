# anagram means two strig are angarms if they contain same character same count but order not atter
# ex = listen=silent
# race = care

a='silent'
b='listen'
if sorted(a)==sorted(b):
    print('anagram')
else: 
    print('not a anagram')

