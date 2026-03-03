justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
print(justice_league)
print(len(justice_league))
justice_league.append("batgirl")
justice_league.append("Nightwing")
print(justice_league)
justice_league.remove("WonderWoman")
justice_league.insert(0,"WonderWoman")
print(justice_league)
justice_league.remove("Green Lantern")
justice_league.insert(4, "Green Lantern")
print(justice_league)

justice_league=["Cyborg","Shazam","Hawkgirl","MartianManhunter","Green Arrow"]
print(justice_league)

justice_league.sort()
print(justice_league)
print("New leader:",justice_league[0])