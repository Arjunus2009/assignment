

def simple_interest(p,t,r):
    return (p*t*r)/100

print(simple_interest(100000, 1, 10))


# default parameters always in last
def simple_interest(p,t=10,r=6):
    si = (p*t*r)/100
    return si
p = 10000

print(simple_interest(p, )) 
print(simple_interest(t =5, p = 5000))   


#