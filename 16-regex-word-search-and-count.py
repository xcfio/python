import re

text = "Python is great. I love Python programming. Python is easy."
word = "Python"

matches = re.findall(word, text)
print("Found:", matches)
print("Count:", len(matches))
