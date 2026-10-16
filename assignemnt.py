def classify(value): 
    if value < 748:
        return "Below range"
    elif value <= 752:
        return "In range"
    else: 
        return "Above range"
    

def calculate_average(total,count):
        return total/count

total = 0
below_range = 0
in_range = 0
above_range = 0

num_tins = int(input("Enter the number of paint tins: ")) 

for i in range(num_tins):
    volume = int(input("Enter the paint tin volume: "))  
    cg = classify(volume)  
    total  = total + volume 
    print(cg)

    if cg == 'Below range':
        below_range = below_range + 1
    elif cg == "In range":
        in_range = in_range + 1
    else: 
        above_range = above_range +1

    
print(f"Total volume: {total} ml", )
print("Average volume: ", calculate_average(total, num_tins), " ml")

print("Below range: ", below_range)
print("In range: ", in_range)
print("Above range: ", above_range)


    
