#GUI를 위한 모듈
from tkinter import *  
from tkinter.messagebox import *    # tkinter는 모듈 밑에 있는 모듈을 from tkinter import *로 가져올 수 없음
from tkinter.scrolledtext import *
from tkinter.font import *
# 제미나이를 위한 모듈
import google.generativeai as genai

# 6. 제미나이 API용 구성
genai.configure(api_key='AIzaSyAyDxVa-BkFP2P-oM3OAWTt3fm9Yw3ytHs')  # 신청한 API키
model = genai.GenerativeModel('gemini-1.5-flash') # AI 사전훈련된 모델


# 4. 전송버튼 이벤트, 제미나이 실행 포함
def responseMessage():
    # showinfo('실행', 'API를 실행합니다!')
    inputText = textMessage.get('1.0', END).replace('\n', '').strip() # 문자열 데이터 전송
    print(inputText)
    textMessage.delete('1.0', END) # 입력창 글 지우기
    # showinfo('결과', inputText) # 다이얼로그, 모달(Modal)창

    if inputText:
        try:
            textResult.insert(END, '유저: ', BOLD)
            textResult.insert(END, f'{inputText}\n\n', 'user') # 'user' 텍스트 아규먼트

            ai_response = model.generate_content(inputText)
            response = ai_response.text # 텍스트만 가져오기
        
            textResult.insert(END, '챗봇: ', 'bold')
            textResult.insert(END, f'{response}\n\n', 'ai') # 'ai' 텍스트 아규먼트

        except Exception as e:
            textResult.insert(END, f'Error: {str(e)}\n\n', 'error')
        finally:
            textResult.see(END) # 스크롤텍스트 마지막위치로 스크롤 다운

# 8. textMessage 위젯에서 엔터를 치면 전송버튼이 클릭
def keypress(event):
    # print(repr(event.char)) # repr을 안쓰면 \r, \x80 표시안됨
    # \r(캐리지 리턴) \n(뉴라인) 혼용해서 사용 \r\n, \n, \r
    if event.char == '\r':
        responseMessage()

# 11. 종료시 이벤트처리 함수
def onClosing():
    if askyesno('종료확인', '종료하시겠습니까?'):
        root.destroy() # 완전 종료

# 1. 메인 윈도우 생성, 초기설정
root = Tk()
root.title('제미나이 챗봇')
root.geometry('730x450')

# 12. 아이콘 변경
# ./image/ 경로는 삭제
root.iconbitmap('robot.ico')    #pyinstaller때는 실행파일폴더에 icon 복사하고

# 7. 전체에서 사용할 폰트 지정 -> 나눔고딕
myFont = Font(family='NanumGothic', size=10)
boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

# 2. UI화면 구성
inputFrame = Frame(root, width=730, height=30, bg='#EFEFEF')
inputFrame.pack(side=BOTTOM, fill=BOTH)

# 3. inputFrame에 들어갈 Entry와 Button 구성
textMessage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myFont)
# 8. 입력창에서 엔터를 치면 keypress 이벤트처리함수 발생
textMessage.bind('<Key>', keypress)
textMessage.pack(side=LEFT, padx=15)

buttonSend = Button(inputFrame, text='전송', bg='green', fg='white',
                    font=myFont, command=responseMessage)
buttonSend.pack(side=RIGHT, padx=18, pady=5)

# 5. API호출 결과메시지 출력될 스크롤기능 텍스트 위젯
textResult = ScrolledText(root, wrap=WORD, bg='black', fg="white", font=myFont)
textResult.pack(fill=BOTH, expand=True)

# 10. 스크롤텍스트에 나올 메시지 디자인
textResult.tag_configure('user', font=boldFont, foreground='yellow')
textResult.tag_configure('ai', font=myFont, foreground='limegreen') 
textResult.tag_configure('error', font=boldFont, foreground='red') 

# 9. 실행 후 바로 입력창에 포커스가 가도록
textMessage.focus_set()

# 11. 종료버튼(x)를 누르면 종료 메시지 확인 후 종료
root.protocol('WM_DELETE_WINDOW', onClosing)

# 1. 종료시까지 계속 실행
root.mainloop()

