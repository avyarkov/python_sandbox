def func1(arg, kwarg=0, *args, **kwargs):
    print(
        'arg: ' + str(arg) + ', ' +
        'kwarg: ' + str(kwarg) + ', ' +
        '*args: ' + str(args) + ', ' +
        '**kwargs: ' + str(kwargs))


def func2(arg, *args, kwarg=0, **kwargs):
    print(
        'arg: ' + str(arg) + ', ' +
        '*args: ' + str(args) + ', ' +
        'kwarg: ' + str(kwarg) + ', ' +
        '**kwargs: ' + str(kwargs))


func1(1, 2)
func1(1, 2, 3)
# func1(1, 2, kwarg=3)
# TypeError: func1() got multiple values for argument 'kwarg'

func2(1, 2)
func2(1, 2, 3)
func2(1, 2, 3, kwarg=4)
func2(1, 2, 3, a=101, b=102)
func2(1, 2, 3, a=101, b=102, kwarg=4)
