import tkinter as tk


window = tk.Tk()
window.title('Calc')
window.geometry('500x550')
window.resizable(False, False)
window.configure(bg='black')

# Логика
def calculate(operation):
	global formula

	if operation == 'C':
		formula = ''
	elif operation == 'Del':
		formula = formula[0:-1]
	elif operation == 'x^2':
		formula = str((eval(formula)) ** 2)
	elif operation == '=':
		formula = str(eval(formula))
	elif operation == '%':
		formula = str(eval(formula)/100)
	elif operation == '+/-':
		formula = str((eval(formula)* -1))
	else:
		if formula == '0':
			formula = ''
		formula += operation
	label_text.configure(text=formula)

# Окно вывода
formula = '0'
label_text = tk.Label(text=formula, font=('Roboto', 45, 'bold'), fg='white', bg='black')
label_text.place(x=11, y=50)

# Кнопки
buttons = [ 
			'C', 'Del', '*', '=',
			'1', '2', '3', '/',
			'4', '5', '6', '+',
			'7', '8', '9', '-',
			'+/-', '0', '%', 'x^2'
		]
x = 18
y = 160

for button in buttons:
	get_lbl = lambda x=button: calculate(x)
	tk.Button(text=button, bg='orange', font=('Roboto', 25), command=get_lbl).place(x=x, y=y, width=120, height=70)
	x += 119
	if x > 400:
		x = 18
		y += 75

window.mainloop()