var coll = document.getElementsByClassName("option");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("option-active-list");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
	  content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}
function launch_toast(e){
  console.log("entrooooooooooooooooooooooooooooo");
	var x = document.getElementById("toast");
	
	console.log(x);
  x.className = "show";
  document.getElementById('desc').innerHTML = e;
	setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
}

