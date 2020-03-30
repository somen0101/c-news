import requests
import json
from django import template
import re
register = template.Library()

@register.filter
def translater(sentence,country_name):
    c_name = country_name.split("/")[2]
    api = "https://script.google.com/macros/s/AKfycbxy9rc0bI6I4c8UUhFYUeuJT74Vx4pOaSq1BJ75GLKnoevXGnjh/exec?text={sentence}&source={country_name}&target=ja"
    new_sentence = re.sub(r"&.*?;", "", sentence)

    if c_name == "kr":
        url = api.format(country_name="ko", sentence=new_sentence)
    elif c_name == "gb" or c_name == "us":
        url = api.format(country_name="en", sentence=new_sentence)
    elif c_name == "cn":
        url = api.format(country_name="zh", sentence=new_sentence)
    elif c_name == "be":
        url = api.format(country_name="nl", sentence=new_sentence)
    else:
        url = api.format(country_name=c_name, sentence=new_sentence)
    r = requests.get(url)
    data = json.loads(r.text)
    return data["text"]
