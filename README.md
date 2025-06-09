# 🌱 Environmental Quality Monitoring System

This project monitors environmental parameters such as **temperature** and **humidity** using a **DHT22 sensor** connected to an **ESP32** board. The data is sent over Wi-Fi to a **Flask server**, which stores the data either in a database or in a text file (for local logging). This setup is ideal for IoT-based monitoring of air quality in smart farming, urban planning, or greenhouses.

---


---

## 🧰 Hardware Requirements

- ESP32 development board
- DHT22 temperature and humidity sensor
- Breadboard + jumper wires
- Wi-Fi network

---

## 🔌 Connection Details

| DHT22 Pin | ESP32 Pin | Notes                    |
|-----------|-----------|--------------------------|
| VCC       | 3.3V      | Power supply             |
| DATA      | GPIO 4    | Connect to digital pin   |
| GND       | GND       | Ground                   |

> 💡 *Use a 10kΩ pull-up resistor between DATA and VCC if needed.*

---

## 📲 ESP32 Code Setup

Edit the `code/dht_read_send.ino` file:

```cpp
const char* ssid = "your_SSID";             // Your Wi-Fi name
const char* password = "your_PASSWORD";     // Your Wi-Fi password
const char* serverName = "http://<server_ip>:5000/add_data";  // Your Flask server IP


"# environmental-quality-monitoring-system" 
