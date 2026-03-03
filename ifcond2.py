australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
city=input("Enter the city name:");
if city in australia:
    print(city,"is in australia");
elif city  in uae:
    print(city,"is in uae");
elif city  in india:
    print(city,"the city in india");
else:
    print("city not found");
    
city1=input("enter first city:");
city2=input("enter second city:");


if city1 in australia:
    print("country1=australia");
elif city1 in uae:
    print("country1=uae");
elif city1 in india:
    print("county1=india");
else:
    country1=("unknown");
  
if city2 in australia:
    print("country2=australia");
elif city2 in uae:
    print("country2=uae");
elif city2 in india:
    print("county2=india");
else:
    country2=("unknown");
    
    
if country1 == country2 and country1!="unknown":
    print("both cities are in",country1);
else:
    print("they do not belong to the same country");