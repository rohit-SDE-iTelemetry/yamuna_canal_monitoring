import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

sender_email = "etest0454@gmail.com"
receiver_email = ['rajat.goyal@i-telemetry.com','etest0454@gmail.com']
password = 'nlnzaecjswoixons'

message = MIMEMultipart("alternative")
message["Subject"] = "Alert: Yamuna Canal Monitoring Gate: %s" % (datetime.today().date())
message["From"] = sender_email
message["CC"] = None
message["BCC"] = None
for i in receiver_email:
    message["o"] = i

html = """\
<html>
<head>

  <meta charset="utf-8">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title>TelePro Delay Offline Report</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style type="text/css">
  @media screen {
    @font-face {
      font-family: 'Source Sans Pro';
      font-style: normal;
      font-weight: 400;
      src: local('Source Sans Pro Regular'), local('SourceSansPro-Regular'), url(https://fonts.gstatic.com/s/sourcesanspro/v10/ODelI1aHBYDBqgeIAH2zlBM0YzuT7MdOe03otPbuUS0.woff) format('woff');
    }
    @font-face {
      font-family: 'Source Sans Pro';
      font-style: normal;
      font-weight: 700;
      src: local('Source Sans Pro Bold'), local('SourceSansPro-Bold'), url(https://fonts.gstatic.com/s/sourcesanspro/v10/toadOcfmlt9b38dHJxOBGFkQc6VGVFSmCnC_l7QZG60.woff) format('woff');
    }
  }
  body,
  table,
  td,
  a {
    -ms-text-size-adjust: 100%; /* 1 */
    -webkit-text-size-adjust: 100%; /* 2 */
  }

  /**
   * Remove extra space added to tables and cells in Outlook.
   */
  table,
  td {
    mso-table-rspace: 0pt;
    mso-table-lspace: 0pt;
  }

  /**
   * Better fluid images in Internet Explorer.
   */
  img {
    -ms-interpolation-mode: bicubic;
  }

  /**
   * Remove blue links for iOS devices.
   */
  a[x-apple-data-detectors] {
    font-family: inherit !important;
    font-size: inherit !important;
    font-weight: inherit !important;
    line-height: inherit !important;
    color: inherit !important;
    text-decoration: none !important;
  }

  /**
   * Fix centering issues in Android 4.4.
   */
  div[style*="margin: 16px 0;"] {
    margin: 0 !important;
  }

  body {
    width: 100% !important;
    height: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }

  a {
    color: #1a82e2;
  }

  img {
    height: auto;
    line-height: 100%;
    text-decoration: none;
    border: 0;
    outline: none;
  }
  </style>

</head>
<body style="background-color:white;">
<br>
<img src="https://public-images-docs.s3.ap-south-1.amazonaws.com/aaxis_logo_new.png" alt="Aaxis Nano Technologies Pvt. Ltd." style="margin-left:1%;" height="100px;" width="150px;">
<div class="container-fluid" style="background-color: #e9ecef;width:1000px; margin-left:1%;margin-right:20%;">
    <div style="background-color:#017A75; height:60px; width:100%;">
        <h2 style="color:white; padding:15px 5px 5px 15px;">Alert</h2>
    </div>
    <div style="padding:10px 5px 15px 20px;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%">
            <tr>
                <td style="padding: 10px 0 30px 0;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" width="800" style="border: 1px solid #cccccc; border-collapse: collapse;">

                        <tr>
                            <td>
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td style="font-family: Arial, sans-serif; font-size: 18px;">
                                            <center><strong> Yamuna Canal Monitoring</strong></center>
                                            <br>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>

                        <tr>
                            <td style="font-family: Arial, sans-serif; font-size: 20px;">
                                <table border="1" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <th bgcolor="#017A75" style="color:white;">
                                            Station
                                        </th>
                                        <th bgcolor="#017A75" style="color:white;">
                                            Status
                                        </th>
                                        <th bgcolor="#017A75" style="color:white;">
                                            Last Data Received ON
                                        </th>
                                    </tr>

                                    <tr>
                                        <td>
                                            <a href="https://tpro.telsys.in/dashboard/">Gate 1</a>
                                        </td>
                                        <td>
                                            Open
                                        </td>
                                        <td>
                                            26-09-2022 11:00:00
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <a href="https://tpro.telsys.in/dashboard/">Gate 2</a>
                                        </td>
                                        <td>
                                            Close
                                        </td>
                                        <td>
                                            26-09-2022 11:00:00
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <a href="https://tpro.telsys.in/dashboard/">Gate 3</a>
                                        </td>
                                        <td>
                                            Close
                                        </td>
                                        <td>
                                            26-09-2022 11:15:00
                                        </td>
                                    </tr>

                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td>&nbsp;</td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </div>
    <br>
    <small style="float:right; padding:10px;color:white;">
        <sup>Powered By:</sup>
        <br>
        <a href="http://i-telemetry.com/" style="color:white;">iTelemetry Technologies Pvt. Ltd</a>
    </small>
    <div style="background-color:#017A75;color:white;">
        <small>
            This is an automatically generated email, please do not reply.
            <br>
            Thanks & Regards:
        </small>
        <br>
        <a href="https://aaxisnano.com/" style="color:white;">Aaxis Nano Technologies Pvt. Ltd</a>
    </div>

</div>
</body>
</html>

"""

part2 = MIMEText(html, "html")
message.attach(part2)

def gate_alert():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


if __name__ == '__main__':
    try:
        gate_alert()
        print('Gate Alert mail sent succesfully')
    except Exception as er:
        print(er)