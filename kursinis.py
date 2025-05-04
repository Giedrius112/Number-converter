from abc import ABC, abstractmethod

# Abstract base class
class Converter(ABC):
    @abstractmethod
    def convert(self, value):
        pass

# Concrete class for Arabic to Roman
class ArabicToRomanConverter(Converter):
    def __init__(self):
        self._map = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]

    def convert(self, number):
        if not (1 <= number <= 3999):
            return "Skaičius turi būti tarp 1 ir 3999."
        result = ""
        for roman, value in self._map:
            while number >= value:
                result += roman
                number -= value
        return result

# Concrete class for Roman to Arabic
class RomanToArabicConverter(Converter):
    def __init__(self):
        self._map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def convert(self, roman):
        roman = roman.upper()
        i = 0
        result = 0
        while i < len(roman):
            if i+1 < len(roman) and roman[i:i+2] in ["CM", "CD", "XC", "XL", "IX", "IV"]:
                result += ArabicToRomanConverter()._map[[pair[0] for pair in ArabicToRomanConverter()._map].index(roman[i:i+2])][1]
                i += 2
            elif roman[i] in self._map:
                result += self._map[roman[i]]
                i += 1
            else:
                return "Neteisingas įvestas simbolis"
        if ArabicToRomanConverter().convert(result) != roman:
            return "Neteisinga romėniško skaičiaus forma"
        return result

# Factory Method (Design Pattern)
class ConverterFactory:
    def get_converter(self, mode):
        if mode == "1":
            return ArabicToRomanConverter()
        elif mode == "2":
            return RomanToArabicConverter()
        else:
            raise ValueError("Neteisingas režimas")

# Composition: composition with file handler
class FileManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def write_result(self, content):
        with open(self.filepath, "a", encoding="utf-8") as file:
            file.write(content + "\n")

    def read_all(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return "Failas tuščias arba neegzistuoja."


# Aggregation: converter naudoja factory, bet nėra jo dalis
class ConverterApp:
    def __init__(self, factory, file_manager):
        self.factory = factory
        self.file_manager = file_manager

    def run(self):
        while True:
            print("\n1 - Arabų → Romėniški\n2 - Romėniški → Arabų\n3 - Rodyti istoriją\n0 - Išeiti")
            mode = input("Pasirinkite: ").strip()
            if mode == "0":
                print("Programa baigta.")
                break
            elif mode == "3":
                print("Įrašyta istorija:\n", self.file_manager.read_all())
            elif mode in ["1", "2"]:
                value = input("Įveskite skaičių: ").strip()
                converter = self.factory.get_converter(mode)
                try:
                    if mode == "1":
                        result = converter.convert(int(value))
                    else:
                        result = converter.convert(value)
                    print("Rezultatas:", result)
                    self.file_manager.write_result(f"{value} => {result}")
                except Exception as e:
                    print("Klaida:", e)
            else:
                print("Netinkamas pasirinkimas.")


# Main programa
if __name__ == "__main__":
    factory = ConverterFactory()
    file_manager = FileManager("istorija.txt")
    app = ConverterApp(factory, file_manager)
    app.run()
