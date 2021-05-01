# 이 프로그램에서는 Slack api를 활용하여 원하는 정보를 가져오고, 알람을 날릴 수 있게 해봅니다.

# 1. 가져와야될 정보?? => cafe24에서 가져온다.
# 2. 가져온 데이터 local 저장
# 3. 데이터 가공
# 4. slack에서 데이터 전달해주는 방법 디자인


# 1. local에서 데이터 가져오기 (추후 cafe24로 변경)
import pandas as pd
from slacker import Slacker

def readSampleCSV(filename,columns=['주문번호','총 결제금액']):
    csv_test = pd.read_csv(filename)
    # print(csv_test.head(30))
    # print(csv_test.head(30).to_string())    
    print(csv_test[columns])
    return csv_test

# 2. slack bot 활용하기
def slackBotChat(msg):
    token = 'xoxb-2045361366736-2034176662033-a8ZDxq5Y8vHxz2cjEtjfPJgo'
    slack = Slacker(token)
    slack.chat.post_message("#coding", msg, as_user=True)

if __name__ =="__main__":
    readSampleCSV('sample.csv',columns=['주문번호','총 결제금액','수령인'])
    msg = "Coding Bot!"
    slackBotChat(msg)