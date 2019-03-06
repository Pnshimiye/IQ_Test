
import urllib.request,json
from .models import Quote
 
# base_url = None

def configure_request(app):
    global base_url   
    



def get_onequote():
    base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(base_url) as url:
            onequote_data = url.read()
            onequote_response = json.loads(onequote_data)

            quote_object = None
            if onequote_response:
                author= onequote_response.get('author')
                id = onequote_response.get('id')
                quote = onequote_response.get('quote')        

                quote_object = Quote(author,id,quote)

            return quote_object

