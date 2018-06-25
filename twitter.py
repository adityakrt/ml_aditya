import tweepy
import csv
from textblob import TextBlob
ck='uIybI19HszGVyooKJTyqYFTXV'
csk='Oh8pJukZcRKWb2i7zW6T3f8gYsmXk4gKPFW57mnzfLawaaIxPO'
at='2736895531-BxoxhXm0vLrE0CEL5f1TJ4teFWSaLGDnrMAoiIG'
ast='o1t0Ho2j2ErH9vtv5QSqKk7T7qVlREHdFssX684S4m2q0'

#try :
#	auth = tweepy.OAuthHandler(ck, csk)
#	auth.set_access_token(at,ast)		
#	api = tweepy.API(auth)	
#except:
#	print('authentication failed')

pt = api.search('mitb2018')
with open('tweets.csv', 'w') as tp:
	a=csv.writer(tp,delimiter=',',quotechar='|')
	#a=xlsx.writer(tp)
	for i in pt:
		#print(i.text)
   		analysis = TextBlob(i.text)
   		#print(analysis.sentiment)
   		if analysis.sentiment.polarity>0:
   			b='positive'
   		elif analysis.sentiment.polarity<0:
   			b='negative'
   		else:
   			b='neutral'
   		a.writerow([i.text,analysis.sentiment])
with open('tweets.csv', 'r') as tr:
	reader = csv.reader(tr)
	for row in reader:
		print(row)
