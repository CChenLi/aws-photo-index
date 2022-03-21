import nltk

plurals = ['caresses', 'flies', 'dies', 'mules', 'geese', 'mice', 'bars', 'foos',
           'families', 'dogs', 'child', 'wolves']

p = nltk.PorterStemmer()
for input in plurals:
    output = p.stem(input)
    print(output)
