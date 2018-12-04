import web
import json
import os

render=web.template.render('tpl/')
urls = ('/(.*)','add')
db=[]

##########Create a default DB##############
if not os.path.exists('data.json'):
	db=[{'name':'User'},]
	os.mknod('data.json')
	with open('data.json','w') as f:
		f.write(json.dumps(db))
###########################################	

#########ServerResponseBlock###############	
class add:
    def POST(self,url):
    	name='User'
    	i=web.input()
    	
    	with open('data.json','r') as f:
		data=f.read()
		db=json.loads(data)
	db.append({'name':i['name']})
	with open('data.json','w') as f:
		f.write(json.dumps(db))
    	return render.index({'name':name,'db':db})
    	
    def GET(self, name):
    	name='Admin'
    	return render.index({'name':name,'db':db}) 
############################################

############################################    	
if __name__ == "__main__":
	app = web.application(urls, globals())
 	app.run()