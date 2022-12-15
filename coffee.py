print('hello world')
def coffee_bot():
    print('Welcome to the cafe!')
    size = get_size()
    drink_type = get_drink_type()
    print('Alright, that\'s a ' + size + ' ' + drink_type + '!')
    name = input('Can I get your name please?\n')
    print('Thanks, ' + name + '! Your drink will be ready shortly.')

def print_message():
    print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def get_size():
    res = input('What size drink can I get for you?\n [a] Small\n [b] Medium\n [c] Large\n').lower()
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()

def get_drink_type():
    res = input('What type of drink would you like?\n [a] Brewed Coffee\n [b] Mocha\n [c] Latte\n').lower()
    if res == 'a':
        return 'Brewed Coffee'
    elif res == 'b':
        return 'Mocha'
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()

def order_latte():
    res = input('And what kind of milk would you like with your coffee?\n [a] 4% milk\n [b] Goat milk\n [c] Rice milk\n')
    if res == 'a':
        return 'Latte with 4% milk'
    elif res == 'b':
        return 'Latte with Goat milk'
    elif res == 'c':
        return 'Latte with Rice milk'
    else:
        print_message()
        return order_latte()









coffee_bot()