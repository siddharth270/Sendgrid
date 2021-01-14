import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key = os.environ('api_key'))
from_email = Email("sidmehta927@gmail.com")
to_email = To("sidmehta927@gmail.com")
subject = "Hello Everyone!!!"
content = Content("Hi my name is siddharth i am 19 years old. I live in India.")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

