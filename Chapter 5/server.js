import express from 'express';

const app = express();

// Set static folder
app.use(express.static('public'));

// Parse URL-encoded bodies (as sent by HTML forms)
app.use(express.urlencoded({ extended: true }));

// Parse JSON bodies (as sent by API clients)
app.use(express.json());

// Handle POST request for email validation
app.post('/email', (req, res) => {
    const submittedEmail = req.body.email;
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (emailRegex.test(submittedEmail)) {
        return res.send(
            `…`
        )
    }
    else {
        return res.send(
            `…`
        )
    }
});
// Start the server
app.listen(3000, () => {
    console.log('Server listening on port 3000');
});