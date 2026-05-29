const express = require('express');
const fs = require('fs');
const path = require('path');
const urllib = require('url');

const app = express();

app.use((req, res, next) => {
    if (req.url.includes('image?url') || req.url.includes('image%3Furl')) {
        const nextDir = path.join(__dirname, '_next');
        let files;
        try {
            files = fs.readdirSync(nextDir);
        } catch(e) {
            return next();
        }
        
        let urlToParse = req.url.replace(/%3F/g, '?').replace(/&amp;/g, '&');
        const parsedUrl = urllib.parse(urlToParse, true);
        const incomingUrl = parsedUrl.query.url;
        const incomingW = parsedUrl.query.w;
        const incomingQ = parsedUrl.query.q;
        
        if (incomingUrl) {
            for (const file of files) {
                if (file.startsWith('image?')) {
                    const fileQs = file.substring(6);
                    const parsedFile = urllib.parse('?' + fileQs, true);
                    
                    try {
                        const fileUrlDecoded = decodeURIComponent(parsedFile.query.url || '');
                        const incomingUrlDecoded = decodeURIComponent(incomingUrl || '');
                        
                        if (fileUrlDecoded === incomingUrlDecoded && parsedFile.query.w === incomingW && parsedFile.query.q === incomingQ) {
                            return res.sendFile(path.join(nextDir, file));
                        }
                    } catch (e) {}
                }
            }
        }
    }
    
    if (req.url.startsWith('/icon?size=')) {
        const rootDir = __dirname;
        let files;
        try { files = fs.readdirSync(rootDir); } catch(e) {}
        
        let urlToParse = req.url.replace(/&amp;/g, '&');
        const parsedUrl = urllib.parse(urlToParse, true);
        const size = parsedUrl.query.size;
        
        if (size) {
            for (const file of files) {
                if (file === `icon?size=${size}`) {
                    return res.sendFile(path.join(rootDir, file));
                }
            }
        }
    }

    next();
});

app.use(express.static(__dirname, { extensions: ['html'] }));

const port = process.env.PORT || 3000;
app.listen(port, "0.0.0.0", () => {
    console.log(`Listening on port ${port}`);
});
