# Tkinter를 클래스화
from tkinter import *
from tkinter.messagebox import * 
from tkinter.scrolledtext import *
from tkinter.font import *
import google.generativeai as genai

genai.configure(api_key='AIzaSyAyDxVa-BkFP2P-oM3OAWTt3fm9Yw3ytHs')  # API키
model = genai.GenerativeModel('gemini-1.5-flash') 

class window(Tk): # 부모(Tk) 상속, 오버라이딩(재정의), 자동완성 부모 기본값은 지워도 됨
    def __init__(self):
        super().__init__() # 부모객체도 같이 초기화
        self.title('제미나이 챗봇 v2.0')
        self.geometry('730x450')
        self.iconbitmap('./image/robot.ico')
        # 클래스 작업할 땐 self 유심히.
        self.protocol('WM_DELETE_WINDOW', self.onClosing)

        self.initWindow() # 윈도우 화면 초기화 멤버함수(메서드)

    def initWindow(self):
        self.myFont = Font(family='NanumGothic', size=10)
        self.boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

        self.inputFrame = Frame(self, width=730, height=30, bg='#EFEFEF')
        self.inputFrame.pack(side=BOTTOM, fill=BOTH)

        self.textMessage = Text(self.inputFrame, width=75, height=1, wrap=WORD, font=self.myFont)
        # self.textMessage.bind('<Key>', keypress) 해결
        self.textMessage.bind('<Key>', self.keypress)  # 엔터키
        self.textMessage.pack(side=LEFT, padx=15)

        self.buttonSend = Button(self.inputFrame, text='전송', bg='green', fg='white',
                    font=self.myFont, command=self.responseMessage)
        self.buttonSend.pack(side=RIGHT, padx=18, pady=5)

        self.textResult = ScrolledText(self, wrap=WORD, bg='black', fg="white", font=self.myFont)
        self.textResult.pack(fill=BOTH, expand=True)

        self.textResult.tag_configure('user', font=self.boldFont, foreground='yellow')
        self.textResult.tag_configure('ai', font=self.myFont, foreground='palegreen')
        self.textResult.tag_configure('error', font=self.boldFont, foreground='red')

        self.textMessage.focus_set()

        # 나머지 부분 !!!!!!!

    def responseMessage(self): # 내용수정 !!!!!!
        # showinfo('동작', '이제 API를 호출하면 됩니다!')
        inputText = self.textMessage.get('1.0', END).replace('\n', '').strip()  # 텍스트 가져오기
        print(inputText)
        self.textMessage.delete('1.0', END)  # 입력창 비우기

        if inputText:
            try:
                # 유저
                self.textResult.insert(END, '유저: ', 'bold')
                self.textResult.insert(END, f'{inputText}\n\n', 'user')

                # API 호출
                ai_response = model.generate_content(inputText)
                response = ai_response.text  # AI 답 텍스트 추출

                # 챗봇
                self.textResult.insert(END, '챗봇: ', 'bold')
                self.textResult.insert(END, f'{response}\n\n', 'ai')

            except Exception as e:
                self.textResult.insert(END, f'Error: {str(e)}\n\n', 'error')

            finally:
                self.textResult.see(END) 

    def keypress(self, event):
        if event.char == '\r':
            self.responseMessage()

    def onClosing(self):
        if askyesno('종료확인', '종료하시겠습니까?'):
            self.destroy() # 종료


if __name__ == '__main__':
    print('Tkinter 클래스 시작!')
    app = window() # Tkinter 클래스 객체 생성
    app.mainloop()

