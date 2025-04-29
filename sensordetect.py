import RPi.GPIO as GPIO
import time
import pygame

# Define GPIO pins
FLAME_SENSOR_PIN = 17   # GPIO17 (Pin 11)
GAS_SENSOR_PIN = 27     # GPIO27 (Pin 13)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_SENSOR_PIN, GPIO.IN)
GPIO.setup(GAS_SENSOR_PIN, GPIO.IN)

# Initialize pygame for sound alert
pygame.mixer.init()
pygame.mixer.music.load("fire-alarm-33770_OyJkH2cA.mp3")  # Make sure alert.mp3 is in the same folder

print("Monitoring Gas and Flame Sensors. Press Ctrl+C to exit.")

# State to avoid playing the alert repeatedly
alert_playing = False

try:
    while True:
        flame_detected = GPIO.input(FLAME_SENSOR_PIN) == 0  # LOW = Flame detected
        gas_detected = GPIO.input(GAS_SENSOR_PIN) == 0      # LOW = Gas detected

        if flame_detected:
            print("?? Flame detected!")
        else:
            print("? No flame detected.")

        if gas_detected:
            print("?? Gas leak detected!")
        else:
            print("? No gas leak detected.")

        if (flame_detected or gas_detected) and not alert_playing:
            print("?? Playing alert sound!")
            pygame.mixer.music.play()
            alert_playing = True
        elif not flame_detected and not gas_detected:
            pygame.mixer.music.stop()
            alert_playing = False

        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting gracefully...")
    pygame.mixer.music.stop()
    GPIO.cleanup()

