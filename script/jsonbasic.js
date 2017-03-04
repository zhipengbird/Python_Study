
var  obj,x;
obj= {"name":"bobo" ,"alexa":10000, "site":null};
x= obj.name;
console.log(obj['alexa'])
console.log(obj['site'])
console.log(x)
for (msg  in obj ) {
	console.log(msg)
}
function displayDate () {
	console.log(Date())
}
displayDate()

obj ={
	"name":"bobo" ,"alexa":10000, "sites":{
		'site1':"www.baidu.com",
		'site2':"www.baidu.com",
		'site3':"www.baidu.com"
	}
}
console.log(obj.sites.site1)
console.log(obj.sites['site1'])
obj.sites.site1= "www.google.com"
console.log(obj.sites.site1)
delete obj.sites.site1
for (www in obj.sites) {
	console.log(obj.sites[www])
}

