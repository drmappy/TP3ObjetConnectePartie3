import tkinter as tk

root = tk.Tk()
root.title("Tp3 partie 3")
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

top_frame = tk.Frame(frame)
top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

textInputButton = tk.Button(top_frame, text="Texte à faire défiler sur les segments :")
textBox = tk.Entry(top_frame, width=30)

textInputButton.pack(side=tk.LEFT)
textBox.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=(10,0))

bottom_frame = tk.Frame(frame)
bottom_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=(0,5))

redButton = tk.Button(bottom_frame, text="Servo tourne de -45 degres", bg="red")
blueButton = tk.Button(bottom_frame, text="Servo tourne de +45 degres", bg="blue")

blueButton.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0,30))
redButton.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(30,0))

root.mainloop()