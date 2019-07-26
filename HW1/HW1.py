import re
import collections

book = open("book.txt", "r")
text= book.read()

wordsWithApos = re.findall(r"\w+\'\w+", text.lower())

wordsAll=text.lower().split()

wordsWithoutApos = ' '.join([w for w in wordsAll if w not in wordsWithApos])

words = re.findall(r"\w+", wordsWithoutApos)
words += wordsWithApos

counter=collections.Counter(words)


for (key, value) in counter.items() :

 # I remember that was a condition print only words that repeated in text at least once.
 # If I am wrong then if clause is unnecessary
  if value > 1:
   print(key,  value, " times ")
