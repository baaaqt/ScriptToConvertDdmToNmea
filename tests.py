from bs4 import BeautifulSoup as bs
from requests import get, Response
import random
from DdmToNmea.script import ddm_convert


def test_values(ddm: list, nmea: list):
    print("site_lat:", ddm[0], ";", "site_lon:", ddm[1])
    print("func_lat:", nmea[0], ";", "func_lon:", nmea[1])


def test() -> None:
    dec_lat = random.uniform(-100, 1000)
    dec_lon = random.uniform(-100, 1000)
    response = get(f"http://www.hiddenvision.co.uk/ez/?dec_lat={dec_lat}&dec_lon={dec_lon}")
    soup = bs(response.text, "html.parser")
    nmea_lat = soup.find(name="input", attrs={"name":"nmea_lat"})
    nmea_lon = soup.find(name="input", attrs={"name":"nmea_lon"})
    test_values([nmea_lat["value"], nmea_lon["value"]], ddm_convert(dec_lat, dec_lon))


def main():
    for i in range(100):
        test()


if __name__ == '__main__':
    main()



