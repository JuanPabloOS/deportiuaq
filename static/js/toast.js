function launch_toast(e, type){
    console.log("entrooooooooooooooooooooooooooooo");
    var x = document.getElementById("toast");
    // console.log(x);
    var icon = document.getElementById("imgToast");
    var iTag = document.createElement("i");
    if(type==1){
      iTag.setAttribute("class","fas fa-check");
    }else{
      iTag.setAttribute("class","fas fa-exclamation");
    }
    icon.appendChild(iTag);
    x.className = "show";
    document.getElementById('desc').innerHTML = e;
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
  }


