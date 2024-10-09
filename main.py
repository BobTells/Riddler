import tkinter as tk

class ScavengerHuntGame:
    def __init__(self, root):
        # Initialize the window and widgets
        self.root = root
        self.root.title("Scavenger Hunt")
        
        # Centering the window and setting size
        window_width, window_height = 500, 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = int((screen_width / 2) - (window_width / 2))
        y_position = int((screen_height / 2) - (window_height / 2))
        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        
        # Set focus on the window
        root.focus_force()

        # List of riddles and answers
        self.riddles = [
            ("Riddle 1: I’m a place where you sit and write, but I’m hiding something out of sight. "
             "Look underneath, don’t delay, you’ll find a letter card to lead the way.", "t"),
            ("Riddle 2: The letter you found is one to fear, now add ‘T’ and a ghost may appear. "
             "What’s the spooky word you get?  BA_", "bat"),
            ("Riddle 3: It’s made of wood, used in a game. Swing it fast to earn your fame. "
             "But this one’s hiding out of view, go to the closet for the next clue.", "6"),
            ("Riddle 4: The number you found is part of the lore, now add to it like never before. "
             "Four more to the total, and you’ll see, the number that haunts this mystery!", "10"),
            ("Riddle 5: You’ve cracked the code, and the number is ten, time to check the place where watches have been. "
             "A box that holds ten, not more, not less—there’s a prize inside, can you guess? "
             "Don’t be distracted by shoes nearby, the real reward is where time flies by!", "")
        ]

        # Initialize current riddle index
        self.current_riddle = 0

        # Instructions label
        self.label = tk.Label(root, wraplength=400, font=("Arial", 14))
        self.label.pack(pady=20)

        # Entry for user input
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        self.entry.focus_set()  # Set focus to the input box on start
        
        # Bind Enter key to the check_answer function
        root.bind('<Return>', self.check_answer_event)

        # Button to submit answer
        self.button = tk.Button(root, text="Submit Answer", command=self.check_answer)
        self.button.pack(pady=10)
        
        # Feedback label
        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        # Display the first riddle
        self.show_riddle()

    def show_riddle(self):
        """Display the current riddle."""
        self.label.config(text=self.riddles[self.current_riddle][0])
        self.feedback_label.config(text="")
        self.entry.delete(0, tk.END)
        
        # If it's the 5th riddle, hide the input box and button
        if self.current_riddle == len(self.riddles) - 1:
            self.hide_input()
            self.feedback_label.config(text="Congratulations! Your prize is at the next location.")

    def hide_input(self):
        """Hide the input box and button after the final riddle."""
        self.entry.pack_forget()
        self.button.pack_forget()

    def check_answer_event(self, event):
        """Handler to check the answer when the Enter key is pressed."""
        self.check_answer()

    def check_answer(self):
        """Check the user's answer against the current riddle's answer."""
        answer = self.entry.get().strip().lower()

        # Check if the answer is correct for the current riddle
        correct_answer = self.riddles[self.current_riddle][1]
        if answer == correct_answer:
            self.feedback_label.config(text="Correct!")
            self.current_riddle += 1  # Move to the next riddle
            self.show_riddle()
        else:
            self.feedback_label.config(text="Oops! That’s not correct. Try again.")

# Create the main window
root = tk.Tk()
game = ScavengerHuntGame(root)
root.mainloop()
