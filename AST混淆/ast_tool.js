const {parse} = require('@babel/parser');
const fs = require('fs');
const traverse = require('@babel/traverse').default;
const types = require("@babel/types");
const generator = require('@babel/generator').default;

process.argv.length > 2 ? File1 = process.argv[2] : File1 = './encode.js'
process.argv.length > 3 ? File2 = process.argv[3] : File2 = './result.js'


jscode = fs.readFileSync(File1,{encoding:'utf-8'})
let ast = parse(jscode)
console.log(ast)
//处理字面量想加

const __nn = {
    BinaryExpression(path) {
        let {left,right,operator} = path.node
        if (types.isNumericLiteral(left) && types.isNumericLiteral(right) && operator == "+") {
            value = left.value + right.value
            console.log(value)
            path.replaceWith(types.valueToNode(value))
        }

        //处理字符串类型的相加
        if (types.isStringLiteral(left) && types.isStringLiteral(right) && operator == "+" ) {
            value = left.value + right.value
            console.log(value)
            path.replaceWith(types.valueToNode(value))
        }
    }

}
traverse(ast,__nn)


let {code} = generator(ast,opts =  {jsescOption:{"minimal":true}});
// console.log(code);
fs.writeFile(File2, code, (err) => {});