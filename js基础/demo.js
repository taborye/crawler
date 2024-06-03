

var pi = 3.14

var person = "Join one"

var answer = "yes i am"

//var const let  三个声明变量的方法

var carname
carname = "voivo"
var carname = "tabroye"
console.log(carname)


let name = "taborye"
console.log(name)

//let 声明的变量是块的作用域，var 声明的变量是函数的作用域
/*
(1).let允许声明一个作用域被限制在 块级中的变量、语句或者表达式。与 var 关键字不同的是， var声明的变量只能是全局或者整个函数块的。
(2) let 所声明的变量是在代码块内有效，属于块级的作用域,➡由{}决定
(3) let 声明的变量可以被修改，但是不能被重复声明
(4) let 不存在变量提升，切存在暂存死区
*/

let xa  = 2
{
    let xa = 3
    console.log(xa)
}

/**
 * const 声明变量的时候 和let一样 只能在声明时的块区间内使用
 * 且在申明时需要初始化。用const申明的变量是只读，一旦申明后不允许重复声明和修改。
 *
 */

//函数

//有名函数
function xxs() {
    console.log("xxs func")
}
xxs()

//函数赋值表达式定义函数
xxx = function (a,b,c) {
    console.log(a,b,c)
}
xxx(1,2,3)


//自执行函数：自执行也就是所谓的自动执行,也就是自己执行自己
!(function (){
    console.log("hello world")
}) ();
var x1
!(function (){
    var a = 3,b = 4,c = 5;
    function x2() {
        console.log(a,b,c)
    }
    x1 = x2
})()
x1()



var car = {name:"xiaoluo",model:500,color:"red",
toString:function (){
    return "name is " + this.name + "model is + " + this.model + "color is  " + this.color;
}};
console.log(car)

person = new Object();
    /**
     * constructor： 保存着用于创建当前对象的函数。
     * hasOwnProperty：用于检测给定的属性在当前对象的实例中是否存在。
     * isPrototypeOf ： 用于检查传入的对象是否是当前对象的原型
     * propertyIsEnumerble ： 用于检查给定属性能否使用for-in来枚举
     * toLocaleString() : 返回对象的字符串表示。
     * toString() : 返回对象的字符串表示。
     * valueOf() : 返回对象的字符串，数值，或布尔表示。通常和toString() 返回的值相同。
     *
     */

console.log(person.constructor)
console.log(car.constructor)

console.log(person.hasOwnProperty())
console.log(car.hasOwnProperty("name"))
console.log(Object.prototype.toString.call(car))
console.log(car.toString())


console.log(JSON.stringify(car))

var json_obj = JSON.stringify(car)

console.log(JSON.parse(json_obj))


