// var FHIRrootURL ="http://hapi.fhir.org/baseR4";
//var FHIRrootURL ="http://203.64.84.213:52888/r4/fhir";

var FHIRrootURL ='https://59.126.239.51:53443/fhir';
var globalPatientID;
function queryParam(){
	var url = location.href;
	if(url.indexOf('?')!=-1)
	{
		var ary = url.split('?')[1].split('&');
		for(i=0;i<=ary.length-1;i++)
		{
			if(ary[i].split('=')[0] == 'patientID')
				globalPatientID = ary[i].split('=')[1];
			
		}
	}
}
