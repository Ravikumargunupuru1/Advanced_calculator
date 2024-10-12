import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ravi's Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.result_var = tk.StringVar()

        # Create the display frame
        self.create_display()

        # Create the buttons frame
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, height=150, bg="lightgray")
        display_frame.pack(expand=True, fill="both")

        display_label = tk.Label(
            display_frame, textvariable=self.result_var,
            anchor="e", bg="lightgray", fg="black",
            padx=24, font=("Arial", 30)
        )
        display_label.pack(expand=True, fill="both")
        
        self.result_var.set("0")  # Set default value

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="white")
        button_frame.pack(expand=True, fill="both")

        # Define button labels and grid structure
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '.', '+'),
            ('=',)
        ]

        # Grid configuration for buttons
        for row, button_row in enumerate(buttons):
            for col, button_text in enumerate(button_row):
                if button_text == '=':
                    button = tk.Button(button_frame, text=button_text, font=("Arial", 24),
                                       bg="green", fg="white", height=2, width=4,
                                       command=self.evaluate)
                elif button_text == 'C':
                    button = tk.Button(button_frame, text=button_text, font=("Arial", 24),
                                       bg="red", fg="white", height=2, width=4,
                                       command=self.clear)
                else:
                    button = tk.Button(button_frame, text=button_text, font=("Arial", 24),
                                       bg="white", fg="black", height=2, width=4,
                                       command=lambda x=button_text: self.on_button_click(x))
                button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Make sure buttons stretch to fill the frame
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        current_text = self.result_var.get()

        if current_text == "0" or "Syntax Error" in current_text:
            self.result_var.set(char)
        else:
            self.result_var.set(current_text + char)

    def evaluate(self):
        try:
            expression = self.result_var.get()
            result = str(eval(expression))
            self.result_var.set(result)
        except (SyntaxError, ZeroDivisionError):
            self.result_var.set("Syntax Error")

    def clear(self):
        self.result_var.set("0")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()