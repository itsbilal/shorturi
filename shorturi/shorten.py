
import json
import urllib
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

def isgd (longuri):
	geturi		= "http://is.gd/create.php?" + urllib.urlencode({"url" : longuri, "format" : "json"})

	request		= urllib2.Request(geturi)
	response	= urllib2.urlopen(request)

	response_data	= response.read()
	shorturi	= json.loads(response_data)['shorturl']

	return shorturi		

def cligs (longuri):
	geturi		= "http://cli.gs/api/v1/cligs/create?" + urllib.urlencode({"url" : longuri})

	request		= urllib2.Request(geturi)
	response	= urllib2.urlopen(request)
	
	return response.read()
