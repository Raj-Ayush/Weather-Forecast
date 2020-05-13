function check(){
	var getElem = document.getElementById("mytext").value
	document.getElementById("Location").innerHTML = getElem
	document.getElementById("mytext").value=""

}

function empty() {
    var x;
    x = document.getElementById("mytext").value;
    if (x == "") {
        alert("Enter the text");
        return false;
    };
}
