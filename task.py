import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import *
from PIL import Image, ImageTk

# Function to handle button click
def submit_url():
    global url_value
    url_value = url_entry.get()  # Retrieve the value from the entry widget
    print(f"Entered URL: {url_value}")
    scan_url(url_value) 

def scan_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    # Open the output file in write mode (overwrites if exists, creates if not)
    with open("output.txt", "w") as file:
        for link in soup.find_all("a"):
            href = link.get("href")
            file.write(f"Link: {href}\n")
        print("~~~~~~Contents Writen in File successfully~~~~~")

root = Tk()
root.title("Web Crawler")
root.geometry("1100x650")
# Load and resize the image
image_path = 'G:\cyber_project\Green_kali.png'  # Replace with your image file path
image = Image.open(image_path)
image = image.resize((1500, 1000), Image.LANCZOS)
img = ImageTk.PhotoImage(image)
# Create a Canvas widget
canvas = Canvas(root, width=1100, height=650)
canvas.pack(fill="both", expand=True) 
canvas.create_image(0, 0, anchor="nw", image=img)
frame_width = 500
frame_height = 200
x_position = (1100 - frame_width) // 2
y_position = 10 
frame = Frame(root, bg='#000000', bd=5)
frame.place(x=x_position, y=y_position, width=frame_width, height=frame_height)  # Position and size of the frame
# Create an Entry widget for URL input
url_entry = Entry(frame, width=40, bg='#333333', fg='#00FF00', bd=2, relief=SUNKEN, font=("Helvetica", 16))
url_entry.pack(pady=20)
# Create a Button widget
submit_button = Button(frame, text="ENTER", command=submit_url, bg='#555555', fg='#ffffff', bd=2, relief=RAISED)
submit_button.pack(pady=10)
url_value = ""
root.mainloop()

