import requests as req

def api_call(city):
    weather_api = 'ec488331a2784c0290c20038230509'

    # Make API Call to WeatherAPI
    weatherapi_call = f'https://api.weatherapi.com/v1/current.json?key={weather_api}&q={city}&aqi=yes'

    # Make the API request
    weatherapi_response = req.get(weatherapi_call)

    # Check if the request was successful (status code 200)
    if weatherapi_response.status_code != 200:
        print(f'Error: WeatherAPI returned status code {weatherapi_response.status_code}')
        return -1
    else:
        data = weatherapi_response.json()
        return data

def parse_data(data):
    # Extract necessary data from dictionary
    city_name = data['location']['name']
    region_name = data['location']['region']
    country_name = data['location']['country']
    temp_c = data['current']['temp_c']
    wind_kph = data['current']['wind_kph']
    humidity = data['current']['humidity']
    feelslike_c = data['current']['feelslike_c']
    cloud_vol = data['current']['cloud']

    var_list = [city_name, region_name, country_name, temp_c, wind_kph, humidity, feelslike_c, cloud_vol]

    return var_list

def decision(var_list):
    # Makes the decision between clothes
    temp_c, wind_kph, humidity, feelslike_c, cloud_vol = var_list[3:8]

    wind_mps = wind_kph / 3.6
    est_temp = feelslike_c - temp_c
    print("\nRecommendation for today:")
    if temp_c <= 30 or humidity <= 29 or cloud_vol >= 66 and wind_mps >= 3.1:
      if est_temp <= 3:
        print("You can wear warm clothes; tight clothes; full-blown outfits\n")
      elif est_temp >= 4:
        print("You can wear cool clothes; breathable; light\n")
    elif temp_c >= 31 or humidity >= 30 or cloud_vol <= 65 and wind_mps <= 3.0:
      if est_temp <= 3:
        print("Preferably, you should wear cool, loose clothes; breathable; light\n")
      elif est_temp >= 4:
        print("You should wear warm clothes; loose clothes; discouraged on full-blown outfits\n")

def system_start():
    while True:
        answer = input("Do you know what to wear today? [Y/N] ")
        if answer == "N" or answer.lower() == 'n':
            city = input("\nWhich city are you in right now? ")
            data = api_call(city)

            if data == -1:
                print("Failed to retrieve weather data.")
                break

            parsed_data = parse_data(data)
            print(f'City:{parsed_data[0]}')
            print(f'Region:{parsed_data[1]}')
            print(f'Country:{parsed_data[2]}')
            decision(parsed_data)
        elif answer == 'Y' or answer.lower() == 'y':
            print("\nThat's great to hear! Go out there and be your best self!\n")
            break


if __name__ == '__main__':
  system_start()