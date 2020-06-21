a = {'20','40' ,'60'}
b = {'30','40','50'}
c = {'20','50','70'}

set.union(a,b)

set.intersection(a,b)

set.difference(c,b)

set.symmetric_difference(a,c)

set.intersection(set.difference(set.union(set.difference(c,b),a),c),b)

from fractions import Fraction

n = int(input('lim 1/n    n = ?: '))

lim = Fraction(1, n)
print('%.12f' % lim)