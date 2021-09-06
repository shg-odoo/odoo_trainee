let a= 10
console.log(a)

console.log(5==="5")

a="abcdef"
console.log(a.charAt(0))
console.log(a.length)
console.log(a.substring(0,5))

var arr=["hello",1,2,3]
arr.push("world")
console.log(arr)
arr.unshift(4)
console.log(arr)
arr.shift()

console.log(arr)
console.log(arr.join(":"))
arr.splice(2,4,"hi","wr","ld")
console.log(arr)
objct={"a":1}
objct["b"]=2
for ( a in arr)
{
	console.log(a)}

for (a of arr){
	console.log(a)
}

grade = 'B';
switch (grade) {
  case 'A':
    console.log("Great job");
    break;
  case 'B':
    console.log("OK job");
    break;
  case 'C':
    console.log("You can do better");
    break;
  default:
    console.log("In default Block");
    break;
}
a="abc"
a.toUpperCase()
console.log(a.toUpperCase())

function iteration(){
	console.log("hello again !!")

}
//setInterval(iteration,5000)
//setTimeout(iteration,5000)

console.log(Math.min(1,2,3,4))

a=[1,2,3,4]
b=[5,6]
console.log(a+b)
console.log(typeof(a+b))
console.log(typeof(a))
console.log(typeof(b))
a.concat(b)
console.log(a.concat(b))


