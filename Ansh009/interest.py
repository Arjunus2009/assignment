# calcuate interest 

    #ram, 100000, 5 yrs  12%
    #SHAYAM 200000, 3 YRS  11.5%
    #HARI 300000, 4 YRS  9.9%
# FIND OUT OF SUM AMOUNT OF PEOPLE WHEN their FD matured.

# you have to find out the compound interest compounded yearsly


people = {
    
    "ram": {"p":100000, "t": 5, "r":0.12},
    "shyam": {"p":200000, "t": 3, "r":0.115},
    "hari": {"p":300000, "t": 4, "r":0.909}
}
amount = {}
for name,value in people.items():
    a = value["p"]*(1+value["r"]**value["t"])
    amount[name]=a
    print(amount)
    


    
    
    
