import logging
import atexit
import socket
import time
import re
import os
import board
import neopixel
from datetime import datetime

timestampt = datetime.today()
filename = timestampt.strftime("%d-%m-%Y") + ".txt"
def utworz_plik_logu(nazwapliku) :
    if os.path.isfile(nazwapliku):
        pass
    else:
        plik = open(nazwapliku, "w")
        plik.close()

utworz_plik_logu(filename)


LISTA_BEACONOW = ['3V8SS', '9A1CIG', '9M2CNC', '9V1MH', '9V1RM', 'AA4VV', 'AC0C-1', 'BA7PC', 'BD7MLA', 'BG6SNJ', 'BG7IBS', 'BG7IS', 'BG8DIV', 'BH4RRG1', 'BH4RRG4', 'CT7ANO', 'DE1LON', 'DF2CK', 'DF4XX', 'DF7GB', 'DK0TE', 'DK2GOX', 'DK8NE', 'DK9IP', 'DL0LA', 'DL0LBS', 'DL1AXX', 'DL1HWS'
, 'DL3DTH', 'DL8LAS', 'DL8TG', 'DL9GTB', 'DM6EE', 'DO4DXA', 'DR4W', 'E28AC', 'EA1URA', 'ES5PC', 'ET3AA', 'F4VSQ', 'F5AHD', 'G3XBI', 'G4ZFE', 'GI4DOH', 'HA1AG', 'HA1VHF', 'HA6PX', 'HA7GN', 'HB9BXE', 'HB9DCO', 'HB9JCB', 'HG8A', 'HS8KVH', 'IK3STG', 'IK4VET', 'IK7YTT', 'IZ2CPS', 'JA1JRS'
, 'JA4ZRK', 'JG1VGX', 'JH7CSU1', 'JI1HFJ', 'JJ2VLY', 'JO1YYP', 'JQ1BVI', 'K1FC', 'K1TTT', 'K2DB', 'K2MFF-2', 'K2PO/7', 'K3PA-1', 'K4PP', 'K4XD', 'K5TR', 'K7MJG', 'K9IMM', 'K9LC', 'K9TM-4', 'KB5NJD', 'KC0VKN','SJ2W', 'DK3UA', 'SM7IUN', 'SE5E', 'RW9AV', 'RN4WA', 'RK3TD', 'SV8RV', 'LZ7AA'
, 'LZ4AE', 'ON3URE', 'OH0K/6'
, 'KQ8M', 'KU7T', 'LU1MAW', 'LU9DCE', 'LZ3CB', 'LZ4UX', 'MM0HVU', 'MM0ZBH', 'N2QT', 'N4RLI', 'N4ZR', 'N6TV', 'N7TUG', 'N9MKC', 'NA0B', 'NC7J', 'NH6HI', 'NN3RP', 'OE9GHV', 'OH6BG', 'OK1FCJ', 'OL7M', 'ON6ZQ', 'PA0MBO', 'PA5KT', 'PJ2A', 'R6YY', 'R9IR', 'RK3TD', 'RL3A-2', 'RN4WA', 'RW0A'
, 'S50ARX', 'SM0TCZ', 'SM6FMB', 'SP8R', 'SV1CDN', 'SZ1A', 'TF4X', 'UA0S', 'UA4M', 'V51YJ', 'VE2WU', 'VE6AO', 'VE6JY', 'VE6WZ', 'VE7CC', 'VK2GEL', 'VK3RASA', 'VK4CT', 'VK6ANC', 'VU2PTT', 'VY0ERC', 'W1NT-2', 'W1NT-6', 'W2AXR', 'W2LB', 'W2MV', 'W2NAF', 'W3LPL', 'W3OA', 'W3UA', 'W4AX'
, 'W4KAZ', 'W6YX', 'W7HR', 'W8WTS', 'W9XG', 'WA2ZYU', 'WA7LNW', 'WB6BEE', 'WC2L', 'WE9V', 'WI5V', 'WW1L', 'ZL4YL', 'WS3W', 'LA6TPA', 'R2AT', 'EA1HG', '3D2AG', 'PA3GRM', 'NL13862', 'IK2LFF', 'S53M', 'DM7EE', 'BH4XDZ', 'K7EG', 'BA4KW', 'CX6VM', 'UY2RA', 'JG1DLY', 'WA9VEE', 'W8WWV', 'RV7C'
, 'VK2EBN', 'G0KTN', 'DJ2BC', 'VK2LX', 'BI7JIS', 'OK2EW', 'OE6ADD', '9A5CW', 'LU0660016', 'OG73X', 'G0TMX', 'M0WJG', , 'LU9DMG', 'PE1PUX', 'GM6DX', 'BG2UKX', 'SV1DPJ', 'BG0ARE', 'N9PBJ', 'OH2BBT', 'KV4TT', 'DJ9IE', 'C91PM', 'PU2MST', 'BD7JNA', 'BD7NWR', 'UP2L', 'JQ1YUF', 'S55OO', 'BD7IBS'
, 'ES3V', 'DJ3AK', 'TZ4AM', 'EA1RX', 'EA5WU', 'G4AON', 'WZ7I', 'BD7IS', 'HB9FKK', 'RA0FF', 'EA2JG', 'BI8AZK', 'KC4LE', 'KC4YVA', 'KD2OGR', 'KD7YZ', 'KE3BK', 'KH6LC', 'KL7RA', 'KM3T', 'KM3T-2', 'KO7SS', 'KO7SS-7', 'KP2RUM', 'LY3G', 'G4HYG', 'RX3AFE', 'G3YPP', 'DF0RW', 'BD7LMD', 'UT7EZZ'
, 'SP5OSF', 'PE1RDP', 'PA5WT', 'R2AT/3', 'BA7JA', 'BA7KW', 'BG7JAW', '5W1SA', 'BD8CS', 'KC0CC']
print(len(LISTA_BEACONOW))

