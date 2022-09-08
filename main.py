from tkinter import *
from tkinter import messagebox 
import customtkinter
from PIL import ImageTk, Image
from news import News
import re

root = customtkinter.CTk()

root.title('News Sender')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root.iconbitmap('/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/Monopoly/favicon.ico')
root.geometry("1000x500")
root.configure(bg='black')

#Bot.message_bot()

news = News()

def send_msg():
    news.news_amount = int(combobox2.get())
    news.search_for = news_search_for_entry.get()
    news.receiver = news_receiver_entry.get()
    news.language = combobox.get()
    
    nums = []
    with open('/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/News/requests.txt', 'r') as f:
        for line in f.readlines():
            nums.append(int(line))
        if nums[0] == news.month:
            with open('/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/News/requests.txt', 'w') as f:
                f.write(str(news.month))  
                f.write("\n")
                f.write(str(nums[1]-1)) 
                print(f"Requests left this month: {nums[1]-1}")
        else:
            with open('/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/News/requests.txt', 'w') as f:
                f.write(str(news.month))  
                f.write("\n")
                f.write(str(100)) 
                print("Requests left this month: 100") 
                
    
    valid_mail = solve(news.receiver)
    if valid_mail:
        news.send_news()
    else:
        messagebox.showerror('Error: Failed to send news', 'Please enter a valid e-mail!')

def solve(s):
   pat = r"[^@]+@[^@]+\.[^@]+"
   if re.match(pat,s):
      return True
   return False    

news_frame = customtkinter.CTkFrame(master=root,
                               width=1000,
                               height=500,
                               corner_radius=10,
                               bg='black',
                               fg_color='#FEB139',
                               border_width=2, border_color="white")

news_receiver = customtkinter.CTkLabel(root, text="Receiver:", width=130,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#FEB139')

news_times = customtkinter.CTkLabel(root, text="How many articles:", width=130,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#FEB139')

news_search_for = customtkinter.CTkLabel(root, text=f"Search for:", width=140,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#FEB139')

news_receiver_entry = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#0F3D3E',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#FEB139',
                               border_width=2, border_color="white"
                            )


news_language = customtkinter.CTkLabel(root, text=f"Language:", width=140,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#FEB139')

news_receiver_entry = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#0F3D3E',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#FEB139',
                               border_width=2, border_color="white"
                            )

news_amount_entry = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#0F3D3E',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#FEB139',
                            )

news_search_for_entry = customtkinter.CTkEntry(root, width=130,
                               height=40,
                               corner_radius=10,
                            fg_color='#0F3D3E',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#FEB139',
                               border_width=2, border_color="white"
                            )

whatsapp_button = customtkinter.CTkButton(root, command=send_msg, width=195,
                                 height=40,
                                 corner_radius=8,
                                 text="Search News",
                                 fg_color='#0F3D3E',
                                 text_font=('Times New Roman', 20),
                               bg_color='#FEB139',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white"
                                 )


combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=["en", "de", "ru"], 
                                       width=80,
                                        height=40,
                                        fg_color=("white", "#0F3D3E"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='#FEB139',
                                        text_color='white',
                                        
                                        button_color='#0F3D3E',
                                        button_hover_color='#3AB4F2',
                                        dropdown_text_font=('Times New Roman', 24),
                                                           
                                        )
combobox.grid(row=1, column=0, sticky='ew', padx=10, columnspan=2)
combobox.set("en")  # set initial value


combobox2 = customtkinter.CTkOptionMenu(master=root,
                                       values=[str(i+1) for i in range(20)],
                                       width=80,
                                        height=40,
                                        fg_color=("white", "#0F3D3E"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='#FEB139',
                                        text_color='white',
                                        
                                        button_color='#0F3D3E',
                                        button_hover_color='#3AB4F2',
                                        dropdown_text_font=('Times New Roman', 24),
                                                           
                                        )
combobox2.set('3')  # set initial value



#Packing them on the screen
news_frame.grid(row=0, column=0, columnspan=4, rowspan=6, sticky='news')
news_receiver.grid(row=2, column=2, sticky='ew', padx=10, columnspan=2)
news_times.grid(row=0, column=2, sticky='ew', padx=10, columnspan=2)
news_search_for.grid(row=2, column=0, sticky='ew', padx=10, columnspan=2)
news_receiver_entry.grid(row=3, column=2, padx=10, sticky='nsew', columnspan=2, rowspan=2)
combobox2.grid(row=1, column=2, sticky='ew', padx=10, columnspan=2)
news_search_for_entry.grid(row=3, column=0, padx=10, sticky='nsew', columnspan=2, rowspan=2)
news_language.grid(row=0, column=0, sticky='ew', padx=10, columnspan=2)
whatsapp_button.grid(row=5, column=0, columnspan=4, sticky='ew', padx=10)




root.mainloop()