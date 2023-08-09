def foo(n):
    var1, var2 = 0, 1
    while var1 < n:
        print(var1, end=' ')
        var1, var2 = var2, var1 + var2
    print()


def bar(n):
    result = []
    var1, var2 = 0, 1
    while var1 < n:
        result.append(var1)
        var1, var2 = var2, var1 + var2
    return result
