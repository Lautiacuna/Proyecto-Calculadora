import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculadora')
        # Tamaño de la ventana y la ubicación
        self.root.geometry("330x320")
        self.root['background'] = '#ffffff'
        self.root.resizable(width=False, height=False)

        # Almacenar elementos de entrada clave
        self.mylist = []
        # Que mostrar en la interfaz
        self.result_num = tk.StringVar()
        self.result_num.set(0)
        self.layout()

        self.root.mainloop()


    def put(self,x):
        self.mylist.append(x)
        self.result_num.set(''.join(self.mylist))


    def delete(self):
        '' 'Función de botón Borrar' ''
        self.mylist.clear()
        self.result_num.set(0)


    def back(self):
        '' 'Función de botón Eliminar, eliminar un número u operador' ''
        if len(self.mylist) > 0:
            del self.mylist[-1]
            self.result_num.set(self.mylist)


    def calculation(self):
        '' 'Botón de cálculo' ''
        expression = ''.join(self.mylist)
        result = eval(expression)
        self.result_num.set(result)
        # Borrar la lista de datos después de calcular el resultado y solo almacene el resultado del cálculo actual
        self.mylist.clear()
        # join une los elementos de la lista en cadenas, todos los elementos de la lista deben ser del tipo str
        self.mylist.append(str(result))


    def operate(self,operator):
        
        if len(self.mylist) > 0:
            if self.mylist[-1] in ['+', '-', '*', '/','.']:
                self.mylist[-1] = operator
            else:
                self.mylist.append(operator)

            self.result_num.set(''.join(self.mylist))


    def inverse(self):
        if len(self.mylist) > 0 and self.mylist[-1] not in ['+', '-', '*', '/','.']:
            self.mylist[-1] = str(-int(self.mylist[-1]))
            self.result_num.set(''.join(self.mylist))

    def layout(self):
        # La primera línea de la cuadrícula muestra el panel
        # Mostrar el panel de entrada clave y resultados de cálculo
        label = tk.Label(self.root, textvariable=self.result_num, width=20, height=2,
                        justify='left', anchor='se', bg='#ffffff', font=('Song Ti', 20))
        label.grid(row=0, column=0, padx=4, pady=4, columnspan=4)


        # La segunda línea comienza con el operador
        button_clear = tk.Button(self.root, text='C', width=5, font=(
            'Song Ti', 16), bg='#C0C0C0', command=self.delete)
        button_clear.grid(row=1, column=0, padx=4, pady=4)
        # Eliminar clave
        button_back = tk.Button(self.root, text='←', width=5, font=(
            'Song Ti', 16), bg='#C0C0C0', command=self.back)
        button_back.grid(row=1, column=1, padx=4, pady=4)
        # División
        button_div = tk.Button(self.root, text='/', width=5, font=('Song Ti', 16),
                            bg='#C0C0C0', command=lambda: self.operate('/'))
        button_div.grid(row=1, column=2, padx=4, pady=4)
        # Multiplicación
        button_mult = tk.Button(self.root, text='*', width=5, font=('Song Ti', 16),
                                bg='#C0C0C0', command=lambda: self.operate('*'))
        button_mult.grid(row=1, column=3, padx=4, pady=4)

        # La tercera línea comienza con un número

        # La tercera fila
        button_seven = tk.Button(self.root,text=7, width=5, font=(
            'Song Ti', 16), bg='#FFDEAD', command=lambda: self.put('7'))
        button_seven.grid(row=2, column=0, padx=4)

        button_eight = tk.Button(self.root,text=8, width=5, font=(
            'Song Ti', 16), bg='#FFDEAD', command=lambda: self.put('8'))
        button_eight.grid(row=2, column=1, padx=4)

        button_nine = tk.Button(self.root,text=9, width=5, font=(
            'Song Ti', 16), bg='#FFDEAD', command=lambda: self.put('9'))
        button_nine.grid(row=2, column=2, padx=4)

        button_sub = tk.Button(self.root, text='-', width=5, font=('Song Ti', 16),
                            bg='#C0C0C0', command=lambda: self.operate('-'))
        button_sub.grid(row=2, column=3, padx=4, pady=4)

        # Cuarta línea
        button_four = tk.Button(self.root,text=4, width=5, font=(
            'Song Ti', 16), bg='#FFDEAD', command=lambda: self.put('4'))
        button_four.grid(row=3, column=0, padx=4)

        button_five = tk.Button(self.root,text=5, width=5, font=(
            'Song Ti', 16), bg='#FFDEAD', command=lambda: self.put('5'))
        button_five.grid(row=3, column=1, padx=4)

        button_six = tk.Button(self.root,text=6, width=5, font=('Song Ti', 16),
                            bg='#FFDEAD', command=lambda: self.put('6'))
        button_six.grid(row=3, column=2, padx=4)

        button_add = tk.Button(self.root, text='+', width=5, font=('Song Ti', 16),
                            bg='#C0C0C0', command=lambda: self.operate('+'))
        button_add.grid(row=3, column=3, padx=4, pady=4)

        # La quinta línea
        button_one = tk.Button(self.root, text=1, width=5, font=(
            'Song Ti', 16), bg='#FFDEAD', command=lambda: self.put('1'))
        button_one.grid(row=4, column=0, padx=4)

        button_two = tk.Button(self.root, text=2, width=5, font=(
            'Song Ti', 16), bg='#FFDEAD', command=lambda: self.put('2'))
        button_two.grid(row=4, column=1, padx=4)

        button_three = tk.Button(self.root, text=3, width=5, font=(
            'Song Ti', 16), bg='#FFDEAD', command=lambda: self.put('3'))
        button_three.grid(row=4, column=2, padx=4)

        button_equal = tk.Button(self.root, text='=', width=5, height=3, font=(
            'Song Ti', 16), bg='#C0C0C0', command=self.calculation)
        button_equal.grid(row=4, column=3, padx=4, rowspan=5)

        # Sexta línea
        # Invertido, usado para representar números opuestos y negativos
        button_not = tk.Button(self.root, text='+/-', width=5,
                            font=('Song Ti', 16), bg='#FFDEAD', command=self.inverse)
        button_not.grid(row=5, column=0, padx=4)

        button_zero = tk.Button(self.root, text=0, width=5, font=(
            'Song Ti', 16), bg='#FFDEAD', command=lambda: self.put('0'))
        button_zero.grid(row=5, column=1, padx=4)

        # Punto decimal
        button_pot = tk.Button(self.root, text='.', width=5, font=(
            'Song Ti', 16), bg='#FFDEAD', command=lambda: self.put('.'))
        button_pot.grid(row=5, column=2, padx=4, pady=4)



app = App()