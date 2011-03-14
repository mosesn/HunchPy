
import HunchPy

#tmp = HunchPy.HunchReq().set_twitter("oprah").set_limit("3").set_topic("list_magazine")

tmp = open('rec.html')

#filepoint = tmp.get_fp()

for elt in tmp.get_rec()['recommendations']:
    for key in iter(elt):
        print str(key) + '\n'

#for line in filePoint:
 #   print line
