from tkinter import Tk, Label, Button, Text
from gtts import gTTS

class Main:
    def __init__(self, master):
        self.master = master
        master.title("TTS")

        self.label = Label(master, text="Coller votre texte ici!")
        self.label.pack()

        self.T = Text(root, height=2, width=30)
        self.T.pack()

        self.greet_button = Button(master, text="Save", command=self.save)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def save(self):
        tts = gTTS(text=self.T.get('1.0', 'end'), lang='fr')
        print("Network activities...")
        tts.save("MyNewAudioBook.mp3")
        print("done")

        
root = Tk()
my_gui = Main(root)
root.mainloop()