# native libraries
import re

# third party libraries
from bs4 import BeautifulSoup
import requests


class Scrapper:
    def __init__(self, host):
        self.host = host
        self._html = self._visit()

    def _visit(self):
        response = requests.get(self.host)

        return response.text

    def _select(self, query_string):
        soup = BeautifulSoup(self._html, 'html.parser')

        return soup.select(query_string)


class ImagesWeb(Scrapper):
    def __init__(self, host):
        super().__init__(host)

    @property
    def images_links(self):
        is_image_link_well_formed = re.compile(r"^https?://.+\.(png|jpg|jpeg|svg|JPEG|JPG|PNG)$")
        image_nodes = self._select('img')

        image_links = [image_link['src'] for image_link in image_nodes if
                       image_link and is_image_link_well_formed.match(image_link['src']) and image_link.has_attr('src')]

        return list(set(image_links))
