import requests
import pretty_errors
import unittest
from unittest.mock import patch, Mock


def get_user_data(user_id):
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()


class TestUserData(unittest.TestCase):
    
    @patch('requests.get')
    def test_get_user_data(self,mock_get):
        mock_response = Mock()
        response_dict = {'name': 'John', 'email': 'john@sample.com'}
        mock_response.json.return_value = response_dict
        
        mock_get.return_value = mock_response
        
        user_data = get_user_data(1)
        mock_get.assert_called_with("https://api.example.com/users/1")
        self.assertEqual(user_data, response_dict)
        
        
if __name__ == '__main__':
    unittest.main()      

# -----

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import unittest
# from unittest.mock import patch, ANY


# def send_email(smtp_server, smtp_port, from_addr, to_addr, subject, body):
#     msg = MIMEMultipart()
#     msg['From'] = from_addr
#     msg['To'] = to_addr
#     msg['Subject'] = subject
#     msg.attach(MIMEText(body, 'plain'))
    
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()
#     server.login(from_addr, "MyPassword")
#     text = msg.as_string()
#     server.sendmail(from_addr, to_addr, text)
#     server.quit()
    
    
# class TestMail(unittest.TestCase):
    
#     @patch('smtplib.SMTP')
#     def test_end_mail(self, mock_smtp):
#         instance = mock_smtp.return_value
        
#         send_email("smtp.examle.com", 587, "mymail@example.com", "theymail@example.com", "Subject", "Mail Content")
        
#         mock_smtp.assert_called_with("smtp.examle.com", 587)
        
#         instance.starttls.assert_called_with()
#         instance.login.assert_called_with("mymail@example.com", "MyPassword")
#         instance.sendmail.assert_called_with("mymail@example.com", "theymail@example.com", ANY)
#         instance.quit.assert_called_with()
        
# if __name__ == '__main__':
#     unittest.main()