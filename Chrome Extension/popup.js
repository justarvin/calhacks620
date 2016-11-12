console.log("hi")

document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('submitbutton');
    // onClick's logic below:
    link.addEventListener('click', function() {
        console.log('xxx');
    });
});