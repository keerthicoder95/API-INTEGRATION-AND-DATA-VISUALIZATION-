import requests
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Replace this with your real API key
API_KEY = 'YOUR API KEY'

# List of cities
cities = ["Chennai", "Delhi", "Mumbai", "Bengaluru"]

# Store data here
weather_records = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "main" in data:
        weather_records.append({
            "City": city,
            "Parameter": "Temperature (°C)",
            "Value": data["main"]["temp"]
        })
        weather_records.append({
            "City": city,
            "Parameter": "Humidity (%)",
            "Value": data["main"]["humidity"]
        })
        weather_records.append({
            "City": city,
            "Parameter": "Pressure (hPa)",
            "Value": data["main"]["pressure"]
        })
    else:
        print(f"⚠️ Could not fetch data for {city}: {data.get('message', 'Unknown error')}")

# Convert to DataFrame
df = pd.DataFrame(weather_records)

# Plotting with Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
palette = sns.color_palette("mako")

# Grouped barplot: City vs Value for each Parameter
sns.barplot(data=df, x="City", y="Value", hue="Parameter", palette=palette)

plt.title("Weather Comparison Between Cities", fontsize=16, weight='bold')
plt.ylabel("Value")
plt.xlabel("City")
plt.legend(title="Parameter")
plt.tight_layout()
plt.show()
