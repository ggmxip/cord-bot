from random import choice, randint

 # basic logic, should add own logic or AI damnnnn
 
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == ' ':
        return ' Why so silent!?...'
    elif 'hello' in lowered:
        return'Hola Amigo! Kaise ho, theek ho?'
    elif 'how are you' in lowered:
        return'Bhai bohat hi set'
    elif 'acha' in lowered:
        return'Tell them I\'m just not impressed'
    elif 'dice satta' in lowered:
        return f'You rolled: {randint(1,6)}'
    elif 'bye' in lowered:
        return'Aunty ko bolna "I\'m sending my love"'
    elif 'help' in lowered:
        return'foolowing key words only-- hello, how are you, acha, dice satta, bye'
    else:
        return choice (['I do not understand lol',
                         'try typing something human lol',
                         'pogo dekho ja kar bro XD'])
    
    