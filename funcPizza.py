def orders(*items,name,destination):
    print(f"Order for {name} going to {destination}:")
    for i in items:
        print(f"--{i}") 
orders("pizza","burger",name="neha",destination="Cvcorp")