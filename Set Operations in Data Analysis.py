# You are given a list of customer IDs, 
# some of which are duplicated. Write a Python 
# script to remove duplicates and display the unique customer IDs.

# Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
# unique_ids = set(customer_ids)
# print("Unique Customer IDs:", unique_ids)
# Expected Outcome:
# A set of unique customer IDs, ensuring no duplicates. 
# For instance, 
# {'C001', 'C002', 'C003', 'C004'}.

def rmv_duplicates(customer_ids):
    
    unique = set()
    
    for id in customer_ids:
        
        unique.add(id)
        
    return unique

unique_ids = rmv_duplicates(customer_ids)
print("Unique Customer IDs:", unique_ids)