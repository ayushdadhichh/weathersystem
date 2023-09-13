import requests
import time

# API Key
API_KEY = 'YOUR_API_KEY'

# Favorite Cities (You can use a database or file for persistence)
favorite_cities = []

def get_weather(city_name):
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None

def add_favorite(city_name):
    if city_name not in favorite_cities:
        favorite_cities.append(city_name)
        print(f'Added {city_name} to favorites.')

def remove_favorite(city_name):
    if city_name in favorite_cities:
        favorite_cities.remove(city_name)
        print(f'Removed {city_name} from favorites.')

def list_favorites():
    print('Favorite Cities:')
    for city in favorite_cities:
        print(city)

def main_menu():
    while True:
        print('\nWeather Checking Application')
        print('1. Check Weather by City')
        print('2. Manage Favorite Cities')
        print('3. Auto-Refresh Options')
        print('4. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            city = input('Enter city name: ')
            weather_data = get_weather(city)
            if weather_data:
                # Display weather data here
                print(weather_data)
        elif choice == '2':
            manage_favorite_cities()
        elif choice == '3':
            auto_refresh_options()
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

def manage_favorite_cities():
    while True:
        print('\nManage Favorite Cities')
        print('1. Add Favorite City')
        print('2. Remove Favorite City')
        print('3. List Favorite Cities')
        print('4. Back to Main Menu')

        choice = input('Enter your choice: ')

        if choice == '1':
            city = input('Enter city name to add to favorites: ')
            add_favorite(city)
        elif choice == '2':
            city = input('Enter city name to remove from favorites: ')
            remove_favorite(city)
        elif choice == '3':
            list_favorites()
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please try again.')

def auto_refresh_options():
    while True:
        print('\nAuto-Refresh Options')
        print('1. Enable Auto-Refresh')
        print('2. Disable Auto-Refresh')
        print('3. Back to Main Menu')

        choice = input('Enter your choice: ')

        if choice == '1':
            interval = int(input('Enter refresh interval (seconds): '))
            enable_auto_refresh(interval)
        elif choice == '2':
            disable_auto_refresh()
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')

def enable_auto_refresh(interval):
    print(f'Auto-Refresh enabled with an interval of {interval} seconds.')
    while True:
        # Fetch and display weather data here
        time.sleep(interval)

def disable_auto_refresh():
    print('Auto-Refresh disabled.')

if __name__ == '__main__':
    main_menu()
