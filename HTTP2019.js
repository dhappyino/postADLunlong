var ret;
//取得網路上的資源
function HTTPGetData(urlStr) {
    var HttpObj = new XMLHttpRequest();
    HttpObj.onreadystatechange = function () {
        if (HttpObj.readyState === 4) {
            ret = HttpObj.responseText;
            //   alert(ret);
            callBack(ret);
            //   alert("data retrieved");
        }
    }
    HttpObj.open("GET", urlStr, true);
    HttpObj.send();
}

//上傳 dataStr 到網路上
function HTTPPostData(urlStr, dataStr) {
    var HttpObj = new XMLHttpRequest();
    HttpObj.open("POST", urlStr, true);
    HttpObj.setRequestHeader("Content-type", "application/json+fhir");
    // HttpObj.setRequestHeader("Content-type", "application/xml+fhir");
    HttpObj.onreadystatechange = function () {
        //alert(HttpObj.readyState);
        if (HttpObj.readyState === 4) {
            ret = HttpObj.responseText;
            //alert(ret);
            var jsonOBJ =JSON.parse(ret);
            if("id" in jsonOBJ && jsonOBJ.hasOwnProperty("id"))
              alert("上傳成功！" + "問卷編號：" + jsonOBJ["id"]);
            else
              alert("上傳失敗！"+ret);
        }
    }

    HttpObj.send(dataStr);
    //  getData
}

//上傳 dataStr 到網路上
function CB_HTTPPostData(urlStr, dataStr, cb) {
    var HttpObj = new XMLHttpRequest();
    HttpObj.open("POST", urlStr, true);
    HttpObj.setRequestHeader("Content-type", "application/json+fhir");
    // HttpObj.setRequestHeader("Content-type", "application/xml+fhir");
    HttpObj.onreadystatechange = function () {
        //alert(HttpObj.readyState);
        if (HttpObj.readyState === 4) {
            ret = HttpObj.responseText;
            cb(ret)
        }
    }

    HttpObj.send(dataStr);
    //  getData
}