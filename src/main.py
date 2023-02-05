import sys
import time
from argparse import ArgumentParser


from bluepy import btle

import ble_resources

def main():
  print("""
  BLE IoT Sensor Demo
  Author: Gary Stafford
  Reference: https://elinux.org/RPi_Bluetooth_LE
  """)
  
  # get args
  args = get_args()

  print("Connecting...")
  nano_sense = btle.Peripheral(args.mac_address)

  print("Discovering Services...")
  _ = nano_sense.services
  environmental_sensing_service = nano_sense.getServiceByUUID("181A")

  print("Discovering Characteristics")
  _ = environmental_sensing_service.getCharacteristics()

  while True:
    print("\n")

    temperature = ble_resources.read_temperature(environmental_sensing_service)
    humidity = ble_resources.read_humidity(environmental_sensing_service)
    pressure = ble_resources.read_pressure(environmental_sensing_service)

    print(f"Temperature: {round(temperature, 2)}°C")
    print(f"Humidity: {round(humidity, 2)}%")
    print(f"Barometric Pressure: {round(pressure, 2)} kPa")

    time.sleep(2)


def get_args():
  args_parser = ArgumentParser(description="BLE IoT Sensor Demo")
  args_parser.add_argument('mac_address', help="MAC address of the device to connect")
  return args_parser.parse_args()

if __name__ == "__main__":
  main()