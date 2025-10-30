def layer(num):
    layer_1 = '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    '''

    layer_2 = '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    '''

    layer_3 = '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    '''

    layer_4 = '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    '''

    layer_5 = '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    '''

    layer_6 = '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    '''

    layer_7 = '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    '''

    layers = [layer_1, layer_2, layer_3, layer_4, layer_5, layer_6, layer_7]
    return layers[num] # Default to first layer if number is out of range
