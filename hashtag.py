import string

stroka = input("Введіть свій рядок: ")
for x in string.punctuation:
    stroka = stroka.replace(x, "")
words = stroka.split()
words = [w.capitalize() for w in words]
hashtag = "#" + "".join(words)
hashtag = hashtag[:140]

print(hashtag)
