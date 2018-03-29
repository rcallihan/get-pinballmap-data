import urllib.request, json

#Directory to put files - user must define
output_directory = "C://Users//**username**//documents//pinball//"

def get_all_regions():
    #URL to get list of regions available at from pinballmap.com
    region_URL = 'https://pinballmap.com/api/v1/regions.json'
    
    #Retrieve region json and load
    response = urllib.request.urlopen(region_URL)
    regions_json = json.load(response)
    
    response.close()
    

    #For each region object and construct new URL to grab pinball machine locations for each region.
    for x in regions_json["regions"]:
    
        #Pull region name out of region json object
        location_name = x["name"]
    
        #Construct url for individual pinball region data and local storage path
        location_url = "https://pinballmap.com/api/v1/region/" + location_name + "/location_machine_xrefs.json"
        pin_location_file = output_directory + location_name + ".json"
    
        #Retreive json from url
        response = urllib.request.urlopen(location_url)
        locations_json = json.load(response)
    
        #Write json to directory
        with open(pin_location_file, 'w') as outfile:
            json.dump(locations_json, outfile)
    
        print(location_name + " downloaded.")
    
    
get_all_regions()


