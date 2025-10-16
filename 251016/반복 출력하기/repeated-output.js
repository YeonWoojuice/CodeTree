function printStr(n){
    for (i=0; i<num; i++){
        process.stdout.write("12345^&*()_\n");
    }
}

const fs = require("fs");
let num = Number(fs.readFileSync(0).toString().trim());
printStr(num);