# New function that calculates the distance in the variable of miles, kilometers, and meters.
# This function also convert the units into meters
def total_distance(mile, km, m): # The name of the function is total_distance. mile, km, and m are called parameters.
    convert_miles_to_m = mile * 1609 #This line converts the distance in miles into meters where 1 mile equals to 1609 meter
    convert_km_to_m = km * 1000 #This line convert the distance in kilometers into meters where 1 kilometer equals to 1000 meter
    
    #the next line will calculate the total of the distance in meters
    distance_in_meters = convert_miles_to_m + convert_km_to_m + m

    # Use the keyword "return" to return the value of the calculated distance to the function call
    # In this case, the value is distance_in_meters and the function is total_distance
    return distance_in_meters
# The new function is done

# Now I will call the function to calculate the the distance of 1 miles, 150 kilometers, and 123456 meters as the parameters
# Use print() function to see the result
print(total_distance(1, 150, 123456))