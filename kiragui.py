import sys
import tkinter as tk
from tkinter import ttk
import threading
import subprocess
from datetime import datetime


class OutputText(tk.Text):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.stdout = sys.stdout

    def write(self, message):
        self.insert(tk.END, message)
        self.see(tk.END)
        self.stdout.write(message)

    def flush(self):
        self.stdout.flush()

    def clear(self):
        self.delete("1.0", tk.END)

class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kira GUI")
        self.window.geometry("1920x1080")
        self.center_x = 100  # X-coordinate of the sphere center
        self.center_y = 100  # Y-coordinate of the sphere center
        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self.window, bg="black")
        main_frame.pack(fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(main_frame, bg="black")
        left_frame.pack(side=tk.LEFT, padx=80, pady=80)

        sphere_frame = tk.Frame(left_frame, bg="black")
        sphere_frame.pack()

        radius = 100
        center_x = 100
        center_y = 100

        self.canvas = tk.Canvas(sphere_frame, width=200, height=200, bg="black", highlightthickness=0)
        self.canvas.pack()
        self.sphere = self.canvas.create_oval(
            center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="#00FFFF", width=2
        )

        self.animate_sphere()

        kira_label = self.canvas.create_text(
            center_x, center_y, text="Kira", font=("Arial", 30, "bold"), fill="#00FFFF"
        )

        button_frame = tk.Frame(left_frame, bg="black")
        button_frame.pack(pady=100)

        style = ttk.Style()
        style.configure(
            "Neon.TButton",
            foreground="black",
            background="#008080",
            font=("Arial", 14, "bold"),
            highlightthickness=1,
            highlightbackground="#00FFFF",
            highlightcolor="#00FFFF",
            relief=tk.SOLID,
            borderwidth=10,
            padx=10,
            radius=10,
            pady=5,
        )
        style.map("Neon.TButton", foreground=[("active", "#00FFFF")], background=[("active", "#008080")])

        start_button = ttk.Button(button_frame, text="Start", command=self.start_chatbot, style="Neon.TButton")
        start_button.pack(side=tk.LEFT, padx=60)

        exit_button = ttk.Button(button_frame, text="Exit", command=self.window.destroy, style="Neon.TButton")
        exit_button.pack(side=tk.LEFT, padx=60)

        terminal_frame = tk.Frame(main_frame, bg="black", bd=10)
        terminal_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        terminal_label = tk.Label(terminal_frame, text="Output Terminal", font=("Arial", 26), fg="#00FFFF", bg="black")
        terminal_label.pack(pady=10)
        self.output_text = OutputText(
            terminal_frame,
            bg="black",
            fg="#00FFFF",
            font=("Courier New", 18),
            relief=tk.SOLID,
            borderwidth=2,
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=0, pady=10)

        scrollbar = tk.Scrollbar(self.output_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the scrollbar colors
        scrollbar.config(troughcolor="black", bg="black", highlightbackground="black", activebackground="black")

        # Configure the scrollbar width and thickness
        scrollbar.config(width=0, bd=0, relief=tk.SOLID)

        # Link the scrollbar to the output_text widget
        self.output_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.output_text.yview)

        # Add current time on the bottom left with neon color
        time_frame = tk.Frame(left_frame, bg="black", highlightthickness=1, highlightbackground="#00FFFF")
        time_frame.pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=10)

        time_label = tk.Label(
            time_frame,
            text="",
            font=("courier new", 40, "bold"),
            fg="#00FFFF",
            bg="black",
            padx=55,
            pady=10,
            highlightthickness=1,
            highlightbackground="#00FFFF",
        )
        time_label.pack(side=tk.LEFT, anchor=tk.CENTER)

        def update_time():
            current_time = datetime.now().strftime("%I:%M:%S %p")
            time_label.config(text=current_time)
            time_label.after(1000, update_time)

        update_time()

    def start_chatbot(self):
        sys.stdout = self.output_text
        threading.Thread(target=self.run_main_program).start()

    def run_main_program(self):
        main_program_file = "main.py"
        process = subprocess.Popen(["python", main_program_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            output = process.stdout.readline().decode("utf-8")
            sys.stdout.flush()  # Add this line to flush the output
            if output == "" and process.poll() is not None:
                break
            if output:
                self.output_text.write(output)

    def animate_sphere(self):
        # Define the properties of the waves
        wave_color = "#03A9F4"  # Blue color for waves
        wave_radius = 100  # Vibration radius
        wave_speed = 50  # Speed of beat animation (increase for slower animation)
        min_radius = 80  # Minimum radius for beat animation
        max_radius = 120  # Maximum radius for beat animation
        delta_radius = 10  # Change in radius for each beat animation step
        current_radius = min_radius  # Initial radius for beat animation
        increasing = True  # Flag to indicate if the sphere is currently increasing or decreasing in size

        def update_waves():
            nonlocal current_radius, increasing

            # Update the size of the sphere
            self.canvas.coords(
                self.sphere,
                self.center_x - current_radius,
                self.center_y - current_radius,
                self.center_x + current_radius,
                self.center_y + current_radius,
            )

            # Adjust the size for the next step of the beat animation
            if increasing:
                current_radius += delta_radius
                if current_radius > max_radius:
                    current_radius = max_radius
                    increasing = False
            else:
                current_radius -= delta_radius
                if current_radius < min_radius:
                    current_radius = min_radius
                    increasing = True

            # Repeat the update at regular intervals
            self.window.after(wave_speed, update_waves)

        # Start updating the waves
        update_waves()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    chatbot_gui = ChatbotGUI()
    chatbot_gui.run()
