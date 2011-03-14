import re

#matcher = re.compile(r'<code>([^<]+)')
matcher = re.compile(r'<tr>[\s]+<td><code>([^<]+)')
#fp = open('rec.html')

lst =[]

file_list = [("get-recommendations","get-rec.txt"),("get-results","get-res.txt"),("get-similar-results","get-sim-res.txt"),("flag-result","flag-res.txt"),("create-result","create-result.txt"),("edit-result","edit-res.txt"),("delete-result","del-res.txt"),("set-result-alias","set-res-alias.txt"),("get-auth-token","get-auth-tok.txt"),("get-token-status","get-tok-stat.txt"),("get-user-info","get-user-info.txt"),("get-friends","get-friends.txt"),("get-tastemates","get-tastemates.txt"),("get-recommendees","get-recommendees.txt"),("set-user-alias","set-user-alias.txt"),("get-result-topics","get-res-topics.txt"),("get-topics","get-topics.txt"),("get-activity","get-activity.txt"),("get-preferences","get-prefs.txt"),("get-pro-cons","get-pro-con.txt"),("set-preference","set-pref.txt"),("set-pro-cons","set-pro-con.txt"),("delete-preference","delete-pref.txt"),("get-predictions","get-predictions.txt"),("get-questions","get-questions.txt"),("teach-hunch-about-you","teach-hunch-about-you.txt")]

for tup in file_list:
    fp = open(tup[1])

    print "    def "+tup[0].replace("-","_")+":"
    print "        lst = []"
    print "        "
    print "        tmp = None"


#for line in fp.readlines():
    #    tmp = matcher.search(line)
    for tmp in fp.readlines():
        if tmp:
            print "        tmp =  self.get_"+tmp.strip()+"()"
            print "        if tmp:"
            print "            lst.append(tmp)"
            print "        tmp = None"
            print "        "
 #           lst.append(str(tmp.group(1)))

    print '        q_str = "&".join(lst)'
    print '        urlstr = "http://api.hunch.com/api/v1/"+tup[0]+"/?"+q_str'
    print "        "
    print "        return json.load(urllib2.urlopen(urlstr))"
    print "        "
#lst = list(set(lst))
#    new_lst = []

#    for x in lst:
#        new_lst.extend(x.split(" "))

#    lst = new_lst

#    for x in lst:
#        print x
#    print '    def get_' + x + '(self):'
#    print '        if self.'+x+':'
#    print '            return "' + x + '=" + self.' + x
#    print '        else:'
#    print '            return self.'+x
#    print ''
    
#    print '    def set_' + x + '(self,my_'+x+'):'
#    print '        self.'+x+' = my_' + x
#    print '        return self'
#    print ''
