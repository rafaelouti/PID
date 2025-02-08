import tkinter as tk
import threading
import time
import random
import math

class MotorSupervisory:
    def __init__(self, root):
        self.root = root
        self.root.title("Supervisório Industrial - Motores")
        self.root.geometry("600x400")
        root.configure(bg="green") 

        # Canvas para desenhar motores
        self.canvas = tk.Canvas(root, width=600, height=250, bg="white")
        self.canvas.pack()

        # Motores e LEDs
        self.motors = [
            {"x": 100, "y": 100, "status": False, "led": None, "fan": None, "angle": 0, "temp": 25},
            {"x": 250, "y": 100, "status": False, "led": None, "fan": None, "angle": 0, "temp": 25},
            {"x": 400, "y": 100, "status": False, "led": None, "fan": None, "angle": 0, "temp": 25},
        ]

        # Criando motores, hélices e LEDs
        for motor in self.motors:
            self.canvas.create_oval(
                motor["x"], motor["y"], motor["x"] + 50, motor["y"] + 50, fill="gray"
            )
            motor["fan"] = self.canvas.create_line(  # Hélice
                motor["x"] + 25, motor["y"] + 25, motor["x"] + 25, motor["y"], width=4, fill="black"
            )
            motor["led"] = self.canvas.create_oval(  # LED
                motor["x"] + 15, motor["y"] + 60, motor["x"] + 35, motor["y"] + 80, fill="red"
            )

        # Criando botões de controle
        self.buttons = []
        for i in range(3):
            btn = tk.Button(root, text=f"Ligar Motor {i+1}", command=lambda i=i: self.toggle_motor(i))
            btn.pack(side=tk.LEFT, padx=10)
            self.buttons.append(btn)

        # Labels de temperatura
        self.temp_labels = []
        for i in range(3):
            lbl = tk.Label(root, text=f"Temp. Motor {i+1}: 25°C")
            lbl.pack(side=tk.LEFT, padx=10)
            self.temp_labels.append(lbl)

        # Atualizar temperaturas
        self.update_temperatures()

    def toggle_motor(self, index):
        """Liga ou desliga o motor e anima a rotação da hélice"""
        motor = self.motors[index]
        motor["status"] = not motor["status"]
        
        # Atualiza LED e cor do botão
        color = "green" if motor["status"] else "red"
        self.canvas.itemconfig(motor["led"], fill=color)
        self.buttons[index].config(text=f"{'Desligar' if motor['status'] else 'Ligar'} Motor {index+1}")

        # Inicia animação se estiver ligado
        if motor["status"]:
            threading.Thread(target=self.animate_motor, args=(index,), daemon=True).start()

    def animate_motor(self, index):
        """Anima a hélice do motor girando"""
        motor = self.motors[index]
        while motor["status"]:
            motor["angle"] += 20  # Incrementa o ângulo
            if motor["angle"] >= 360:
                motor["angle"] = 0

            # Calcula nova posição da hélice
            x1 = motor["x"] + 25 + 20 * math.cos(math.radians(motor["angle"]))
            y1 = motor["y"] + 25 + 20 * math.sin(math.radians(motor["angle"]))

            # Atualiza hélice no canvas
            self.canvas.coords(motor["fan"], motor["x"] + 25, motor["y"] + 25, x1, y1)
            self.root.update()
            time.sleep(0.1)

    def update_temperatures(self):
        """Simula variação de temperatura"""
        for i, motor in enumerate(self.motors):
            if motor["status"]:
                motor["temp"] += random.uniform(-0.5, 1.5)
            else:
                motor["temp"] = max(25, motor["temp"] - 0.5)

            self.temp_labels[i].config(text=f"Temp. Motor {i+1}: {motor['temp']:.1f}°C")

        self.root.after(1000, self.update_temperatures)

# Iniciar interface
root = tk.Tk()
app = MotorSupervisory(root)
root.mainloop()
