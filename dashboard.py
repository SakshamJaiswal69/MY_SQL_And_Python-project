from tkinter import*
from PIL import Image,ImageTk #pip install pillow
class RMS:
    def __init__(self,root):
        self.root=root
         # THIS FUNC IS USED FOR THE HEADER AND WINDOW PROGRAM
        self.root.title(" COLLEGE RESULT MANAGEMENT SYSTEM") #THIS IS HEADER FILE
        self.root.geometry("1350x700+0+0")#THIS IS ITS ALIGNMENT        
        self.root.config(bg="light yellow")#FOR COLOUR
        #-->this is for icons
        self.logo_dash=ImageTk.PhotoImage(file="images/download.png")
        #-->this is for title
        title=Label(self.root,text="COLLEGE RESULT MANAGEMENT SYSTEM",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#FFF000",fg="black").place(x=0,y=0,relwidth=1,height=75)
        #-->this is for menu and its frame plus buttons
        M_Frame=LabelFrame(self.root,text="MENU",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="COURSE",font=("goudy old style",15,"bold"),cursor="hand2",bg="#FF0000",fg="black").place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="STUDENT",font=("goudy old style",15,"bold"),cursor="hand2",bg="#FF0000",fg="black").place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="RESULT",font=("goudy old style",15,"bold"),cursor="hand2",bg="#FF0000",fg="black").place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="VIEW STUDENT\nRESULT",font=("goudy old style",14,"bold"),cursor="hand2",bg="#FF0000",fg="black").place(x=680,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="EXIT",font=("goudy old style",15,"bold"),cursor="hand2",bg="#FF0000",fg="black").place(x=900,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="LOGOUT",font=("goudy old style",15,"bold"),cursor="hand2",bg="#FF0000",fg="black").place(x=1120,y=5,width=200,height=40)
        #-->this is for BACKGROUNG image uploader and fiter also enhancer
        self.bg_img=Image.open("images/na.jpg") 
        self.bg_img=self.bg_img.resize((920,350),Image.LANCZOS) 
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #-->this is for footer or bottom details
        footer=Label(self.root,text="SAKSHAM JAISWAL\nCOLLEGE RESULT MANAGEMENT SYSTEM\nContact Us for any Technical Issue:983801XXXX ",font=("goudy old style",12,"bold"),bg="#228B22",fg="BLACK").pack(side=BOTTOM,fill=X)
        # #-->this is for the total number of courses, students, and results
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",22),bd=10,relief=RIDGE,bg="#FFA500",fg="BLACK").place(x=400,y=530,width=300,height=100)

        self.lbl_Student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",22),bd=10,relief=RIDGE,bg="#FFEA00",fg="BLACK").place(x=710,y=530,width=300,height=100)

        self.lbl_Result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old style",22),bd=10,relief=RIDGE,bg="#FF0000",fg="BLACK").place(x=1020,y=530,width=300,height=100)
        #-->this is for class and object attributes instances 
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()