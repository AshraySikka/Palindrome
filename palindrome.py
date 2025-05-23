s1 = input("Enter a Word / Phrase: ")
s2 = s1.casefold()
s2 = s2.replace(' ','')
r = s2[::-1]
if r == s2:
    print(s1,'is Palindrome')
else:
    print('The new Palindrome is: ',s2+r)
