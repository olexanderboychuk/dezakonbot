from bs4 import BeautifulSoup

from zakon.api import ZakonApi
from zakon.models import AcceptedZakonModel, RegisteredZakonModel
from zakon.zakon_objects import AcceptedZakon, RegisteredZakon


class ZakonParser:

    @classmethod
    def _get_soup_object(cls, html):
        return BeautifulSoup(html, features="html.parser")

    @classmethod
    def parse_registered_laws(cls):

        html = ZakonApi.get_registered()

        soup = cls._get_soup_object(html)

        trs = soup.find_all("tr")

        for tr in trs[1:]:
            tds = tr.find_all("td")

            zakon_id = tds[0].text.strip()
            zakon_date = tds[1].text.strip()
            zakon_name = tds[2].text.strip()
            zakon_authors = tds[3].text.strip()

            zakon = RegisteredZakon(
                zakon_id, zakon_date, zakon_name, zakon_authors)
            
            RegisteredZakonModel.create_from_dict(zakon.to_dict())

    @classmethod
    def parse_accepted_laws(cls):

        html = ZakonApi.get_accepted()

        soup = cls._get_soup_object(html)

        trs = soup.find_all("tr")

        for tr in trs[1:]:
            tds = tr.find_all("td")

            zakon_number_act = tds[0].text.strip()
            zakon_date_act = tds[1].text.strip()
            zakon_name = tds[2].text.strip()
            zakon_id = tds[3].text.strip()
            zakon_date = tds[4].text.strip()

            zakon = AcceptedZakon(zakon_id, zakon_date,
                                  zakon_name, zakon_number_act, zakon_date_act)
            
            AcceptedZakonModel.create_from_dict(zakon.to_dict())
