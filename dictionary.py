# Dictionaries: Associations = { Key: Value }

myDictionary = {
  'Spain': 'Madrid',
  'France': 'Paris',
  'Germany': 'Berlin',
}

print('Print dictionary:', myDictionary)

print('Print only France:', myDictionary['France'])

myDictionary['UK'] = 'Manchester' # Adding entry to dictionary

myDictionary['UK'] = 'London' # Correcting dictionary entry

print('Print dictionary:', myDictionary)

del myDictionary['UK'] # Removing an item from the dictionary

print('Print dictionary:', myDictionary)

print('Dictionary keys:', myDictionary.keys())

print('Dictionary values:', myDictionary.values())

print('Dictionary length:', len(myDictionary))
