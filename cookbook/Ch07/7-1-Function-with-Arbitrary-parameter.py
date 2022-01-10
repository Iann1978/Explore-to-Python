

def func1(*params):
    print(params)
    print(type(params))

func1('a')

func1('b', 3, True)

def func2(**params):
    print(params)
    print(type(params))

func2(arg0=0)

func2(arg0=0, arg1=1)


def func3(*params0, **params1):
    print(params0)
    print(params1)

func3(0,1)
func3(0,1,arg2=2,arg3=3)

def func4(x, *args):
    print(x)
    print(args)
    # print(y)

func4(1,2,3,4)

