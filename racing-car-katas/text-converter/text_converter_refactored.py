from abc import ABC, abstractmethod
from typing import List
# This is for Python 3
import html as html_converter

# for Python 2 uncomment this line
#import cgi as html_converter


class UnicodeFileToHtmlTextConverter(object):

    def __init__(self, full_filename_with_path):
        self.full_filename_with_path = full_filename_with_path
        self._reader = HtmlReader(self.full_filename_with_path)

    def convert_to_html(self):
        lines = self._reader.read_file()
        html = ""
        for line in lines:
            html += self.escape_html(line.rstrip()) + "<br />"
        return html

    @staticmethod
    def escape_html(line: str, quote: bool = True):
        return html_converter.escape(line, quote=quote)


class Reader(ABC):

    def __init__(self, full_filename_with_path):
        self.full_filename_with_path = full_filename_with_path

    @abstractmethod
    def read_file(self):
        pass


class HtmlReader(Reader):

    def read_file(self) -> List:
        try:
            with open(self.full_filename_with_path, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            return []
