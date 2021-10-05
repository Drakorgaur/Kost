//$(document).ready(function () {
//    let url = new URL("https://frs.gov.cz/cs/ioff/application-status");
//    var http = new XMLHttpRequest();
//    http.open("get", url, true);
//    http.responseType = 'json';
//    http.send();
//    http.onload = function () {
//        alert(`Downloaded: ${http.status} ${http.response}`);
//        let responseObj = http.response;
//        alert(responseObj.message);
//    };

//    http.onerror = function () {
//        alert("Request failed");
//    };

//});