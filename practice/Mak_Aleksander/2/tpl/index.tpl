$def with (context)


    
    
    <html>
        <head>
            <title>Hello User!</title>
        </head>
        <body>
        
        
            $if context['name']:
                I just wanted to say <em>hello</em> to context['name'].
            $else:
                <em>Hello</em>, world!
    
                
            <ul>
            $for user in context['db']:
                <li>$user['name']</li>
            </ul>    
                        
    
            <form method="post" action="/ddd">
                <label>Add</label>
                <input type="text" name="name">
                <input type="submit" value="Go">
            </form>
        </body>
    </html>
© 2018 GitHub, Inc.