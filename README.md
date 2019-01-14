# Mailgun Email Proxy

This server is used as a proxy for the IGTP Contractors landing page. This proxy handles the automation of sending emails from the IGTP Contractors landing page to the company's email.

## Parameters

```json
{
    "from": "Customer email",
    "subject": "Subject of the E-Mail",
    "text": "Body of the E-Mail"
}
```

Send a `POST` request to `https://mailgun-email-proxy.herokuapp.com/send-email` with the above parameters. 

## Variable explanations

The following are explanations of variables used in this proxy:

- `BASE_URL` - The base url for Mailgun server

- `DOMAIN` - The domain url for my Mailgun server

- `API_KEY` - Mailgun api key

- `TO_EMAIL` - IGTP Contractors contact email

- `MAILGUN_URL` - Url for sending emails. Consists of `BASE_URL` and `DOMAIN`

- `FROM_EMAIL` - The email of the customer, coming from client side

- `SUBJECT` - Subject of the email, coming from client side

- `MESSAGE` - Body of the email, coming from client side

- `DATA` - Dictionary containing all information needed by Mailgun to send email