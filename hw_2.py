a = {'20','40' ,'60'}
b = {'30','40','50'}
c = {'20','50','70'}

set.union(a,b)

set.intersection(a,b)

set.difference(c,b)

set.symmetric_difference(a,c)

set.intersection(set.difference(set.union(set.difference(c,b),a),c),b)

das