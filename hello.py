country = ['France', 'UK', 'Spain', 'Sweden', 'Iceland', 'Belgium', 'Italy', 'Germany', 'Netherlands', 'Poland', 'Russia']
capital = ['paris', 'london', 'madrid', 'stockholm', 'reykjavik', 'brussels', 'rome', 'berlin', 'amsterdam', 'warsaw', 'moscow']
question_no = 0


while question_no < 9:
    quiz = input(f'What is the capital of {country[question_no]}? ').lower()
    if quiz == capital[question_no]:
        print('You are correct!')
        quiz = input(f'What is the capital of {country[question_no]}? ').lower()
    question_no += 1
