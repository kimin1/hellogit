# -> 경로 정보를 취득하기 위한 모듈
import os.path
# -> 발송서버와 연동하기 위한 모듈
from smtplib import SMTP
# -> 본문 구성 기능
from email.mime.text import MIMEText
# -> 파일을 Multipart 형식으로 변환
from email.mime.application import MIMEApplication
# -> 파일을 본문에 추가하는 기능 제공
from email.mime.multipart import MIMEMultipart

# 파이썬 메일 발송 함수
def send_mail(from_addr, to_addr, subject, content, files=[]):
    content_type = "html"             # 컨텐츠 형식 (text or html)
    username = 'k7132474@gmail.com'   # 구글 메일 주소
    password = 'krav qsuj oseh vgqz'        # 구글 비밀번호
    smtp = 'smtp.gmail.com'           # 구글 발송 서버 주소 (고정값)
    port = 587                        # 구글 발송 서버 포트 (고정값)
    
    # 메일 발송 정보를 저장하기 위한 객체
    msg = MIMEMultipart()

    msg['Subject'] = subject     # 메일 제목
    msg['From'] = from_addr     # 보내는 사람
    msg['To'] = to_addr     # 받는사람

    # 본문 설정 -> 메일의 내용과 형식 지정
    msg.attach(MIMEText(content, content_type))
    
    # 리스트 변수의 원소가 하나라도 존재할 경우 True
    if files:
        for f in files:
            with open(f, 'rb') as a_file:
                basename = os.path.basename(f)
                part = MIMEApplication(a_file.read(), Name=basename)
                part['Content-Disposition'] = 'attaxhment; filename="%s"' % basename
                msg.attach(part)
                
    mail = SMTP(smtp)
# 메일 서버 접속
    mail.ehlo()
# 메일 서버 연동 설정
    mail.starttls()

    mail.login(username, password)

    mail.sendmail(from_addr, to_addr, msg.as_string())
