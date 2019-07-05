def hi():
    print('Hi there!')
    print('How are you?')


def hi_sample(name):
    if name == 'gami':
        print('Hi gami')
    elif name == 'kazuki':
        print('Hi kazuki')
    else:
        print('Hi anonymous')


def hi(name):
    print('Hi ' + name + '!')


def count(num1, num2):
    for i in range(num1, num2):
        print(i)


lab = ['gami', 'inaba', 'nakamura', 'numanoi', 'ozaki']

for name in lab:
    hi(name)
    print('Next!')

count(3, 10)
