import xml.etree.ElementTree as ET


class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
        return 9.0 / 5.0 * temperature_in_celsius + 32


class ForecastXmlParser:
    def __init__(self, temperature_converter):
        self.temperature_converter = temperature_converter

    def parse(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            day = child.find('day').text
            temperature_in_celsius = int(child.find("temperature_in_celsius").text)
            temperature_in_fahrenheit = round(self.temperature_converter
                                              .convert_celsius_to_fahrenheit(temperature_in_celsius), 1)
            print(f"{child.find("day").text}: {temperature_in_celsius} Celsius, {temperature_in_fahrenheit} Fahrenheit")

temperature_converter = TemperatureConverter()
forecast_xml_parser = ForecastXmlParser(temperature_converter)
forecast_xml_parser.parse("forecast.xml")
