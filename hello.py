country = ['France', 'UK', 'Spain', 'Sweden', 'Iceland', 'Belgium', 'Italy', 'Germany', 'Netherlands', 'Poland', 'Russia']
capital = ['paris', 'london', 'madrid', 'stockholm', 'reykjavik', 'brussels', 'rome', 'berlin', 'amsterdam', 'warsaw', 'moscow']
question_no = -1

while True:
    country = question_no
    quiz = input(f'What is the capital of {country[question_no]}? ').lower()
    if quiz == capital[question_no]:
        print('You are correct!')
    question_no += 1

