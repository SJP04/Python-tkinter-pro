from tkinter import *
from tkinter import ttk

def submit_form():
    full_name = e1.get()
    email = e2.get()
    gender = "Male" if v.get() == 1 else "Female"
    country = countrychoosen.get()
    java_selected = "Yes" if a.get() == 1 else "No"
    python_selected = "Yes" if b.get() == 1 else "No"

    print("Full Name:", full_name)
    print("Email:", email)
    print("Gender:", gender)
    print("Country:", country)
    print("Java Selected:", java_selected)
    print("Python Selected:", python_selected)

window = Tk()
window.geometry("600x300")
window.title("Registration Form")

# Registration Form Label
label = Label(window, text="Registration Form", font=("arial", 25))
label.place(x=10, y=10)

# Full name
l1 = Label(window, text="Full name", font=("arial", 13))
l1.place(x=10, y=62)
e1 = Entry(window, width=60)
e1.place(x=140, y=62)

# Email
l2 = Label(window, text="Email", font=("arial", 13))
l2.place(x=10, y=92)
e2 = Entry(window, width=60)
e2.place(x=140, y=92)

# Gender
l3 = Label(window, text="Gender", font=("arial", 13))
l3.place(x=10, y=122)
v = IntVar()
Radiobutton(window, text="Male", variable=v, value=1, font=("arial", 10)).place(x=140, y=122)
Radiobutton(window, text="Female", variable=v, value=2, font=("arial", 10)).place(x=209, y=122)

# Country
l4 = Label(window, text="Country", font=("arial", 13))
l4.place(x=10, y=152)
c = StringVar()
countrychoosen = ttk.Combobox(window, width=25, textvariable=c, state="readonly")
countrychoosen['values'] = ("Select your country", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
                            "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan",
                            "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", 
                            "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", 
                            "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", 
                            "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus",
                            "Czech Republic", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", 
                            "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", 
                            "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
                            "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", 
                            "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", 
                            "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
                            "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", 
                            "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives",
                            "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova",
                            "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", 
                            "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", 
                            "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru",
                            "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
                            "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", 
                            "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
                            "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka")

countrychoosen.place(x=140, y=153)
countrychoosen.set("Select your country")

# Programming
l5 = Label(window, text="Programming", font=("arial", 13))
l5.place(x=10, y=185)
a = IntVar()
b = IntVar()
Checkbutton(window, text="Java", variable=a, onvalue=1, offvalue=0, font=("arial", 10)).place(x=140, y=187)
Checkbutton(window, text="Python", variable=b, onvalue=1, offvalue=0, font=("arial", 10)).place(x=200, y=187)

# Submit button
l7 = Button(window, text="Submit", background="#ad0a15", command=submit_form)
l7.place(x=20, y=223)

window.mainloop()