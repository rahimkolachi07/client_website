import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd
from chatgpt import text_inp

def email_send(post_data, website):
    emails = pd.read_csv("email_list.csv")
    emails = emails["emails"]
    print(f"Total emails to send: {len(emails)}")

    for email in emails:
        print(f"Sending to: {email}")
        smtp_server = "smtp.dondominio.com"
        smtp_port = 587
        email_address = "newsletter@spreadit.es"
        email_password = "kqUFK.WXh2yIf/"

        subject = text_inp(
            f"Act as a professional email writer. Review 1000 times to improve grammatical errors .I will reward you if the subject is professional and error-free. Write a perfect subject analyzing this website post: {post_data}. Return only the subject in text format. Write in Spanish. Write an attractive subject.",
            f"Write a perfect subject for email newsletters about this post which has topic, subtopics: {post_data}. Write in Spanish."
        )

        body = text_inp(
            f"Act as a professional email writer. Review 1000 times to improve grammatical errors. I will reward you if the body is professional and error-free. Don't write the subject. mention website only one time .avoide to add [], make generale dont spacify the client name or recipient name, make is general. Make the email general and not specific to any client. Kind regards, SpreadIt.es. Write a perfect email body analyzing this website post: {post_data}. Return only the email body in text format. My website is {website}. Write in Spanish. Write an attractive body and tell users to read more by visiting my website: {website}.",
            f"Write a perfect body for email newsletters about this post which has topic, subtopics: {post_data}. Write in Spanish. Tell users to visit my website post: {website} to read more."
        )

        recipient_email = email

        # Create the email container
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # HTML body with footer
        html_body = f"""
        <html>
        <body>
            <p>{body}</p>
            <br>
            <p>Visita nuestra página web <a href="{website}">www.spreadit.es</a></p>
            <p>Este email ha sido enviado desde una cuenta oficial de Spread It para ponerse en contacto con usted, si ha habido algún error, no dude en ponerse en contacto con nosotros.</p>
            <img src="cid:image1" alt="Spread It Logo">
            <p>También puedes consultar nuestra <a href="{website}/privacy">Política de privacidad</a>.</p>
            <p>Copyright © 2024 SpreadIt, All rights reserved.</p>
        </body>
        </html>
        """

        # Attach the HTML body with the msg instance
        msg.attach(MIMEText(html_body, 'html'))

        # Attach the image
        with open("foot.png", 'rb') as img:
            mime_image = MIMEImage(img.read())
            mime_image.add_header('Content-ID', '<image1>')
            msg.attach(mime_image)

        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Use TLS

        # Login to the email account
        server.login(email_address, email_password)

        # Send the email
        server.sendmail(email_address, recipient_email, msg.as_string())
        server.quit()  # Close the connection

        print(f"Email sent successfully to {recipient_email}!")


