var string ='{ "name":"runoob", "alexa":10000, "site":"www.runoob.com" }'
var obj  = JSON.parse(string)
console.log(obj.name)
/*
使用循环读写对象属性的值，并显示
 */
for (variable in obj) {
	console.log(obj[variable])
}
var  object = JSON.parse(string,function (key,value) {
 	if (key == "name") {
 		return "yuanph"
 	}else {
 		return value
 	}
})
for (variable in obj) {
	console.log(obj[variable])
}
// var obj = { "name":"runoob", "alexa":10000, "site":"www.runoob.com"};
var json  = JSON.stringify(obj)
console.log(json)

