const express = require('express');
const app = express();

const response = { response: "🎉 Your JavaScript API is running" };

app.get('/', (req, res) => {
    res.json(response);
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});