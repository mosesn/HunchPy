import re

#matcher = re.compile(r'<code>([^<]+)')
matcher = re.compile(r'<tr>[\s]+<td><code>([^<]+)')
#fp = open('rec.html')

lst =[]

file_list = [("get-recommendations","get-rec.txt"),("get-results","get-res.txt"),("get-similar-results","get-sim-res.txt"),("flag-result","flag-res.txt"),("create-result","create-result.txt"),("edit-result","edit-res.txt"),("delete-result","del-res.txt"),("set-result-alias","set-res-alias.txt"),("get-auth-token","get-auth-tok.txt"),("get-token-status","get-tok-stat.txt"),("get-user-info","get-user-info.txt"),("get-friends","get-friends.txt"),("get-tastemates","get-tastemates.txt"),("get-recommendees","get-recommendees.txt"),("set-user-alias","set-user-alias.txt"),("get-result-topics","get-res-topics.txt"),("get-topics","get-topics.txt"),("get-activity","get-activity.txt"),("get-preferences","get-prefs.txt"),("get-pro-cons","get-pro-con.txt"),("set-preference","set-pref.txt"),("set-pro-cons","set-pro-con.txt"),("delete-preference","delete-pref.txt"),("get-predictions","get-predictions.txt"),("get-questions","get-questions.txt"),("teach-hunch-about-you","teach-hunch-about-you.txt")]

#for tup in file_list:
fp = open("ref_files/rec.html")

for tmp in matcher.finditer(fp.read()):
    if tmp:
        lst.append(tmp.group(1))

new_lst = []

for elt in lst:
    new_lst.extend(elt.split(" "))

lst = new_lst

lst = list(set(lst))

for tmp in lst:
    print "        self."+tmp+" = None"
