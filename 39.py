import tkinter as tk
import requests
from tkinter import messagebox


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.api_key = "YOUR_API_KEY"  # جایگزین با کلید API خودتان از OpenWeatherMap

        # City label and entry
        self.label_city = tk.Label(root, text="City:")
        self.label_city.pack()

        self.entry_city = tk.Entry(root)
        self.entry_city.pack()

        # Get Weather button
        self.button_get_weather = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.button_get_weather.pack()

        # Weather information display
        self.label_weather_info = tk.Label(root, text="", font=("Helvetica", 12))
        self.label_weather_info.pack()

    def get_weather(self):
        city = self.entry_city.get()
        if city:
            try:
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
                response = requests.get(url)
                data = response.json()

                if data["cod"] == 200:
                    temp = data["main"]["temp"]
                    weather = data["weather"][0]["description"]
                    self.label_weather_info.config(text=f"Temperature: {temp}°C\nWeather: {weather}")
                else:
                    messagebox.showerror("Error", data["message"])
            except Exception as e:
                messagebox.showerror("Error", "Unable to get weather information")
        else:
            messagebox.showwarning("Warning", "Please enter a city name")


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()