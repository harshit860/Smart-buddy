import webbrowser
print('---------------------------')
print('---------------------------')
print('Welcome to buddy your friend')


first = input('What is your name')
last = input(first+' '+'last name please')
gender = input('press m for male and f for female')

if gender == 'm':
    age = input('what is your age Mr '+first)
else:
    age = input('what is your age Ms '+first)

if first[0] == 'h' or first[1] =='a' or first == 'harshit':
    print('Hello admin')

if int(age) > 25:
    remark = 'Young'

choice = input(remark+' '+'choice from these options :-')


if choice == 'y':
    webbrowser.open('https://www.youtube.com')

