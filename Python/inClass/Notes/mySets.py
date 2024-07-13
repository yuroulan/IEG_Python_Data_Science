# python set we use {}
# set does not allow duplicate'
# set is not ordered (items not retain its position)
# set is not index (like 0,1,2,3,4, ...)
# set is modifiable

fruits = {"apple", "orange", "mango", "apple", "banana", "grapes", "apple"}
print(fruits)
print('1' * 50)
# fruits is an object or instance inside a set class


# selection and indexing
# print(fruits[0]) # -->> cannot because its not subscriptable

# cannot select item using index
# can iterate using for loop

# for fruit in fruits:
#     print(fruit, end=" ")
# print('2' * 75)

# # modifiable
# fruits.add("durian")
# print(fruits)
# print('3' * 75)

# # update is not practical
# # fruits[2] = "rambutan"
# # if want to update, drop the old fruit and add new fruit

# # drop a fruit
# fruits.remove("grapes")
# print(fruits)
# print('4' * 75)

# # can use pop but pop will randomly remove object
# fruits.pop()
# print(fruits)
# print('5' * 75)

# NLP -->> National Language Processing
# NLTK

# overseafruits = {"apple", "orange", "banana", "mango", "grapes"}
# localfruits = {"durian", "rambutan", "cempedak", "mangosteen", "banana"}

# print(overseafruits.union(localfruits)) # print all the fruits
# print('-' * 75)

# print(overseafruits.intersection(localfruits))  # banana
# print('-' * 75)

# print(overseafruits.difference(localfruits)) # all except banana
# print('-' * 75)

# print(localfruits.difference(overseafruits))
# print('-' * 75)

# favouritefruits = {"durian", "rambutan", "mangosteen"}
# print('-' * 75)

# print(favouritefruits.issubset(localfruits))    # True
# print('-' * 75)

# print(localfruits.issuperset(favouritefruits))
# print('-' * 75)

# print(favouritefruits.isdisjoint(overseafruits))
# print('-' * 75)

# to break into words

content = """A spam word, in most cases, is a keyword or phrase used to create urgency or simply 
grab attention by being sensational, very promotional, or in connection to a sensitive topic. 
That being said, some very common marketing language can also be seen as spammy when used in 
the wrong context, but more on that a bit later. Who keeps an eye out for spam words? Well, 
besides spam filters set up by email service providers that are trying to spot gimmicks, 
overpromises, multi-level marketing, and shady activities, email recipients themselves can be 
triggered by these words and decide to mark emails containing them as spam folder-worthy."""

words = content.split()
print(len(words))

cleanwords =[]
for word in words:
    word = word.replace("," , " ")
    word = word.replace("." , " ")
    word = word.lower()
    cleanwords.append(word)
uniquewords = set(cleanwords)
print(len(uniquewords))

commonwords = {"do", "is", "all", "did", "not", "you", "i", "be", "to", "at", "a", "and" , "he", \
    "she", "we", "they", "what", "when", "why", "how", "or"}
uniquewords = uniquewords.difference(commonwords)
uniquewords = set(cleanwords)
print(len(uniquewords))
spamwords = {"sensational", "spam", "promotional", "sensitive"}
spamwordsYesNo = uniquewords.intersection(spamwords)
print(len(spamwordsYesNo))

print(cleanwords)
print('-' * 75)

# listfruits = list(fruits)
# listfruits.clear()
# print(listfruits) # empty lists

# print(fruits)
# fruits.clear()
# print(fruits)



