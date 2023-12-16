# Create a set named unique_words containing unique words and
# another set named duplicate_words containing words that appear 
# more than once.
words = ["apple", "banana", "orange", "grape", "kiwi", "banana", "apple"]
uniq_word=set()
duplicate_word=set()


for word in words:
    if word in uniq_word:
        duplicate_word.add(word)
    else:
        uniq_word.add(word)
print("These are unique:",uniq_word)
print("These are duplicate:",duplicate_word)


    


    

# Write a program to create two sets:

# A set containing even numbers from the given set.
# A set containing squares of odd numbers from the given set.

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

evenset=set()
oddset=set()


for i in numbers:
    if i%2==0:
        evenset.add(i)
    else:
        oddset.add(i)
print("The even set is:",evenset)
print("The odd set is:",oddset)