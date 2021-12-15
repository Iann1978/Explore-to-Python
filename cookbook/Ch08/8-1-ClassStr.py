
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        print('__repr__')
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    # def __str__(self):
    #     print ('__str__')
    #     return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
p

print('p is {0!r}'.format(p))
#
print('p is {0}'.format(p))

print('p is {0!s}'.format(p))

pp = eval(repr(p))


print(pp)
print(pp.__class__)