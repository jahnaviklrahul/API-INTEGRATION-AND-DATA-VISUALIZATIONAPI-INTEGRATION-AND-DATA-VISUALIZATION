import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(temp, feels_like, humidity, city):
    """Visualize the weather data using bar charts."""
    categories = ['Temperature (°C)', 'Feels Like (°C)', 'Humidity (%)']
    values = [temp, feels_like, humidity]

    # Set Seaborn style
    sns.set(style="whitegrid")

    # Create a bar chart
    plt.figure(figsize=(8, 5))
    sns.barplot(x=categories, y=values, palette="coolwarm")
    plt.title(f"Current Weather Data for {city}", fontsize=16)
    plt.xlabel("Parameters", fontsize=12)
    plt.ylabel("Values", fontsize=12)
    plt.tight_layout()
    plt.show()