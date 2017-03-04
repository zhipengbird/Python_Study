var  array =['name','age','sex','alexa']
for (index  in array) {
	console.log(array[index])
}
for (var i = array.length - 1; i >= 0; i--) {
	console.log( array[i])
}
var  obj ={
	"name":"网站",
	"num":3,
	"sites": [
	{ "name":"Google", "info":[ "Android", "Google 搜索", "Google 翻译" ] },
	{ "name":"Runoob", "info":[ "菜鸟教程", "菜鸟工具", "菜鸟微信" ] },
	{ "name":"Taobao", "info":[ "淘宝", "网购" ] }
	]
}
/*
循环遍历每个数组
 */
for (index  in obj.sites) {
	console.log(obj.sites[index].name)
	for (inf  in obj.sites[index].info) {
		console.log(obj.sites[index].info[inf])
		console.log('-----')
	}
	console.log('-----')

}

/*
修改数组的值
 */
array[0]='age+name'
console.log(array[0])
/*
删除数组元素
 */
delete array[0]
console.log(array[1])
console.log(array[0])
console.log(array.length)