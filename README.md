# theremin
Trying to build a theremin with two ultrasonic sensors. 

```sh
    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 firmwares/esp8266-1m-20220117-v1.18.bin

    esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 firmwares/esp32-20220117-v1.18.bin
```