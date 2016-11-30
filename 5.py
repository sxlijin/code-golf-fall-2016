y=lambda x:[x] if type(x) is int else [a for z in x for a in y(z)]
print(y(eval(input())))

