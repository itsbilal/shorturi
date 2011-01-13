
import json
import urllib2

def googl (longuri, apikey=None):
	posturi		= "https://www.googleapis.com/urlshortener/v1/url"
	headers 	= {'Content-Type' : 'application/json'}
	data		= {'longUrl' : longuri}

	if apikey is not None:
		posturi += "?key=" + apikey

	data		= json.dumps(data)

	request		= urllib2.Request(posturi,data,headers)
	response	= urllib2.urlopen(request)
	
	response_data	= response.read()

	shorturi	= json.loads(response_data)['id']

	return shorturi
