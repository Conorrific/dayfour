

#use a key to access dictionaries. the key here is "IAH"
airports = {"IAH":"Houston Airport","LAX":"Los Angeles Airport"}
airports = {"IAH":{"Location":"Houston","AreaCode":6675}}


for (k,v) in airports.items():
    print(k, v)
houston_airport = airports["IAH"]

print(houston_airport["IAH"])
print(airports["LAX"])