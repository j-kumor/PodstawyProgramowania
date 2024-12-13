###
# Calculates the final grade for a tset based
#

def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif 14 <= points < 18:
        grade = 'Good'
    elif 10 <= points < 14:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    return grade


test_result = 15
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result}, points on the test. Your final grade is {final_grade}')
