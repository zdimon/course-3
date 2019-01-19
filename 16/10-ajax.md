# Ajax request

    ln -s node_modules/jquery/dist jquery
    
    
Library

      <script src="/static/jquery/jquery.min.js"></script>
      <script src="{% static 'prj.js' %}"></script>
      
      
     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script> 
      
      
Form

            <ul class="navbar-nav " id="logout_link" style="display: none">
                <li class="nav-item active">
                  <a class="nav-link" href="{% url 'logout' %}">Logout</a>
                </li>
              </ul>
            <form action="{% url 'login' %}" method="POST" id="login_form" class="form-inline mt-2 mt-md-0">
                    {% csrf_token %}
                    <input class="form-control mr-sm-2" type="text" id="login" name="login" placeholder="Login" >
                    <input class="form-control mr-sm-2" type="text" id="password" name="password" placeholder="Password" >
                    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">SignIn</button>
                    <button id="login_link" class="btn btn-outline-success my-2 my-sm-0"> Login AJAX </button>
            </form>
            
JS




    function success(data){
        
        if(data.status==0){
            $('#login_form').hide();
            $('#logout_link').show();
        } 
        alert(data.message);
    }

    function ajax_login(){

    data = {
        'login': $('#login').val(),
        'password':  $('#password').val(),
        'csrfmiddlewaretoken': $( "[name='csrfmiddlewaretoken']" ).val()
    }

    $.ajax({
        type: "POST",
        url: "/account/alogin",
        data: data,
        success: success
      });

    }

    $('#login_link').on('click',ajax_login);
    
    
Plugin 

    pip install django-jsonview
    
    
URL

    path('alogin', alogin, name='alogin'),
    
    
View

    from jsonview.decorators import json_view

    @json_view
    def alogin(request):
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            l(request, user)
            return { 'status': 0, 'message': 'Welcome!!!!' }
        else:
            return { 'status': 1, 'message': 'Login or password incorrect!!!' }
                
        
        
    
    
    
    
    
    

