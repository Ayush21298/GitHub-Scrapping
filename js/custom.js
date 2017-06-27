if (document.title!="Github - Scrapping"){
  document.title="Github - Scrapping"
}

window.onload = function(){
  var list = document.getElementById('list');
  var reader = new XMLHttpRequest() || new ActiveXObject('MSXML2.XMLHTTP');
  content=""

  function loadFile() {
    reader.open('get', 'a.txt', true);
    reader.onreadystatechange = displayContents;
    reader.send(null);
  }

  function displayContents() {
    if(reader.readyState==4) {
      // content+=reader.responseText;
      var output=reader.responseText;
      var user="";
      var s = "";
      var b = 0
      for (var i=0;i<output.length;i++){
          if (output[i]==","){
            if(b==0){
              b=1;
              user=s;
              document.getElementById("legend").innerHTML=s;
            }
            else {
              content=content+"<li><a href='https://github.com/"+user+"/"+s+"'>"+s+"</a></li>";
              // content=content+"<li>"+s+"</li>"
            }
            s="";
          }
          else {
            s+=output[i];
          }
      }
      list.innerHTML=content;
    }
  }

  loadFile();
  // list.innerHTML=content

}
