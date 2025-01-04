// Check if the cookie is present
if (getCookie("accepted_cookies") === "true") {
    // Hide the cookie notice
    document.getElementById("cookie-notice").style.display = "none";
} else {
    document.getElementById("cookie-notice").style.display = "block";
}

// Function to get cookie value by name
function getCookie(cookieName) {
    var name = cookieName + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var cookieArray = decodedCookie.split(';');
    for(var i = 0; i <cookieArray.length; i++) {
        var cookie = cookieArray[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) === 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return "";
}

// Add event listener to accept button
document.getElementById("cookies-accept").addEventListener("click", function() {
    // Hide the cookie notice
    document.getElementById("cookie-notice").style.display = "none";
    // Create expiration date 30 days from now
    var expirationDate = new Date();
    expirationDate.setDate(expirationDate.getDate() + 30);
    // Format expiration date as UTC string
    var expirationDateStr = expirationDate.toUTCString();
    // Create the cookie
    document.cookie = "accepted_cookies=true; expires=" + expirationDateStr + "; path=/";
});