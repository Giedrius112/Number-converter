import unittest
from kursinis import ArabicToRomanConverter, RomanToArabicConverter, ConverterFactory, FileManager
import os



class TestArabicToRomanConverter(unittest.TestCase):
    def test_convert(self):
        converter = ArabicToRomanConverter()
        
        self.assertEqual(converter.convert(1), 'I')
        self.assertEqual(converter.convert(4), 'IV')
        self.assertEqual(converter.convert(5), 'V')
        self.assertEqual(converter.convert(9), 'IX')
        self.assertEqual(converter.convert(10), 'X')
        self.assertEqual(converter.convert(3999), 'MMMCMXCIX')
        self.assertEqual(converter.convert(4000), 'Skaičius turi būti tarp 1 ir 3999.')



class TestRomanToArabicConverter(unittest.TestCase):
    def test_convert(self):
        converter = RomanToArabicConverter()
        
        self.assertEqual(converter.convert('I'), 1)
        self.assertEqual(converter.convert('IV'), 4)
        self.assertEqual(converter.convert('V'), 5)
        self.assertEqual(converter.convert('IX'), 9)
        self.assertEqual(converter.convert('X'), 10)
        self.assertEqual(converter.convert('MMMCMXCIX'), 3999)
        self.assertEqual(converter.convert('IIII'), 'Neteisinga romėniško skaičiaus forma')
        self.assertEqual(converter.convert('ABCD'), 'Neteisingas įvestas simbolis')



class TestConverterFactory(unittest.TestCase):
    def test_get_converter(self):
        factory = ConverterFactory()
        
        self.assertIsInstance(factory.get_converter("1"), ArabicToRomanConverter)
        self.assertIsInstance(factory.get_converter("2"), RomanToArabicConverter)
        
        with self.assertRaises(ValueError):
            factory.get_converter("3")



class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.file_manager = FileManager("test_istorija.txt")
    
    def tearDown(self):
        if os.path.exists("test_istorija.txt"):
            os.remove("test_istorija.txt")

    def test_write_result(self):
        self.file_manager.write_result("Test 1 => I")
        with open("test_istorija.txt", "r", encoding="utf-8") as file:
            content = file.read()
        self.assertIn("Test 1 => I", content)
    
    def test_read_all(self):
        self.file_manager.write_result("Test 1 => I")
        result = self.file_manager.read_all()
        self.assertIn("Test 1 => I", result)

    def test_read_empty_file(self):
        empty_file_manager = FileManager("empty_test.txt")
        result = empty_file_manager.read_all()
        self.assertEqual(result, "Failas tuščias arba neegzistuoja.")


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
