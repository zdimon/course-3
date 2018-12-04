import web
import json
render = web.template.render('tpl/')

def db_read():
    with open("db.txt") as dbfile:
        d = json.load(dbfile)
        print(d)
        return d
        
db = db_read()
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())



class hello:        

    def POST(self,url):
        name = 'Dima' 
        i = web.input()
        db_append({"name": i["name"]})
        #import pdb; pdb.set_trace()
        return render.index({'name':name,'db':db})
        
        
    def GET(self, name):
        name = 'Dima'
        return render.index({"name":name,"db":db})
        '''
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'
        '''

def db_append(name):
    #db.append(name)
    with open("db.txt", mode='w', encoding='utf-8') as feedsjson:
        db.append(name)
        json.dump(db, feedsjson)
    


if __name__ == "__main__":
    app.run()
