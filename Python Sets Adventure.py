# Imagine you work for an airline and need to compare the flight routes 
# of your airline with a competitor. You have two sets of flight destinations,
# one for each airline. Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
# Whether there are any destinations that neither airline shares.
# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def both_airlines(our_routes, competitor_routes): # Destinations that both airlines fly to.
    
    same = our_routes.intersection(competitor_routes)
    
    return same

print(both_airlines(our_routes, competitor_routes))


def differences(my_airline, competitor_routes): # Destinations unique to your airline.
    
    diff = my_airline.difference(competitor_routes)
    
    return diff

print(differences(our_routes, competitor_routes)) # Whether there are any destinations that neither airline shares.

def neither(our_routes, competitor_routes):
     a = differences(our_routes, competitor_routes)
     b = differences(competitor_routes, our_routes)
     
     dont_share = a.union(b)
     
     return dont_share
 
print(neither(our_routes, competitor_routes))
    