// API CODE FOR GETTING RANDOM QUOTES IN HOME PAGE
var getQuote=async()=>{
    var request=await fetch("http://api.quotable.io/random")
    var response= await request.json();
    console.log(response);document.querySelector(".quote").innerHTML=`"${response.content}"`;
    console.log(response);document.querySelector(".author").innerHTML=`By:${response.author}`;

}
getQuote();

//*********************************************************************** */
// RANDOM QUOTES IMAGES CODE INSIDE ADD AND UPDATE ACTIVITY PAGE
window.onload = choosePic;

var myPix = new Array("/static/images/ali.png", "/static/images/sailor.jpg", "/static/images/bigjourney.jpg", "/static/images/inspiration.jpg", "/static/images/proud.png");

function choosePic() {
    var randomNum = Math.floor(Math.random() * myPix.length);
    console.log(randomNum)
    document.getElementById("myPicture").src = myPix[randomNum];
}
//***************************************************************** */

// script for dropdown box in add and edit forms
$(document).ready(function(e) {
    try {
    $("body select").msDropDown();
    } catch(e) {
    alert(e.message);
    }
    });
//************************************************************** */
// add advice box implementation

function removeHidden(){
    document.querySelector(".advice_box").classList.remove("hidden");
}
setTimeout(removeHidden, 2000);

function runClose(){
    document.querySelector(".advice_box").classList.add("hidden");
}





