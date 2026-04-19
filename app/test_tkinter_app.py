
# Tkinter app - simple window with a close button
import tkinter as tk

class TestApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test App")
        self.geometry("300x200")

        # Create a close button
        close_button = tk.Button(self, text="Close", command=self.close_app)
        close_button.pack(pady=20)

    def close_app(self):
        self.destroy()
        
if __name__ == "__main__":
    app = TestApp()
    app.mainloop()
    