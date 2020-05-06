import requests
import json

def shortenURL(urlToShorten):
    r = requests.post("https://api.rebrandly.com/v1/links",

    data = json.dumps({
            "destination": urlToShorten
        , "domain": { "fullName": "rebrand.ly" }
        # , "slashtag": "A_NEW_SLASHTAG"
        # , "title": "Rebrandly YouTube channel"
    }),
    headers={
        "Content-type": "application/json",
        "apikey": "b58369bd708a41b39086d4ee9cead6ae"
    })

    if (r.status_code == requests.codes.ok):
        link = r.json()
        #print("Long URL was %s, short URL is %s" % (link["destination"], link["shortUrl"]))
        return link["shortUrl"]
    else:
        return r.status_code

