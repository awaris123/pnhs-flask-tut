var baseUrl =  "http://127.0.0.1:5000/home"


function post(){
    try{
        
      
        var form = document.forms["create"]
        var name = form.elements["user"]
        
        
        var data = {
            user : name.value
        }
        
        
        json = JSON.stringify(data)
        
        form.reset();
        $.ajax({
            contentType: 'application/json',
            type: "POST",
            url: baseUrl,
            data: json,
            success: function(data){
                console.log("it worked!");
            },
            dataType: "json"
          });
    }

    catch{
        console.log("request failed");
    }
    
}

function put(){
    try{
        var form = document.forms["change"];
        var name = document.forms["change"].elements["oldUser"]
        var newName = document.forms["change"].elements["newUser"]
    
        var data = {
            user : name.value,
            newUser: newName.value
        }
        
        json = JSON.stringify(data)
        form.reset();

    
        $.ajax({
            contentType: 'application/json',
            type: "PUT",
            url: baseUrl,
            data: json,
            success: function(data){
                console.log("it worked!");
            },
            dataType: "json"
          });
    }

    catch{
        console.log("request failed");
    }
    
}

function del(){
    try{
        
        var form = document.forms["kill"]
        var name = document.forms["kill"].elements["toDie"]
        
        
    
        var data = {
            user : name.value,
        }
        
        json = JSON.stringify(data)
        form.reset()
    
        $.ajax({
            contentType: 'application/json',
            type: "DELETE",
            url: baseUrl,
            data: json,
            success: function(data){
                console.log("it worked!");
            },
            dataType: "json"
          });
    }

    catch{
        console.log("request failed");
    }
    
}

