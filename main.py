import os
import bardapi
from dotenv import load_dotenv
from bardapi import BardCookies

load_dotenv() #Load token từ file .env

token1 = os.getenv('__Secure-1PSID_TOKEN')
token2 = os.getenv('__Secure-1PSIDTS_TOKEN')

#Tạo cookie_dict từ token đã lấy được
cookie_dict = {
    "__Secure-1PSID": token1,
    "__Secure-1PSIDTS": token2,
}


#Vòng lặp "While" để thực hiện liên tục
while True:
    input_text = input("Enter a word: ") #Nhập thông tin cần tra
    if input_text == 'No': #Nếu nhập "No" thì thoát khỏi vòng lặp và kết thúc chương trình
        break
    
    bard = BardCookies(cookie_dict=cookie_dict)
    response = bard.get_answer(input_text)['content'] #Lấy nội dung ['content'] từ câu trả lời
    print(response) #In ra nội dung câu trả lời