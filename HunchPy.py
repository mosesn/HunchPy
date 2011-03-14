
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

    def get_recommendations:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_radius()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_query()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_name()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_tags()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_exclude_likes()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_exclude_dislikes()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minimal()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_exclude_chains()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_likes()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_dislikes()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_responses()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_friend_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_limit()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_offset()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_wildcards()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_results:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_radius()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_query()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_name()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_tags()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minimal()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_limit()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_offset()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_similar_results:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_radius()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_query()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_name()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_tags()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_limit()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_offset()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_wildcards()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def flag_result:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_message()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def create_result:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_name()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_description()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_tags()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_url()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def edit_result:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_name()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_description()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_tags()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_url()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def delete_result:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def set_result_alias:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_id1()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_id2()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_auth_token:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_token_key()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_token_status:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_user_info:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_friends:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_friend_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_sort()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_reverse()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_limit()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_offset()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_tastemates:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_radius()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_query()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_name()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_tags()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_limit()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_offset()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_recommendees:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_limit()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_offset()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_wildcards()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def set_user_alias:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_user_id1()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_user_id2()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_result_topics:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_radius()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_query()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_name()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_tags()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_topics:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_activity:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_user_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_lng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_radius()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlat()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_minlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_maxlng()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_query()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_name()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_tags()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_limit()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_offset()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_preferences:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_sites()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_types()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_limit()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_offset()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_pro_cons:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_user_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_limit()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_offset()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def set_preference:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_types()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_rating()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_pros()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_cons()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_friend_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def set_pro_cons:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_pros()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_cons()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def delete_preference:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_result_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_topic_ids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_types()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_friend_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_predictions:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_allowed_qids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_qids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_blocked_rids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_avoid_rids()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_likes()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_dislikes()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_responses()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_limit()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_offset()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_questions:
        lst = []
        
        tmp = None
        tmp =  self.get_app_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_auth_sig()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_question_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def teach_hunch_about_you:
        lst = []
        
        tmp = None
        tmp =  self.get_auth_token()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_question_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_response_id()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_callback()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        tmp =  self.get_suppress_http_errors()
        if tmp:
            lst.append(tmp)
        tmp = None
        
        q_str = "&".join(lst)
        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str
        
        return json.load(urllib2.urlopen(urlstr))
        
    def get_wildcards(self):
        if self.wildcards:
            return "wildcards=" + self.wildcards
        else:
            return self.wildcards

    def set_wildcards(self,my_wildcards):
        self.wildcards = my_wildcards
        return self

    def get_rating(self):
        if self.rating:
            return "rating=" + self.rating
        else:
            return self.rating

    def set_rating(self,my_rating):
        self.rating = my_rating
        return self

    def get_reverse(self):
        if self.reverse:
            return "reverse=" + self.reverse
        else:
            return self.reverse

    def set_reverse(self,my_reverse):
        self.reverse = my_reverse
        return self

    def get_topic_ids(self):
        if self.topic_ids:
            return "topic_ids=" + self.topic_ids
        else:
            return self.topic_ids

    def set_topic_ids(self,my_topic_ids):
        self.topic_ids = my_topic_ids
        return self

    def get_friend_id(self):
        if self.friend_id:
            return "friend_id=" + self.friend_id
        else:
            return self.friend_id

    def set_friend_id(self,my_friend_id):
        self.friend_id = my_friend_id
        return self

    def get_auth_token(self):
        if self.auth_token:
            return "auth_token=" + self.auth_token
        else:
            return self.auth_token

    def set_auth_token(self,my_auth_token):
        self.auth_token = my_auth_token
        return self

    def get_dislikes(self):
        if self.dislikes:
            return "dislikes=" + self.dislikes
        else:
            return self.dislikes

    def set_dislikes(self,my_dislikes):
        self.dislikes = my_dislikes
        return self

    def get_allowed_qids(self):
        if self.allowed_qids:
            return "allowed_qids=" + self.allowed_qids
        else:
            return self.allowed_qids

    def set_allowed_qids(self,my_allowed_qids):
        self.allowed_qids = my_allowed_qids
        return self

    def get_blocked_qids(self):
        if self.blocked_qids:
            return "blocked_qids=" + self.blocked_qids
        else:
            return self.blocked_qids

    def set_blocked_qids(self,my_blocked_qids):
        self.blocked_qids = my_blocked_qids
        return self

    def get_user_id1(self):
        if self.user_id1:
            return "user_id1=" + self.user_id1
        else:
            return self.user_id1

    def set_user_id1(self,my_user_id1):
        self.user_id1 = my_user_id1
        return self

    def get_exclude_likes(self):
        if self.exclude_likes:
            return "exclude_likes=" + self.exclude_likes
        else:
            return self.exclude_likes

    def set_exclude_likes(self,my_exclude_likes):
        self.exclude_likes = my_exclude_likes
        return self

    def get_user_id2(self):
        if self.user_id2:
            return "user_id2=" + self.user_id2
        else:
            return self.user_id2

    def set_user_id2(self,my_user_id2):
        self.user_id2 = my_user_id2
        return self

    def get_likes(self):
        if self.likes:
            return "likes=" + self.likes
        else:
            return self.likes

    def set_likes(self,my_likes):
        self.likes = my_likes
        return self

    def get_query(self):
        if self.query:
            return "query=" + self.query
        else:
            return self.query

    def set_query(self,my_query):
        self.query = my_query
        return self

    def get_message(self):
        if self.message:
            return "message=" + self.message
        else:
            return self.message

    def set_message(self,my_message):
        self.message = my_message
        return self

    def get_question_id(self):
        if self.question_id:
            return "question_id=" + self.question_id
        else:
            return self.question_id

    def set_question_id(self,my_question_id):
        self.question_id = my_question_id
        return self

    def get_description(self):
        if self.description:
            return "description=" + self.description
        else:
            return self.description

    def set_description(self,my_description):
        self.description = my_description
        return self

    def get_result_id1(self):
        if self.result_id1:
            return "result_id1=" + self.result_id1
        else:
            return self.result_id1

    def set_result_id1(self,my_result_id1):
        self.result_id1 = my_result_id1
        return self

    def get_blocked_topic_ids(self):
        if self.blocked_topic_ids:
            return "blocked_topic_ids=" + self.blocked_topic_ids
        else:
            return self.blocked_topic_ids

    def set_blocked_topic_ids(self,my_blocked_topic_ids):
        self.blocked_topic_ids = my_blocked_topic_ids
        return self

    def get_result_id2(self):
        if self.result_id2:
            return "result_id2=" + self.result_id2
        else:
            return self.result_id2

    def set_result_id2(self,my_result_id2):
        self.result_id2 = my_result_id2
        return self

    def get_pros(self):
        if self.pros:
            return "pros=" + self.pros
        else:
            return self.pros

    def set_pros(self,my_pros):
        self.pros = my_pros
        return self

    def get_sites(self):
        if self.sites:
            return "sites=" + self.sites
        else:
            return self.sites

    def set_sites(self,my_sites):
        self.sites = my_sites
        return self

    def get_blocked_sites(self):
        if self.blocked_sites:
            return "blocked_sites=" + self.blocked_sites
        else:
            return self.blocked_sites

    def set_blocked_sites(self,my_blocked_sites):
        self.blocked_sites = my_blocked_sites
        return self

    def get_topic_id(self):
        if self.topic_id:
            return "topic_id=" + self.topic_id
        else:
            return self.topic_id

    def set_topic_id(self,my_topic_id):
        self.topic_id = my_topic_id
        return self

    def get_response_id(self):
        if self.response_id:
            return "response_id=" + self.response_id
        else:
            return self.response_id

    def set_response_id(self,my_response_id):
        self.response_id = my_response_id
        return self

    def get_app_id(self):
        if self.app_id:
            return "app_id=" + self.app_id
        else:
            return self.app_id

    def set_app_id(self,my_app_id):
        self.app_id = my_app_id
        return self

    def get_auth_sig(self):
        if self.auth_sig:
            return "auth_sig=" + self.auth_sig
        else:
            return self.auth_sig

    def set_auth_sig(self,my_auth_sig):
        self.auth_sig = my_auth_sig
        return self

    def get_minimal(self):
        if self.minimal:
            return "minimal=" + self.minimal
        else:
            return self.minimal

    def set_minimal(self,my_minimal):
        self.minimal = my_minimal
        return self

    def get_sort(self):
        if self.sort:
            return "sort=" + self.sort
        else:
            return self.sort

    def set_sort(self,my_sort):
        self.sort = my_sort
        return self

    def get_responses(self):
        if self.responses:
            return "responses=" + self.responses
        else:
            return self.responses

    def set_responses(self,my_responses):
        self.responses = my_responses
        return self

    def get_cons(self):
        if self.cons:
            return "cons=" + self.cons
        else:
            return self.cons

    def set_cons(self,my_cons):
        self.cons = my_cons
        return self

    def get_tags(self):
        if self.tags:
            return "tags=" + self.tags
        else:
            return self.tags

    def set_tags(self,my_tags):
        self.tags = my_tags
        return self

    def get_exclude_chains(self):
        if self.exclude_chains:
            return "exclude_chains=" + self.exclude_chains
        else:
            return self.exclude_chains

    def set_exclude_chains(self,my_exclude_chains):
        self.exclude_chains = my_exclude_chains
        return self

    def get_lat(self):
        if self.lat:
            return "lat=" + self.lat
        else:
            return self.lat

    def set_lat(self,my_lat):
        self.lat = my_lat
        return self

    def get_lng(self):
        if self.lng:
            return "lng=" + self.lng
        else:
            return self.lng

    def set_lng(self,my_lng):
        self.lng = my_lng
        return self

    def get_radius(self):
        if self.radius:
            return "radius=" + self.radius
        else:
            return self.radius

    def set_radius(self,my_radius):
        self.radius = my_radius
        return self

    def get_exclude_dislikes(self):
        if self.exclude_dislikes:
            return "exclude_dislikes=" + self.exclude_dislikes
        else:
            return self.exclude_dislikes

    def set_exclude_dislikes(self,my_exclude_dislikes):
        self.exclude_dislikes = my_exclude_dislikes
        return self

    def get_user_ids(self):
        if self.user_ids:
            return "user_ids=" + self.user_ids
        else:
            return self.user_ids

    def set_user_ids(self,my_user_ids):
        self.user_ids = my_user_ids
        return self

    def get_offset(self):
        if self.offset:
            return "offset=" + self.offset
        else:
            return self.offset

    def set_offset(self,my_offset):
        self.offset = my_offset
        return self

    def get_avoid_rids(self):
        if self.avoid_rids:
            return "avoid_rids=" + self.avoid_rids
        else:
            return self.avoid_rids

    def set_avoid_rids(self,my_avoid_rids):
        self.avoid_rids = my_avoid_rids
        return self

    def get_lat(self):
        if self.lat:
            return "lat=" + self.lat
        else:
            return self.lat

    def set_lat(self,my_lat):
        self.lat = my_lat
        return self

    def get_lng(self):
        if self.lng:
            return "lng=" + self.lng
        else:
            return self.lng

    def set_lng(self,my_lng):
        self.lng = my_lng
        return self

    def get_types(self):
        if self.types:
            return "types=" + self.types
        else:
            return self.types

    def set_types(self,my_types):
        self.types = my_types
        return self

    def get_blocked_result_ids(self):
        if self.blocked_result_ids:
            return "blocked_result_ids=" + self.blocked_result_ids
        else:
            return self.blocked_result_ids

    def set_blocked_result_ids(self,my_blocked_result_ids):
        self.blocked_result_ids = my_blocked_result_ids
        return self

    def get_auth_token_key(self):
        if self.auth_token_key:
            return "auth_token_key=" + self.auth_token_key
        else:
            return self.auth_token_key

    def set_auth_token_key(self,my_auth_token_key):
        self.auth_token_key = my_auth_token_key
        return self

    def get_name(self):
        if self.name:
            return "name=" + self.name
        else:
            return self.name

    def set_name(self,my_name):
        self.name = my_name
        return self

    def get_result_ids(self):
        if self.result_ids:
            return "result_ids=" + self.result_ids
        else:
            return self.result_ids

    def set_result_ids(self,my_result_ids):
        self.result_ids = my_result_ids
        return self

    def get_user_id(self):
        if self.user_id:
            return "user_id=" + self.user_id
        else:
            return self.user_id

    def set_user_id(self,my_user_id):
        self.user_id = my_user_id
        return self

    def get_url(self):
        if self.url:
            return "url=" + self.url
        else:
            return self.url

    def set_url(self,my_url):
        self.url = my_url
        return self

    def get_suppress_http_errors(self):
        if self.suppress_http_errors:
            return "suppress_http_errors=" + self.suppress_http_errors
        else:
            return self.suppress_http_errors

    def set_suppress_http_errors(self,my_suppress_http_errors):
        self.suppress_http_errors = my_suppress_http_errors
        return self

    def get_callback(self):
        if self.callback:
            return "callback=" + self.callback
        else:
            return self.callback

    def set_callback(self,my_callback):
        self.callback = my_callback
        return self

    def get_token(self):
        if self.token:
            return "token=" + self.token
        else:
            return self.token

    def set_token(self,my_token):
        self.token = my_token
        return self

    def get_limit(self):
        if self.limit:
            return "limit=" + self.limit
        else:
            return self.limit

    def set_limit(self,my_limit):
        self.limit = my_limit
        return self

    def get_calls(self):
        if self.calls:
            return "calls=" + self.calls
        else:
            return self.calls

    def set_calls(self,my_calls):
        self.calls = my_calls
        return self

    def get_friend_ids(self):
        if self.friend_ids:
            return "friend_ids=" + self.friend_ids
        else:
            return self.friend_ids

    def set_friend_ids(self,my_friend_ids):
        self.friend_ids = my_friend_ids
        return self

    def get_minlat(self):
        if self.minlat:
            return "minlat=" + self.minlat
        else:
            return self.minlat

    def set_minlat(self,my_minlat):
        self.minlat = my_minlat
        return self

    def get_maxlat(self):
        if self.maxlat:
            return "maxlat=" + self.maxlat
        else:
            return self.maxlat

    def set_maxlat(self,my_maxlat):
        self.maxlat = my_maxlat
        return self

    def get_minlng(self):
        if self.minlng:
            return "minlng=" + self.minlng
        else:
            return self.minlng

    def set_minlng(self,my_minlng):
        self.minlng = my_minlng
        return self

    def get_maxlng(self):
        if self.maxlng:
            return "maxlng=" + self.maxlng
        else:
            return self.maxlng

    def set_maxlng(self,my_maxlng):
        self.maxlng = my_maxlng
        return self

    def get_result_id(self):
        if self.result_id:
            return "result_id=" + self.result_id
        else:
            return self.result_id

    def set_result_id(self,my_result_id):
        self.result_id = my_result_id
        return self

    def get_blocked_rids(self):
        if self.blocked_rids:
            return "blocked_rids=" + self.blocked_rids
        else:
            return self.blocked_rids

    def set_blocked_rids(self,my_blocked_rids):
        self.blocked_rids = my_blocked_rids
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
        self.tags = dicty['tags']
        self.name = dicty['name']
        self.my_dict = dicty

    def get_urls(self):
        return self.urls

    def get_pro_cons(self):
        return self.pro_cons

    def get_preferences(self):
        return self.preferences

    def get_wildcard(self):
        return self.wildcard

    def get_topic_ids(self):
        return self.topic_ids

    def get_url(self):
        return self.url

    def get_description(self):
        return self.description

    def get_categories(self):
        return self.categories

    def get_image_urls(self):
        return self.image_urls

    def get_popularity(self):
        return self.popularity

    def get_score(self):
        return self.score

    def get_affiliate_links(self):
        return self.affiliate_links

    def get_is_personalized(self):
        return self.is_personalized

    def get_stars(self):
        return self.stars

    def get_image_url(self):
        return self.image_url

    def get_aliases(self):
        return self.aliases

    def get_result_id(self):
        return self.result_id

    def get_price(self):
        return self.price

    def get_tags(self):
        return self.tags

    def get_name(self):
        return self.name

    def get_my_dict(self):
        return self.my_dict

