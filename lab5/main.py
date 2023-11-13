import tkinter as tk
import inspect
from tkinter import messagebox
from date_utils import get_current_date, add_days_to_date, format_date, calculate_date_difference, is_leap_year


class DateUtilsApp:
    def __init__(self, master):
        self.master = master
        master.title("Date Utils App")

        # Метка для отображения текущей даты
        self.current_date_label = tk.Label(master, text="Текущая дата:")
        self.current_date_label.pack()

        # Кнопка для отображения документации get_current_date
        self.get_current_date_button = tk.Button(master, text="get_current_date",
                                                 command=lambda: self.show_documentation(get_current_date))
        self.get_current_date_button.pack()

        # Кнопка для отображения документации add_days_to_date
        self.add_days_to_date_button = tk.Button(master, text="add_days_to_date",
                                                 command=lambda: self.show_documentation(add_days_to_date))
        self.add_days_to_date_button.pack()

        # Кнопка для отображения документации format_date
        self.format_date_button = tk.Button(master, text="format_date",
                                            command=lambda: self.show_documentation(format_date))
        self.format_date_button.pack()

        # Кнопка для отображения документации calculate_date_difference
        self.calculate_difference_button = tk.Button(master, text="calculate_date_difference",
                                                     command=lambda: self.show_documentation(calculate_date_difference))
        self.calculate_difference_button.pack()

        # Кнопка для отображения документации is_leap_year
        self.leap_year_check_button = tk.Button(master, text="is_leap_year",
                                                command=lambda: self.show_documentation(is_leap_year))
        self.leap_year_check_button.pack()

    def show_documentation(self, func):
        docstring = inspect.getdoc(func)
        print(f"Документация:\n{docstring}")
        if docstring is not None:
            messagebox.showinfo("Документация", docstring)
        else:
            messagebox.showinfo("Документация", "Документация отсутствует.")


if __name__ == "__main__":
    root = tk.Tk()
    app = DateUtilsApp(root)
    root.mainloop()