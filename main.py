"""ПРостенький таймер подсчета рабочей или учебной сессии."""
import time
from tkinter import *
import tkinter as tk


window = tk.Tk()

# РАзмер окна.
WIDTH, HEIGHT = 300, 150

window.title('TimerWork')
window.geometry('{}x{}'.format(WIDTH, HEIGHT))
window.resizable(width=False, height=False)
var = tk.StringVar(value='0 сек')
var_last = tk.StringVar(value='')

# Поле основного таймера.
lbl = tk.Label(window, textvariable=var, font=('Arial', 18))
lbl.grid(column=4, row=0)

# Поле последней сохраненной сессии.
lbl_last = tk.Label(window, textvariable=var_last, font=('Arial', 12))

# Флаг состояния таймера, True запущен.
timer_running = False

# Инициализирую глобальные переменные.
start_time = 0
elapsed = 0

def convert_to_human_readable_time(elapsed):
    """Переводит монотонное время в человеко-читаемое."""
    hours, rem = divmod(elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    return f'{hours} ч. {minutes:02d} мин. {seconds:02d} сек.'

def update_timer():
    """Вычисляет время с момента запуска."""
    global elapsed
    if timer_running:
        elapsed = int(time.monotonic() - start_time)
        var.set(convert_to_human_readable_time(elapsed))
        window.after(500, update_timer)


def start():
    """Запускает или продолжает отсчет таймера, флаг timer_running = True."""
    global timer_running, start_time
    if not timer_running:
        start_time = time.monotonic() - elapsed
        timer_running = True
        update_timer()
        btn_star.configure(text='Отсчет запущен!')
        btn_reset.grid_forget()
        btn_star.grid_forget()
        btn_stop.grid(column=4, row=3)

def stop():
    """Останавливает таймер, флаг timer_running = False"""
    global timer_running
    timer_running = False
    btn_star.configure(text='Продолжить')
    btn_star.grid(column=4, row=2)
    btn_reset.grid(column=4, row=4)
    btn_stop.grid_forget()


def reset():
    """Сохраняет время последнего сеанса и сбрасывает основой счетчик."""
    global elapsed
    if not timer_running:
        var.set(f'Сброшено.')
        btn_star.configure(text='Старт')
        var_last.set(f'Последний сеанс: '
                     f'{convert_to_human_readable_time(elapsed)}')
        lbl_last.grid(column=4, row=5)
        elapsed = 0
        btn_reset.grid_forget()
        btn_stop.grid_forget()


# Кнопки управления.
btn_star = Button(window, width=40, text='Старт', command=start)
btn_star.grid(column=4, row=2)

btn_stop = Button(window, width=40, text='Стоп', command=stop)
btn_stop.grid(column=4, row=3)

btn_reset = Button(
    window, 
    width=40, 
    text='Сбросить и сохранить последнее время', 
    command=reset
)
btn_reset.grid(column=4, row=4)

window.mainloop()
