// Area of Triangle
// let side1 = 123;
// let side2 = 134;
// let side3 = 97;
// let perimeter = (side1+side2+side3)/2;
// let area = Math.sqrt((perimeter-side1)*(perimeter-side2)*(perimeter-side3));
// console.log("Area of Perimeter : ", area);

// function animate_string(id) 
// {
//     var element = document.getElementById(id);
//     var textNode = element.childNodes[0]; // assuming no other children
//     var text = textNode.data;

// setInterval(function () 
// {
//  text = text[text.length - 1] + text.substring(0, text.length - 1);
//   textNode.data = text;
// }, 100);
// }

// let user_input = prompt("Enter a number ?");
// let rand_num = Math.ceil(Math.random()*10)+1;
// if (user_input==rand_num)
//   console.log("Good work");
// else
//   console.log("Try again later");

var myArray0 = [32,false,"js",12,56,90];
// Splice(startingindex,number of indexes to remove,new values)
myArray0.splice(2,5,"hi","wr"); // = ["js",12,56,90]
// myArray0 === [32,false,"hi","wr","ld"]
console.log(myArray0);