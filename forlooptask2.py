import random
six_count=0
one_count=0
double_six=0
previous_roll=0
for i in range(20):
    roll=random.randint(1,6)
    print("roll",roll);
    if roll==6:
        six_count += 1
    if roll==1:
        one_count+= 1
    if roll==6 and previous_roll==6:
        double_six +=1
    previous_roll=roll    
        
print("total_sixes",six_count)
print("total_ones",one_count)       
print("total six in a row:",double_six)