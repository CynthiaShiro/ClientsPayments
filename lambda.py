#multiply the exclusive amount by the vat
def myfunc(n):
    return lambda a, b : (a*n) + b
#gets the sum of all clients payments
def getSum(Payment):
    Payment = lambda a, b, c : a + b + c
    return Payment

#front end
thisdict = {
    "client1" : 1000000,
    "client2" : 500000,
    "client3" : 2000
}

mydoubler = myfunc(0.16)
new1 = mydoubler(thisdict.get("client1"), thisdict.get("client1"))
new2 = mydoubler(thisdict.get("client2"), thisdict.get("client2"))
new3 = mydoubler(thisdict.get("client3"), thisdict.get("client3"))
x = 0
mySum = getSum(x)
Total = mySum(new1, new2, new3)
print("The Total Inclusive amount is KES {0:,.2f}".format(Total))
