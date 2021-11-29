import smbus
import time


bus = smbus.SMBus(1)

time.sleep(1)

SLEEP = 0.1

GREEN = 0x15
RED = 0x14

SECTOR_12 = 0x20
SECTOR_34 = 0x21
SECTOR_56 = 0x22
SECTOR_78 = 0x24

LED_LIST = [
    {"sector":SECTOR_12, "pin": 0},  # LED_00
    {"sector":SECTOR_12, "pin": 1},  # LED_01
    {"sector":SECTOR_12, "pin": 2},  # LED_02
    {"sector":SECTOR_12, "pin": 3},  # LED_03
    {"sector":SECTOR_12, "pin": 4},  # LED_04
    {"sector":SECTOR_12, "pin": 5},  # LED_05
    {"sector":SECTOR_12, "pin": 6},  # LED_06
    {"sector":SECTOR_12, "pin": 7},  # LED_07
    {"sector":SECTOR_34, "pin": 0},  # LED_08
    {"sector":SECTOR_34, "pin": 1},  # LED_09
    {"sector":SECTOR_34, "pin": 2},  # LED_10
    {"sector":SECTOR_34, "pin": 3},  # LED_11
    {"sector":SECTOR_34, "pin": 4},  # LED_12
    {"sector":SECTOR_34, "pin": 5},  # LED_13
    {"sector":SECTOR_34, "pin": 6},  # LED_14
    {"sector":SECTOR_34, "pin": 7},  # LED_15
    {"sector":SECTOR_56, "pin": 0},  # LED_16
    {"sector":SECTOR_56, "pin": 1},  # LED_17
    {"sector":SECTOR_56, "pin": 2},  # LED_18
    {"sector":SECTOR_56, "pin": 3},  # LED_19
    {"sector":SECTOR_56, "pin": 4},  # LED_20
    {"sector":SECTOR_56, "pin": 5},  # LED_21
    {"sector":SECTOR_56, "pin": 6},  # LED_22
    {"sector":SECTOR_56, "pin": 7},  # LED_23
    {"sector":SECTOR_78, "pin": 0},  # LED_24
    {"sector":SECTOR_78, "pin": 1},  # LED_25
    {"sector":SECTOR_78, "pin": 2},  # LED_26
    {"sector":SECTOR_78, "pin": 3},  # LED_27
    {"sector":SECTOR_78, "pin": 4},  # LED_28
    {"sector":SECTOR_78, "pin": 5},  # LED_29
    {"sector":SECTOR_78, "pin": 6},  # LED_20
    {"sector":SECTOR_78, "pin": 7},  # LED_21
]




def init_Box():
    # Set Port_A of all segments to output   
    bus.write_byte_data(SECTOR_12, 0x00, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_34, 0x00, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_56, 0x00, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_78, 0x00, 0x00)
    time.sleep(SLEEP)
    # Set Port_B of all segments to output
    bus.write_byte_data(SECTOR_12, 0x01, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_34, 0x01, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_56, 0x01, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_78, 0x01, 0x00)
    time.sleep(SLEEP)
    
def off_all_LEDs():
    # Set Port_A of all segments to output   
    bus.write_byte_data(SECTOR_12, RED, 0xFF)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_34, RED, 0xFF)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_56, RED, 0xFF)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_78, RED, 0xFF)
    time.sleep(SLEEP)
    # Set Port_B of all segments to output
    bus.write_byte_data(SECTOR_12, GREEN, 0xFF)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_34, GREEN, 0xFF)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_56, GREEN, 0xFF)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_78, GREEN, 0xFF)
    time.sleep(SLEEP)
    
def set_LED( led, color):
    tmp_data = bus.read_byte_data(LED_LIST[led]["sector"], color)
    tmp_data &= ~(0x01 << LED_LIST[led]["pin"])
    bus.write_byte_data(LED_LIST[led]["sector"], color, tmp_data)

def reset_LED( led, color):
    tmp_data = bus.read_byte_data(LED_LIST[led]["sector"], color)
    tmp_data |= (0x01 << LED_LIST[led]["pin"])
    bus.write_byte_data(LED_LIST[led]["sector"], color, tmp_data)

def all_red_on():
    bus.write_byte_data(SECTOR_12, RED, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_34, RED, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_56, RED, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_78, RED, 0x00)
    time.sleep(SLEEP)

def all_green_on():
    bus.write_byte_data(SECTOR_12, GREEN, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_34, GREEN, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_56, GREEN, 0x00)
    time.sleep(SLEEP)
    bus.write_byte_data(SECTOR_78, GREEN, 0x00)
    time.sleep(SLEEP)

def test_box():
    for i in range(0,31):
        set_LED(i,RED)
        time.sleep(0.2)
        reset_LED(i,RED)

    for i in range(0,31):
        set_LED(i,GREEN)
        time.sleep(0.2)
        reset_LED(i,GREEN)

    all_red_on()
    time.sleep(1)
    off_all_LEDs()
    all_green_on()
    time.sleep(1)
    off_all_LEDs()

    
off_all_LEDs()
init_Box()

test_box()



off_all_LEDs()

