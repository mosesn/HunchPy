
import urllib2
import json

def fib(n):
    alpha = 0
    beta = 1
    for i in range(n):
        alpha , beta = beta , alpha + beta
    return alpha

#returns a file pointer
def demo_call():
    urlstr = "http://api.hunch.com/api/v1/get-recommendations/?user_id=tw_oprah&topic_ids=list_magazine&limit=3"
    return urllib2.urlopen(urlstr)

class HunchReq:
    def __init__(self):
        self.topic = ""
        self.limit = None
        self.twitter = ""
    
#returns a file pointer
    def get_rec(self):
        lst = []

        usr_req = self.get_name()
        usr_top = self.get_topic()
        usr_limit = self.get_limit()

        if usr_req:
            lst.append(usr_req)
        if usr_top:
            lst.append(usr_top)
        if usr_limit:
            lst.append(usr_limit)

        q_str = "&".join(lst)

        urlstr = "http://api.hunch.com/api/v1/get-recommendations/?"+q_str

        return json.load(urllib2.urlopen(urlstr))

    #formats user_id
    #only handles twitter names now
    def get_name(self):
        if self.twitter:
            return "user_id=tw_" + self.twitter
        else:
            return ""

    #formats topic_id
    def get_topic(self):
        if self.topic:
            return "topic_ids="+self.topic
        else:
            return ""

    #formats limit num
    def get_limit(self):
        if self.limit:
            return "limit="+self.limit
        else:
            return ""

    #sets twitter handle
    def set_twitter(self,tw_name):
        self.twitter = tw_name
        return self

    #sets topic name
    def set_topic(self, topic_name):
        self.topic = topic_name
        return self

    #sets limit
    def set_limit(self, cur_limit):
        self.limit = cur_limit
        return self

class Rec_collection:
    def __init__(self,dicty):
        self.full_resp = dicty

    def get_total():
        return self.full_resp['total']

    def ok():
        return self.full_resp['ok']

    def is_personalized():
        return self.full_resp['is_personalized']

    def recommendations():
        return self.full_resp['recommendations']

    def rec_urls():
        return [i['urls'] for i in self.full_resp['recommendations']]

class Rec:
    def __init__(self, dicty):
        self.urls = dicty['urls']
        self.pro_cons = dicty['pro_cons']
        self.preferences = dicty['preferences']
        self.wildcard = dicty['wildcare']
        self.topic_ids = dicty['topic_ids']
        self.url = dicty['url']
        self.description = dicty['description']
        self.categories = dicty['categories']
        self.image_urls = dicty['image_urls']
        self.popularity = dicty['popularity']
        self.score = dicty['score']
        self.affiliate_links = dicty['affiliate_links']
        self.is_personalized = dicty['is_personalized']
        self.stars = dicty['stars']
        self.image_url = dicty['image_url']
        self.aliases = dicty['aliases']
        self.result_id = dicty['result_id']
        self.price = dicty['price']
        
        self.name = dicty['name']        
