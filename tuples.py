tupleParenthesis = ('Luis', 'Ana', 'Manuel')
tupleWithoutParenthesis = 'Luis', 'Ana', 'Manuel'

print(tupleParenthesis, tupleWithoutParenthesis)
print('Print second index:', tupleParenthesis[2])

createdListFromTuple = list(tupleParenthesis)
print('Printing list:', createdListFromTuple)

createdTupleFromList = tuple(createdListFromTuple)
print('Printing tuple:', createdTupleFromList)

print('Is Luis in tuple:', 'Luis' in tupleParenthesis)
print('Times Ana is in tuple:', tupleParenthesis.count('Ana'))

unitaryTuple = ('Francis',)
print('Unitary tuple', unitaryTuple, len(unitaryTuple))

# Unpacking a tuple
myTuple = "Luis", 16, 10, 1999
name, day, month, year = myTuple
print(name, day, month, year)
