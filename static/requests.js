var baseUrl =  "http://127.0.0.1:5000/home"
const name = document.getElementById("user")

function post(){

    var data = {
        "user": name.value
    }
    json = JSON.stringify(data)
    
    req = new XMLHttpRequest();
    
    req.open("POST", baseUrl, true);
    req.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    req.send(json);
}

