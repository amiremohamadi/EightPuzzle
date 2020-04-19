def shapeshift(strings):
    '''convert a result in format: list of strings
       to a list of dicts to be used in front-end
       params:
         -- strings: list of strings. eg: ['12345678X', '1324567X8', ...]
    '''
    res = []

    for string in strings:
        # we don't care about validation now, but each string must be a 
        # permutation of 9 characters (1 - 8) containing a 'X' for empty cell
        cells = []
        # represent each cell with: val (int), attrib (css class name)
        for char in string:
            cell = {'val': char}
            cell['attrib'] = 'correct' if char != 'X' else 'empty'
            cells.append(cell)
        res.append(cells)

    return res
    