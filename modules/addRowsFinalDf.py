from apiQueries import getJsonFourSquare
def addByQuery(df,lat,long,query,distance = 10000):
    json = getJsonFourSquare(lat,long,query,distance,lim=50)
    for ele in json['response']['groups'][0]['items']:
        category = query
        name = ele['venue']['name']
        lat = ele['venue']['location']['lat']
        long = ele['venue']['location']['lng']
        df = df.append({'name':name,'category':category,'lat':lat,'long':long},ignore_index=True)
    return df

def addRows(df,lat,long):
    df = (addByQuery(df,lat,long,'Starbucks'))
    df = (addByQuery(df,lat,long,'University',distance=25000))
    df = (addByQuery(df,lat,long,'Bar'))
    df = (addByQuery(df,lat,long,'Vegan'))
    df = (addByQuery(df,lat,long,'Airport',distance=25000))
    df = (addByQuery(df,lat,long,'Bus Station'))
    df = (addByQuery(df,lat,long,'Museum'))
    df = (addByQuery(df,lat,long,'76ers'))
    return df