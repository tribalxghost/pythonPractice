def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    length = len(phrase)
    reverse = ""
    for num in range(length, 0, -1):
        reverse += phrase[num -1]  
    return reverse    
