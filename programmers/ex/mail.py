import smtplib # SMTP
from email.message import EmailMessage # MIME
import imghdr # 이미지
import re # 정규표현식

# smtp 서버 연결 설정
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465 # gmail 지정

def sendEmail(addr):
    # 이메일 유효성 검사
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.mateh(reg, addr)): # 내용이 있으면 true, 내용이 없다면 false
        # 메일 전송
        smtp.send_message(message) # send_message(메일 내용)
        print("정상적으로 메일이 발송되었습니다.")
    else: 
        print("유효한 이메일 주소가 아닙니다.")
    

# 메일 내용 MIME 생성
message = EmailMessage() # 메시지를 이메일 형태로 만들어줌
message.set_content("메일 본문입니다.") # 본문 내용
message["Subject"] = "이것은 제목입니다." # 메일 제목
message["From"] = "juranlim0422@gmail.com" # 보내는이
message["To"] = "ijo0r98@gmail.com" # 받는이

# 이미지 파일 open
with open("image.png", "rb") as image:
    image_file = image.read() # 읽어온 이미지 파일을 변수로 담음

# 이미지 확장자
image_type = imghdr.what('image', image_file)
print(image_type) # png

# multipart/mixed 타입의 메일 (사진 첨부) - add_attachment(image, maintype, subtype(확장자))
message.add_attachment(image_file, maintype='image', subtype=image_type)

# 서버 연결
# smtplib.SMTP(SMTP_SERVER, SMTP_PORT) -> 에러; gmail SSL 처리 필수
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) # SMTP(서버주소, port)
print(smtp) # <smtplib.SMTP_SSL object at ..>

# 메일 서버 로그인
email = "juranlim0422@gmail.com"
password = "@@namo5059"
smtp.login(email, password) 

# 메일 보내는 메서드 실행
sendEmail("to@gmail.com")

# 종료
smtp.quit()