
with open('filename') as file:
    
    # Place each line as an element in the plan list. Use ".rstrip" to remove white space.
    plan = [line.strip() for line in file]


    