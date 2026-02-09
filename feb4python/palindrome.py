# palindrome is a number ,sequence, word that reads the same forward an backward

def palindrome(a):
     if a==a[::-1]:
      print('it is palindrome')
     else:
      print('not a palindome')

palindrome("level")
palindrome("levels")
palindrome('madam')
palindrome('12345')
palindrome('121')

    
