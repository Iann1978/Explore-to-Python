
values = ['1', '2', -3, '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
fil = filter(is_int, values)
print(fil)
print(type(fil))
ivals = list(filter(is_int, values))
print(ivals)