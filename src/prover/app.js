//main app / service
//app.js
const http = require("http");
const fs = require('fs');
const path = require('path');
const controller = require("./controller");

const { getReqData } = require("./utils");

//const PORT = process.env.PORT || 5000;
// Constants
const PORT = 8000;
const HOST = "172.22.0.10";

const server = http.createServer(async (req, res) => {
    console.log("Called" + req.method + " : " + req.url);

    if (req.url === "/" && req.method === "GET") {
        // set the status code, and content-type
        res.writeHead(200, { "Content-Type": "application/json" });
        // send the data
        res.end("Welcome, this is your Home page\n");
    }

    //Health check and uptime endpoint
    else if (req.url === "/health" && req.method === "GET") {
        // console.log("Called GET : 0.0.0.0:8080/health");
        const healthcheck = {
            uptime: process.uptime(),
            message: "OK",
            timestamp: Date.now(),
        };
        res.end(JSON.stringify(healthcheck));
    }



    else if (
        req.url.match(/\/api\/file\/([a-z]+)/) &&
        req.method === "POST"
    ) {
        try {
            // splits the url to seperate the  filename
            const name = req.url.split("/")[3];
            let data = await getReqData(req);
            var buf = Buffer.from(data, 'base64'); 
            let file = await new controller().saveFile(name,buf );
           
            res.writeHead(201, { "Content-Type": "application/json" }); //was 200
           
            res.end(file);
         
        } catch (error) {
            // set the status code and content type
            res.writeHead(404, { "Content-Type": "application/json" });
            // send the error
            res.end(JSON.stringify({ message: error }));
        }
    }





    // No route present
    else {
        console.log(
            "This endpoint is not implemented / unavailable at the moment !!"
        );
        res.writeHead(404, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ message: "Route not found" }));
    }
});

server.listen(PORT, () => {
     console.log(`server started on ${HOST}  port: ${PORT}`);
//     console.log(`server started on port: ${PORT}`);
});
