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
// MODAL EDITAR TALLER
document.getElementById("btn-edit").addEventListener("click",()=>{
  let modal1 = document.getElementById("modal-workshop").style.display="flex";
});
// CERRAR MODAL DE EDITAR TALLER
document.getElementById("modal-btn2").addEventListener("click",()=>{
  var modal = document.getElementById("modal-workshop").style.display="none";
});



// MODAL AGREGAR ALUMNO
document.getElementById("addmember").addEventListener("click",()=>{
  let modal1 = document.getElementById("modal-addmember").style.display="flex";
});

// CERRAR MODAL DE EDITAR TALLER
document.getElementById("closeadd").addEventListener("click",()=>{
  var modal = document.getElementById("modal-addmember").style.display="none";
});