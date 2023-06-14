import unittest
from text_converter_refactored import UnicodeFileToHtmlTextConverter


class UnicodeFileToHtmlTextConverterTest(unittest.TestCase):
    
    def test_foo(self):
        converter_1 = UnicodeFileToHtmlTextConverter("foo")
        self.assertEqual("foo", converter_1.full_filename_with_path)
        self.assertEqual('', converter_1.convert_to_html())

        converter_2 = UnicodeFileToHtmlTextConverter("test/test_1.txt")
        self.assertEqual('5 &lt; 10<br />9 &gt; 2<br />',
                         converter_2.convert_to_html())

        self.assertEqual('5 &lt; 10', converter_2.escape_html('5 < 10'))
        self.assertEqual('9 &gt; 2', converter_2.escape_html('9 > 2'))


if __name__ == "__main__":
    unittest.main()
