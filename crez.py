import csv
import tkinter as tk
import random

window = tk.Tk()
window.geometry('600x500')
window.title("Creative respone")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="Information on Slaves During 1600's-1950's")
title_label.config(font=("Lobster", 34))
title_label.pack(padx=10, pady=10)

filename = 'toc.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    authors, titles, urls = [], [], []

    for row in reader:
        author = str(row[1])
        title = str(row[2])
        url = str(row[4])

        authors.append(author)
        titles.append(title)
        urls.append(url)

label_names = tk.Label(window, text=f'{random.choice(titles)}')
label_names.config(font=('Arial', 11))
label_names.pack(pady=10, padx=10)

l = tk.Label(window, text=f'Link to the people story: {random.choice(urls)}')
l.config(font=('Arial', 12))
l.pack(padx=10, pady=10)

o = tk.Label(window, text=f'Name of the slave: {random.choice(authors)}')
o.config(font=('Arial', 12))
o.pack(padx=10, pady=10)

window.mainloop()
