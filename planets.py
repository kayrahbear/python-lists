planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)

planet_list.extend(["Neptune", "Uranus"])
print(planet_list)

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
print(planet_list)

planet_list.append("Pluto")
print(planet_list)

rocky_planets = planet_list[:4]
print(rocky_planets)

del planet_list[8]
print(planet_list)



