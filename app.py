import tkinter as tk
from tkinter import ttk
import time
import threading
import random

class PID:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.last_error = 0
        self.integral = 0
        self.last_time = time.time()

    def compute(self, current_value):
        now = time.time()
        dt = now - self.last_time
        if dt == 0:
            return 0

        error = self.setpoint - current_value

        # Termo Proporcional
        P = self.kp * error

        # Termo Integral
        self.integral += error * dt
        I = self.ki * self.integral

        # Termo Derivativo
        derivative = (error - self.last_error) / dt
        D = self.kd * derivative

        # Saída do controlador (MV - porcentagem da válvula)
        output = P + I + D
        output = max(0, min(100, output))  # Mantém entre 0% e 100%

        # Atualiza os valores anteriores
        self.last_error = error
        self.last_time = now

        return output

class PIDTankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador PID - Nível e Temperatura")
        self.root.geometry("500x550")
        self.root.configure(bg="yellow")

        self.kp = 2.0
        self.ki = 0.5
        self.kd = 0.1
        self.sp = 50  # Set Point inicial (nível desejado)
        self.pv = 30  # Nível inicial do tanque
        self.mv = 0   # Porcentagem da válvula
        self.temperature = 25  # Temperatura inicial (°C)
        self.temp_target = 25  # Alvo da temperatura para suavizar mudanças

        self.pid = PID(self.kp, self.ki, self.kd, self.sp)

        # Interface gráfica
        ttk.Label(root, text="Set Point (SP) - Nível:", background="yellow").pack()
        self.sp_entry = ttk.Entry(root)
        self.sp_entry.insert(0, str(self.sp))
        self.sp_entry.pack()

        ttk.Label(root, text="Nível Atual (PV):", background="yellow").pack()
        self.pv_label = ttk.Label(root, text=f"{self.pv:.2f}")
        self.pv_label.pack()

        ttk.Label(root, text="Abertura da Válvula (MV) %:", background="yellow").pack()
        self.mv_label = ttk.Label(root, text=f"{self.mv:.2f}%")
        self.mv_label.pack()

        ttk.Label(root, text="Temperatura (°C - PT100):", background="yellow").pack()
        self.temp_label = ttk.Label(root, text=f"{self.temperature:.2f}°C")
        self.temp_label.pack()

        # Ajustes de Kp, Ki, Kd
        ttk.Label(root, text="Kp:", background="yellow").pack()
        self.kp_entry = ttk.Entry(root)
        self.kp_entry.insert(0, str(self.kp))
        self.kp_entry.pack()

        ttk.Label(root, text="Ki:", background="yellow").pack()
        self.ki_entry = ttk.Entry(root)
        self.ki_entry.insert(0, str(self.ki))
        self.ki_entry.pack()

        ttk.Label(root, text="Kd:", background="yellow").pack()
        self.kd_entry = ttk.Entry(root)
        self.kd_entry.insert(0, str(self.kd))
        self.kd_entry.pack()

        self.start_button = ttk.Button(root, text="Iniciar", command=self.start_pid)
        self.start_button.pack()

        # Canvas para desenhar o tanque
        self.canvas = tk.Canvas(root, width=200, height=250, bg="white")
        self.canvas.pack(pady=10)
        self.tank_rect = self.canvas.create_rectangle(50, 200, 150, 200 - self.pv, fill="blue")

        self.running = False

    def start_pid(self):
        try:
            self.sp = float(self.sp_entry.get())
            self.kp = float(self.kp_entry.get())
            self.ki = float(self.ki_entry.get())
            self.kd = float(self.kd_entry.get())
        except ValueError:
            return  # Evita erro caso digitem algo inválido

        self.pid = PID(self.kp, self.ki, self.kd, self.sp)
        self.running = True
        thread = threading.Thread(target=self.update_pid, daemon=True)
        thread.start()

    def update_pid(self):
        while self.running:
            self.mv = self.pid.compute(self.pv)

            # Simulação do nível do tanque baseado na válvula
            if self.mv > 0:
                self.pv += (self.mv / 100) * 2  # Entrada de água
            self.pv -= 0.5  # Simula vazamento natural

            # Garante que o nível fique entre 0 e 100
            self.pv = max(0, min(100, self.pv))

            # Simulação da temperatura (PT100) com atraso térmico
            if self.pv > 50:
                self.temp_target = 70  # Se o nível está alto, a temperatura sobe para 70°C
            else:
                self.temp_target = 25  # Se o nível está baixo, a temperatura esfria para 25°C

            # A temperatura se ajusta lentamente ao alvo
            self.temperature += (self.temp_target - self.temperature) * 0.1

            # Adiciona ruído para simular medições reais do PT100
            self.temperature += random.uniform(-0.5, 0.5)

            # Mantém a temperatura dentro de um limite
            self.temperature = max(10, min(100, self.temperature))

            # Atualiza os valores na interface
            self.pv_label.config(text=f"{self.pv:.2f}")
            self.mv_label.config(text=f"{self.mv:.2f}%")
            self.temp_label.config(text=f"{self.temperature:.2f}°C")

            # Atualiza o desenho do tanque
            self.canvas.coords(self.tank_rect, 50, 200, 150, 200 - self.pv)

            time.sleep(0.5)

if __name__ == "__main__":
    root = tk.Tk()
    app = PIDTankApp(root)
    root.mainloop()
