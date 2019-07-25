import re
import collections

book = open("book.txt", "r")
text= book.read()
book.close()

# I know this is cheating but apostrophe is sucks
text_a = text.lower().replace('\'','APOS')

words = re.findall(r'\w+', text_a)

counter=collections.Counter(words)

for (key, value) in counter.items():
 
 # I remember that was a condition print only words that repeated in text at least once. 
 # If I am wrong then if clause is unnecessary
  if value > 1:
   print(key.replace('APOS','\''),  value, " times")
