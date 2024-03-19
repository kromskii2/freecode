import tkinter as tk
from tkinter import messagebox

class ScheduleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Расписание рабочего дня и личные финансы")

        # Создание виджетов
        self.label_schedule = tk.Label(master, text="Расписание рабочего дня")
        self.label_schedule.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.schedule_text = tk.Text(master, height=10, width=40)
        self.schedule_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.label_finances = tk.Label(master, text="Личные финансы")
        self.label_finances.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.finances_text = tk.Text(master, height=10, width=40)
        self.finances_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.button_save = tk.Button(master, text="Сохранить", command=self.save_data)
        self.button_save.grid(row=4, column=0, padx=10, pady=10)

        self.button_load = tk.Button(master, text="Загрузить", command=self.load_data)
        self.button_load.grid(row=4, column=1, padx=10, pady=10)

    def save_data(self):
        schedule_data = self.schedule_text.get("1.0", tk.END)
        finances_data = self.finances_text.get("1.0", tk.END)

        # Здесь можно добавить код для сохранения данных в файл или базу данных
        messagebox.showinfo("Сохранение", "Данные успешно сохранены!")

    def load_data(self):
        # Здесь можно добавить код для загрузки данных из файла или базы данных
        # и отображения их в соответствующих текстовых полях
        messagebox.showinfo("Загрузка", "Данные успешно загружены!")

def main():
    root = tk.Tk()
    app = ScheduleApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
