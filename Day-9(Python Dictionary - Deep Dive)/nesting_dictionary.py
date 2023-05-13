# travel_log = {
#     "France":{"cities_visited":["Paris","Lille","Lyon","Marseille"],"total_visits":12},
#     "Germany":{"cities_visited":["Berlin","Dortmund","Munich","Frankfurt"],"total_visits":5}
# }

travel_log=[
 {
     "country":"France", 
     "cities_visited":["Paris","Lille","Lyon","Marseille"],
     "total_visits":12
 },
 {
     "country":"Germany",
     "cities_visited":["Berlin","Dortmund","Munich","Frankfurt"],
     "total_visits":5
 }           
 ]
print(travel_log)


def add_new_country(country_visited, times_visited, cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"]=times_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)