import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 邮箱列表
email_list = [
    "haicongqiao@tencent.com",
    "Mike.YU@cn.bosch.com"
    # ...直到300个邮箱地址
]

# SMTP服务器配置
smtp_server = "172.20.0.24"
smtp_port = 25
sender_email = "xc-wave3@mailing.bosch.com"

# 邮件正文模板
html_template = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type='text/css'>
        p {
            line-height: 25px;
        }
        span {
            font-size:16px;
            font-weight:bold;
        }
    </style>
</head>

<body>
    <div class="container">
        <p style="margin-bottom: 25px;">Dear customer</p>
		<p> 最近由于Bitbucket License限制，我们将对六个月以上未登录的用户回收license,如果需要保留license的话请在9月19日前联系 <span>@XC CN PMT ADC Infrastructure Operations Team BD</span> 
或者邮件至 <span>@ XC CN PMT ADC Infrastructure Operations Team BD</span> 并CC  <span>Gemini.CHEN@cn.bosch.com</span> </p>
		<p> Due to Bitbucket licensing restrictions, we will be revoking licenses for users who have not logged in for more than six months. If you would like to retain your license, please contact <span>@XC CN PMT ADC Infrastructure Operations Team BD</span> before September 19th. Or, email <span>@XC CN PMT ADC Infrastructure Operations Team BD</span> and CC <span>@Gemini.CHEN@cn.bosch.com</span> </p>
		
		</div>
</body>
</html>
"""

# 循环发送邮件给每个邮箱
for recipient_email in email_list:
    try:
        # 创建邮件对象
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Bitbucket License Revoking"
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["CC"] = "xiangyinghu@tenent.com"

        # 构造HTML邮件内容
        html_content = MIMEText(html_template, "html")
        msg.attach(html_content)

        # 使用SMTP发送邮件
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # 如果服务器不需要认证（提供直接发送邮件支持），无需调用 login()
            server.sendmail(sender_email, recipient_email, msg.as_string())

        print(f"邮件发送成功: {recipient_email}")

    except Exception as e:
        print(f"邮件发送失败: {recipient_email}, 错误: {e}")