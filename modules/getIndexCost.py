def getLCostIndex(cities):
    from bs4 import BeautifulSoup
    import requests as re
    retorno = []
    soup = BeautifulSoup(re.get('https://www.numbeo.com/cost-of-living/rankings.jsp').text, 'html.parser')
    soup = soup.select('tr[style]')
    for ele in soup:
        city = ele.select('td[class]')[0].text.split(',')[0].upper()
        if city in [ele['city'].upper() for ele in cities]:
            indCost = float(ele.select('td')[2].text)
            for ele in cities:
                if ele['city'].upper() == city:
                    ele['liveCostIndex'] = indCost
    return cities