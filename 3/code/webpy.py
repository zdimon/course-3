import web
render = web.template.render('tpl/')
        
db = [
    {'name': 'Dima'},
    {'name': 'Vova'}
]       
        
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        

    def POST(self,url):
        name = 'Dima' 
        i = web.input()
        db.append({'name': i['name']})
        #import pdb; pdb.set_trace()
        return render.index({'name':name,'db':db})
        
        
    def GET(self, name):
        name = 'Dima'    
        return render.index({'name':name,'db':db})
        '''
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'
        '''

if __name__ == "__main__":
    app.run()
