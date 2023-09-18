
# Question 1: 
# Implement a function is_balanced(expression) that takes a string 
# containing parentheses, curly braces, and square brackets,and determines whether 
# the expression is balanced. 

# An expression is considered balanced if each opening bracket has a corresponding closing 
# bracket in the correct order.

def is_balanced(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != mapping[char]:
                return False

    return not stack

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False


# Question 2:
# Write a function remove_duplicates(sequence) that takes a 
# sequence (list or tuple) and returns a new sequence with duplicates 
# removed while maintaining the original order of elements. 

def remove_duplicates(sequence):
    unique_elements = []
    for item in sequence:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements


# Test case
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]


# Question 3: 
# Implement a function word_frequency(sentence) that takes 
# a sentence and returns a dictionary containing the frequency of each 
# word in the sentence. 

# Ignore punctuation and consider words in a case-insensitive manner.

import string

def word_frequency(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
