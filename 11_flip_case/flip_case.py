def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newPhrase = ""
    for word in phrase:
        if(word == to_swap.lower() or word == to_swap.upper()):
            newPhrase += word.swapcase()
        else: 
            newPhrase += word
    return newPhrase

        
    
    