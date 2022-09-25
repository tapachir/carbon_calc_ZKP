// controller.js
// Logic behind the functionalities

const fs = require("fs");
class Controller {

    async getFile(name) {
        return new Promise((resolve, reject) => {
            const file = fs.readFileSync(name,'utf8')

            if (file) {
                resolve(file);
            } else {
                reject(`file  with name ${name} not found `);
            }
        });
    }
     async saveFile(name,data) {
        return new Promise((resolve, _) => {

            const file = fs.writeFileSync(name, data);
            console.log(name)

            if (file) {
                resolve(file);
            } else {
                // return an error
                reject(`file  with name ${name} not saved `);
            }
        });
    }
   
}
module.exports = Controller;
