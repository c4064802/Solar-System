import unittest
from planets import Planet, load_planets

class TestPlanet(unittest.TestCase):

    def setUp(self):
        """Set up sample planet data for testing."""
        self.earth = Planet("Earth", 5.97, 149.6, ["Moon"])
        self.jupiter = Planet("Jupiter", 1898, 778.5, ["Io", "Europa"])

    def test_planet_creation(self):
        """Test if planets are created correctly."""
        self.assertEqual(self.earth.name, "Earth")
        self.assertEqual(self.jupiter.mass, 1898)
        self.assertEqual(self.jupiter.moons, ["Io", "Europa"])

    def test_load_planets(self):
        """Test if planets are loaded correctly from the file."""
        planets = load_planets()
        self.assertIn("earth", planets)
        self.assertEqual(planets["earth"].name, "Earth")
        self.assertEqual(planets["mars"].moons, ["Phobos", "Deimos"])

if __name__ == "__main__":
    unittest.main()
