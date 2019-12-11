function launch_toast(e, type){
    console.log(`${e} ${type}`);
    var x = document.getElementById("toast");
    // console.log(x);
    var icon = document.getElementById("imgToast");
    icon.innerHTML="";
    var iTag = document.createElement("i");
    if(type==1){
      iTag.setAttribute("class","fas fa-check");
    }else{
      // alert(x)
      iTag.setAttribute("class","fas fa-exclamation");
    }
    icon.appendChild(iTag);
    x.className = "show";
    if(type!=1){
      x.classList.add("redAlert");imgToast
      document.getElementById('imgToast').classList.add("darkRed");
      document.getElementById('desc').classList.add("redAlert");
    }
    document.getElementById('desc').innerHTML = e;
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
  }


