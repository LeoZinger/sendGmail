import smtplib


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

#Example Usage of above script

#sendemail(from_addr='python@RC.net',
#          to_addr_list=['RC@gmail.com'],
#          cc_addr_list=['RC@xx.co.uk'],
#          subject='Howdy',
#          message='Howdy from a python function',
#          login='pythonuser',
#          password='XXXXX')

sendemail(from_addr    = 'python@RC.net',
          to_addr_list = ['leo.zinger@gmail.com'],
          cc_addr_list = ['leo.zinger@yahoo.com'],
          subject      = 'Howdy',
          message      = 'Howdy from a python sentGmail function',
          login        = 'leo.zinger@gmail.com',
          password     = 'password')