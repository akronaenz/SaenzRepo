function consult_user(){
    let id = document.getElementById("ident").value
    fetch('/consult_user', {
         'method': 'post',
         'headers': {'Content-type' : 'application/json'},
         'body': JSON.stringify(id)
    } )
    .then(resp => resp.json())
    .then(data => {
        document.getElementById("txt-user").value = data.name + " " + data.lastname + " " + data.birthay
    })
    .catch(error => alert("Error"))
}