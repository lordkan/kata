# https://www.codewars.com/kata/53368a47e38700bd8300030d

namelist = lambda l: '' if len(l) == 0 else ', '.join([n['name'] for n in l]).replace(', ' + l[-1]['name'], ' & ' + l[-1]['name'])
