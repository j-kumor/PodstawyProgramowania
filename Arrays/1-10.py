# Prints test statistics
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# Calculates the number of test questions
number_of_questions = len(test_results)

# Calculates the number of correct answers
correct_answers = 0
for answer in test_results:
   if answer:
      correct_answers += 1

# Calculates the number of incorrect answers
incorrect_answers = number_of_questions - correct_answers

percentage_correct = (correct_answers / number_of_questions) * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', number_of_questions)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers: {:.2f}%'.format(percentage_correct))
