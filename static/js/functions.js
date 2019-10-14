var launch_toast = ()=>{
	var x = document.getElementById("toast");
	console.log("====");
	console.log(x);
	x.className = "show";
	setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
}
function hi(){
	alert("adad");
}