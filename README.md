# RGB LED & Potentiometer Control
###  | EEC3612 Embedded Systems Lab


---

## 👥 Team Members

| Name | Role |
|------|------|
| **Ravan Jafarov** | Team Leader, Hardware (Task 2 - Potentiometer) |
| Azar Aslanov | Hardware (Task 1 - RGB LED) |
| Riad Alizada | Code (Task 1 - Fixed colors) |
| Hasan Aliyev | Code (Task 2 - Potentiometer) |

📅 **Date:** 16.10.2025  
🎓 **Professor:** Kim Deokhwan  
🛠️ **LA:** Rasim Mahmudov

---

## 🎯 Objectives

1. **Task 1:** Generate color combinations **without** a potentiometer
2. **Task 2:** Generate dynamic colors **with** a potentiometer

---

## 🔧 Components Used

- Arduino Uno
- Breadboard
- RGB LED (Common Anode)
- 3 × 220 Ω resistors
- Potentiometer (10 kΩ)
- Jumper wires
- USB Type-B cable

---

## 📂 Project Structure
rgb-led-team7/
├── README.md
├── task1_fixed_colors/
│   └── task1.py
├── task2_potentiometer/
│   └── task2.py
└── images/
    ├── task1_circuit.jpg
    └── task2_circuit.jpg



---

## 💻 Task 1: Fixed Color Combinations

### Purpose
Display 5+ colors using fixed PWM values (no potentiometer).

### Circuit
- Common Anode (long leg) → **+5V**
- R pin → **D11** via 220Ω
- G pin → **D12** via 220Ω
- B pin → **D13** via 220Ω

### Code
👉 See [`task1_fixed_colors/task1.py`](task1_fixed_colors/task1.py)

---

## 💻 Task 2: Potentiometer Control

### Purpose
Use analog input to dynamically control RGB brightness and create **16,777,216** color combinations.

### Circuit
- Potentiometer middle pin → **A4**
- Potentiometer side pins → **5V** and **GND**
- RGB LED same as Task 1

### Code
👉 See [`task2_potentiometer/task2.py`](task2_potentiometer/task2.py)

---

## 🚀 How to Run

1. Upload **Standard Firmata** to Arduino via Arduino IDE
2. Install PyFirmata:
   ```bash
   pip install pyfirmata
