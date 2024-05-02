const fs = require('fs');
const path = require('path');

function imageToBase64(imagePath) {
    const imageData = fs.readFileSync(imagePath);
    const base64Image = imageData.toString('base64');
    return base64Image;
}

if (require.main === module) {
    const imagePath = 'bc3.jpg'; 
    const base64String = imageToBase64(imagePath);

    const jsonData = JSON.stringify({ image: base64String });

    console.log(jsonData);
}
