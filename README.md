Number Converter

Tai yra programa, skirta keisti romėniškus skaičius į arabiškus ir atvirkščiai. Romėniški skaičiai naudojami ir šiomis dienomis, tačiau ne kiekvienas šiuos skaičius supranta. Ši programa gali greit išversti juos, ar padaryti atvirkščiai.

Analizė
Polimorfizmas - galimybė skirtingiems objektams reaguoti į tą patį metodą skirtingais būdais. Tai leidžia vieną metodą naudoti kelioms klasėms. Kiekviena klasė įgyvendina metodą savaip.
"class ArabicToRomanConverter(Converter):
    def convert(self, number):"
"class RomanToArabicConverter(Converter):
    def convert(self, roman):"
Tas pats metodas "convert" yra naudojamas su šiomis skirtingomis klasėmis. Klasės skirtingos, metodas įgyvendinamas skirtingai.

Abstrakcija
Tai  reiškia, kad tam tikri objekto metodai ar savybės yra paslėpti, o kiti yra paliekami aiškūs ir prieinami. Klasėse, kuriose naudojama abstrakcija, dažnai apibrėžiami abstraktūs metodai, kuriuos įgyvendins paveldinčios klasės.
from abc import ABC, abstractmethod

"class Converter(ABC):
    @abstractmethod
    def convert(self, value):
        pass"
Kodo pagrindinė abstrakcija yra Converter klasė, kuri turi abstraktų metodą convert(self, value). Tai reiškia, kad nors visi Converter klasės objektai turi turėti metodą convert, tačiau tikrąjį šio metodo įgyvendinimą suteikia paveldinčios klasės, tokios kaip ArabicToRomanConverter ir RomanToArabicConverter.

Paveldėjimas
Tai leidžia kurti naujas klases, kurios paveldi savybes bei metodus iš kitų klasių. Tokiu būdu išvengiama kodo pasikartojimo.
ArabicToRomanConverter ir RomanToArabicConverter paveldi Converter klasę, kad užtikrintų, jog abu metodai turi bendrą sąsają.

Inkapsuliacija
Enkapsuliacija yra principas, kuriuo siekiama paslėpti objekto duomenis ir leisti prieiti prie jų tik per nustatytas sąsajas (metodus). Tai padeda apsaugoti duomenis nuo tiesioginio pakeitimo ir užtikrina, kad duomenys būtų naudojami tik pagal numatytą logiką.
"class ArabicToRomanConverter(Converter):
    def __init__(self):
        self._map = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]"
Inkapsuliacija leidžia paslėpti _map informaciją nuo tiesioginės manipuliacijos. Tokiu būdu išoriniai objektai negali tiesiogiai keisti šių duomenų, duomenys naudojami tik metodų viduje.

Dizaino šablonas:Factory method
Factory Method dizaino šablonas leidžia sukurti objektus, nespecifikuojant tiksliai, kokiai klasei objektas turi priklausyti.
"class ConverterFactory:
    def get_converter(self, mode):
        if mode == "1":
            return ArabicToRomanConverter()
        elif mode == "2":
            return RomanToArabicConverter()
        else:
            raise ValueError("Neteisingas režimas")"
ConverterFactory klasė yra atsakinga už objekto (konverterio) sukūrimą.
Ši klasė turi metodą get_converter(mode), kuris pagal pasirinkimą grąžina arba ArabicToRomanConverter, arba RomanToArabicConverter klasę.

Kompozicija: jei tėvinis objektas yra sunaikintas, jo sudedamieji objektai taip pat sunaikinami. Jie negali egzistuoti vienas be kito, nes yra priklausomi.
"class ConverterApp:
    def __init__(self, factory, file_manager):
        self.factory = factory  
        self.file_manager = file_manager"

Ši programa taip pat saugo istoriją, kurią vėliau galima peržiūrėti. Istorija įrašoma taip:
"class FileManager:
    def write_result(self, content):
        with open(self.filepath, "a", encoding="utf-8") as file:
            file.write(content + "\n")"
Failo turinys perskaitomas taip:
"class FileManager:
    def read_all(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return file.read()  # Grąžina visą failo turinį
        except FileNotFoundError:
            return "Failas tuščias arba neegzistuoja.""

Rezultatai:
Su testų pagalba, kurie užtikrino tikslumą, patikrinau ar kodas neįvelia klaidų (pridėtas failas).

Sukūriau programą, kuri keičia skaičius iš arabiškų į romėniškus ir atvirkščiai, kuri gali būti naudojama mokymosi tikslais.

Buvo iššūkių rašyti kodą, kuris užtikrintų tikslius skaičių pakeitimus.


Išvados:
Šios programos dėka galima mokintis romėniškų ar arabiškų skaičių bei efektyviai ir greitai juos keisti. Programa užtikrina tikslumą, kuris patikrintas testų. Rezultatai saugojami ir vėliau juos galima apžvelgti. Programą galima plėsti ir implementuoti ją įvairiose svetainėse, kurių skaitmenis būtų galima keisti į vienus ar kitus.