pasek_z_diodami = neopixel.NeoPixel(board.D18, 92, auto_write=False)

ZNAK = "YourCallsign"
#kolory
white = (255,255,255) #0-5db
blue = (0,0,255) #6-10db
green = (0,255,0) #11-15db
yellow = (255,255,0) #16-20db
purple = (255,0,255) #21-30db
red = (255,0,0) #30db and up


@atexit.register
def odczekaj_minute_przed_wyjsciem(*args, **kwargs):
    time.sleep(60.0)

def zapal_diode(diody,bikon, sila):
    bikon = bikon[:-3]
    sila_int = int(sila)
    kolor = (0,0,0)
    if sila_int <= 5:
        kolor = white
    elif 5 < sila_int <= 10:
        kolor = blue
    elif 10 < sila_int <= 15:
        kolor = green
    elif 15 < sila_int <= 20:
        kolor = yellow
    elif 20 < sila_int <= 25:
        kolor = purple
    else:
        kolor = red
    try:
        nr_diody = LISTA_BEACONOW.index(bikon)
        diody[nr_diody] = kolor
        diody.show()
    except (ValueError, IndexError):
        pass

def wygas_diode(diody):
    for i in range(len(diody)):
        nowy_kolor = diody[i]
        r = nowy_kolor[0]
        g = nowy_kolor[1]
        b = nowy_kolor[2]
        if r > 0 :
            r = r - 5
        #if r < 0 :
        #    r = 0
        if g > 0 :
            g = g - 5
        #if g < 0 :
        #    g = 0
        if b > 0 :
            b = b - 5
        #if b < 0 :
        #    b = 0
        nowy_kolor = r,g,b
        diody[i] = nowy_kolor
    diody.show()




def wczytaj_linie(s):
    buf = b""
    while True:
        c = s.recv(1)
        buf += c
        if c == b"\n":
            return buf


def zaloguj_sie(s, login):
    buf = b""
    while True:
        c = s.recv(1)
        buf += c
        if c == b"\n":
            logging.debug('zaloguj_sie: odrzucam linię: %r', buf)
            buf = b""
            print(buf)
        if c == b":":
            if buf == b"Please enter your call:":
                print(buf)
                s.send(login.encode() + b"\r\n")
                logging.info('zaloguj_sie: zalogowany?')
                return


def main():
    czas = time.time()
    logging.info('Bot się uruchamia, za 10s nawiąże połączenie...')
    time.sleep(10.0)
    #signal.alarm(60 * 60)
    s = socket.socket()
    s.connect(("telnet.reversebeacon.net", 7000))
    zaloguj_sie(s, ZNAK)
    while True:
        data = datetime.utcnow()
        if (data.hour == 0 and data.minute == 0):
            global filename
            timestampt = datetime.today()
            filename = timestampt.strftime("%d-%m-%Y") + ".txt"
            utworz_plik_logu(filename)
        if time.time() - czas > 10:
            czas = time.time()
            wygas_diode(pasek_z_diodami)
        linia = wczytaj_linie(s)
        msg = linia.decode('utf8', 'ignore').strip()
        #print(msg)
        #print(pasek_z_diodami)
        znaleziono = False
        msg_znak = msg.split(" ")
        msg_znak = list(filter(None, msg_znak))
        #print(msg_znak)
        try:
            znak_do_sprawdzenia = msg_znak[4]
        except (ValueError, IndexError):
            znak_do_sprawdzenia = ""
        #print(znak_do_sprawdzenia)
        if znak_do_sprawdzenia == ZNAK:
            znaleziono = True
        if msg and znaleziono:
            #print(msg)
            msg_bikon = msg.split(" ")
            msg_bikon = msg_bikon[2]
            msg_decybele = re.split("CW    | dB",msg)
            msg_decybele = msg_decybele[1]
            msg_decybele = msg_decybele.strip()

            #logging.info('main(): publikuje linie: %r', linia)
            print(msg)
            print("Bikon", msg_bikon)
            print("Siła", msg_decybele, "dB")
            #time.sleep(5.0)
            zapal_diode(pasek_z_diodami,msg_bikon,msg_decybele)
            print(pasek_z_diodami)
            plik = open(filename, "a")
            msg = msg + "\r\n"
            plik.write(msg)
            plik.close()
        else:
            #logging.info('main(): odrzucam linie: %r', linia)
            pass




if __name__ == "__main__":
    logging.basicConfig(level='DEBUG')
    main()
