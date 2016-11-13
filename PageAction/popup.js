document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('submitbutton');
    // onClick's logic below:
    link.addEventListener('click', function() {
        myurl = document.getElementById("url").value
        mypsw = document.getElementById("password").value
        myuserid = document.getElementById("userid").value
        console.log(myurl)
        console.log(mypsw)
        console.log(myuserid)
    });
});
