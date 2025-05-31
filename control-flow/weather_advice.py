user_weather = input("What's the weather like today? (sunny/rainy/cold):")

if user_weather == "sunny":
    message = "Wear a t-shirt and sunglasses."
elif user_weather == "rainy":
    message = " Don't forget your umbrella and a raincoat."
elif user_weather == "cold":
    message = "Make sure to wear a warm coat and a scarf."
else:
    message = "Sorry, I don't have recommendations for this weather."

print(message)
