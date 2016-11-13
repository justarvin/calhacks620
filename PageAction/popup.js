document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('enter');
    // onClick's logic below:
    link.addEventListener('click', function() {
        var myUsername = 'username';
        var myPassword = 'password';
        // find the fiends in your lo
        document.getElementsByName('ctlLogin$UserName').value = myUsername;
        document.getElementsByName('ctlLogin$Password').value = myPassword;
    });
});