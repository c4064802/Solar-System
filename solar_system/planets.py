import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class Planet:
    """Represents a planet with name, mass, distance from Sun, and moons."""
    def __init__(self, name, mass, distance, moons):
        self.name = name
        self.mass = mass  # in 10^24 kg
        self.distance = distance  # in million km
        self.moons = moons if moons else []

    def __str__(self):
        return (f"Planet: {self.name}\n"
                f"Mass: {self.mass} × 10^24 kg\n"
                f"Distance from Sun: {self.distance} million km\n"
                f"Moons: {', '.join(self.moons) if self.moons else 'None'}")


def load_planets(filename="planets.txt"):
    """Loads planets from a file and returns a dictionary."""
    planets = {}
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split(",")
            name = data[0]
            mass = float(data[1])
            distance = float(data[2])
            moons = data[3:] if len(data) > 3 else []
            planets[name.lower()] = Planet(name, mass, distance, moons)
    return planets


class PlanetApp:
    """GUI Application for querying planet details."""
    def __init__(self, root):
        self.root = root
        self.root.title("Solar System Explorer")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.planets = load_planets()
        self.dark_mode = False

        # Label
        self.label = tk.Label(root, text="Enter a planet name:", font=("Arial", 12))
        self.label.pack(pady=5)

        # Search Box
        self.planet_name_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.planet_name_var, font=("Arial", 12), width=20)
        self.entry.pack(pady=5)

        # Buttons
        self.btn_details = tk.Button(root, text="Show Details", command=self.show_details)
        self.btn_details.pack(pady=5)

        self.btn_mass = tk.Button(root, text="Show Mass", command=self.show_mass)
        self.btn_mass.pack(pady=5)

        self.btn_moons = tk.Button(root, text="Show Number of Moons", command=self.show_moons)
        self.btn_moons.pack(pady=5)

        self.btn_check = tk.Button(root, text="Check If Planet Exists", command=self.check_existence)
        self.btn_check.pack(pady=5)

        # Dark Mode Button
        self.btn_dark_mode = tk.Button(root, text="Toggle Dark Mode", command=self.toggle_dark_mode)
        self.btn_dark_mode.pack(pady=10)

        # Output Label
        self.output_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400, justify="center")
        self.output_label.pack(pady=10)

        # Image Display
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=5)

    def get_planet_name(self):
        """Returns the planet name in lowercase."""
        return self.planet_name_var.get().strip().lower()

    def show_details(self):
        """Displays full details of the selected planet and shows an image."""
        planet_name = self.get_planet_name()
        if planet_name in self.planets:
            self.output_label.config(text=str(self.planets[planet_name]))
            self.display_image(planet_name)
        else:
            messagebox.showerror("Error", "Please enter a valid planet name.")

    def show_mass(self):
        """Displays the mass of the selected planet."""
        planet_name = self.get_planet_name()
        if planet_name in self.planets:
            mass = self.planets[planet_name].mass
            self.output_label.config(text=f"{self.planets[planet_name].name} has a mass of {mass} × 10^24 kg.")
        else:
            messagebox.showerror("Error", "Please enter a valid planet name.")

    def show_moons(self):
        """Displays the number of moons for the selected planet."""
        planet_name = self.get_planet_name()
        if planet_name in self.planets:
            moons_count = len(self.planets[planet_name].moons)
            self.output_label.config(text=f"{self.planets[planet_name].name} has {moons_count} moon(s).")
        else:
            messagebox.showerror("Error", "Please enter a valid planet name.")

    def check_existence(self):
        """Checks if a planet exists in the database."""
        planet_name = self.get_planet_name()
        if planet_name in self.planets:
            self.output_label.config(text=f"Yes, {self.planets[planet_name].name} is in the solar system!")
        else:
            self.output_label.config(text="No, this planet is not in the list.")

    def display_image(self, planet_name):
        """Displays the image of the selected planet."""
        image_path = f"images/{planet_name}.jpg"
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((200, 200), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img
        else:
            self.image_label.config(image="", text="No image available", font=("Arial", 12))

    def toggle_dark_mode(self):
        """Switches between light and dark mode."""
        self.dark_mode = not self.dark_mode
        bg_color = "black" if self.dark_mode else "white"
        fg_color = "white" if self.dark_mode else "black"

        self.root.config(bg=bg_color)
        self.label.config(bg=bg_color, fg=fg_color)
        self.output_label.config(bg=bg_color, fg=fg_color)
        self.image_label.config(bg=bg_color)

        buttons = [self.btn_details, self.btn_mass, self.btn_moons, self.btn_check, self.btn_dark_mode]
        for btn in buttons:
            btn.config(bg="gray" if self.dark_mode else "lightgray", fg=fg_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = PlanetApp(root)
    root.mainloop()
