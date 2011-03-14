
import HunchPy

tmp = HunchPy.HunchReq().set_user_id("tw_oprah").set_limit("3").set_topic_ids("list_magazine")

#filepoint = tmp.get_fp()

for elt in tmp.get_recommendations()['recommendations']:
    for key in iter(elt):
        print str(key) + '\n'

#for line in filePoint:
 #   print line
