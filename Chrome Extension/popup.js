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


function storeUserPrefs() {
    var key = "myKey",
        testPrefs = JSON.stringify({
            'val': 10
        });
    var jsonfile = {};
    jsonfile[key] = testPrefs;
    chrome.storage.sync.set(jsonfile, function () {
        console.log('Saved', key, testPrefs);
    });
}
