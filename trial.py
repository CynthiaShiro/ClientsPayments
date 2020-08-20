
thisdict = {
    "client1" : 1000000,
    "client2" : 500000,
    "client3" : 2000,
    "client4" : 1000
}
newvalue = thisdict.values()
def getTotal(VAT):
    return lambda a, b : (a*VAT) + b
Total = getTotal(0.16)
newtotal = 0
for x in thisdict:
    newtotal += Total(thisdict.get(x), thisdict.get(x))
    
print("The final total is: KES {0:,.2f}".format(newtotal))
