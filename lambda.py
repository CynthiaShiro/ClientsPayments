
def myfunc(n):
    return lambda a, b : (a*n) + b

thisdict = {
    "client1" : 1000000,
    "client2" : 500000,
    "client3" : 2000,
    "client4" : 1000
}

mydoubler = myfunc(0.16)

newvalue = 0
for x in thisdict:
   # print(x)
    newvalue += mydoubler(thisdict.get(x), thisdict.get(x))

print("The Total Inclusive amount is KES {0:,.2f}".format(newvalue))
