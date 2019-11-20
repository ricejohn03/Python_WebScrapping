import webbrowser

print("Type in Address you want Google Maps to Open Up: ")
address = input()
print('Google Maps will now be opening in your browers to the address: \n' + address)
webbrowser.open('https://www.google.com/maps/place/' + address)
print("You have successfully opened Google maps")