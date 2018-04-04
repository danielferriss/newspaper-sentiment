import newspaper

barron        = newspaper.build('https://www.barrons.com/', memoize_articles=False)
economist     = newspaper.build('https://www.economist.com/', memoize_articles=False)
kiplinger     = newspaper.build('https://www.kiplinger.com/', memoize_articles=False)
ibd           = newspaper.build('https://www.investors.com/', memoize_articles=False)
businessweek  = newspaper.build('https://www.bloomberg.com/businessweek', memoize_articles=False)
forbes        = newspaper.build('https://www.forbes.com/#55e2a0d92254', memoize_articles=False)
money         = newspaper.build('https://www.time.com/money/', memoize_articles=False)
cnn           = newspaper.build('https://www.cnn.com', memoize_articles=False)

print('Barron: ' + str(barron.size()))
print('The Economist: ' + str(economist.size()))
print('Kiplinger: ' + str(kiplinger.size()))
print('IBD: ' + str(ibd.size()))
print('Businessweek: ' + str(businessweek.size()))
print('Forbes: ' + str(forbes.size()))
print('Money: ' + str(money.size()))
print('CNN: ' + str(cnn.size()))