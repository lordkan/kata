# https://www.codewars.com/kata/54da5a58ea159efa38000836

from collections import Counter

find_it = lambda seq: [key for key, value in Counter(seq).items() if value % 2 != 0][0]
