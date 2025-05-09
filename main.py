import cv2
import colorama
import kociemba as Cube
import numpy as np
import time


Res = colorama.Fore.RESET
Kır = colorama.Fore.RED
Yesil = colorama.Fore.GREEN
Gri = colorama.Fore.LIGHTBLACK_EX
Mor = colorama.Fore.MAGENTA
colorama.init()
print(rf"{Kır}  	 _________    _______            _________    _______             ___ ___ ___     ")
print(rf"{Gri}	| ________|  |_______|          | ________|  |_______|           |   |   |   |    ")
print(rf"{Kır}	| |_____     | |_____    ___    | |_____     | |_____            |_A_|_L_|_I_|    ")
print(rf"{Gri}	|  _____|    |_____  |  |___|   |  _____|    |_____  |           |   |   |   |    ")
print(rf"{Kır}	| |_______    _____| |          | |_______    _____| |           |C_A|_N_|E_R|    ")
print(rf"{Gri}	|_________|  |_______|          |_________|  |_______|           |   |   |   |   ")
print(rf"{Kır}                                                                 	 |___|___|___|   ")
print(rf"{Gri}                               _________     _________   _________          ", end='\n')
print(rf"{Kır}                              |  ____  /    |   ___   |  |__  ___|   ")
print(rf"{Kır}                              | |____| \    |  |   |  |     | |      ")
print(rf"{Gri}                              |  _____  |   |  |   |  |     | |         ")
print(rf"{Kır}                              | |_____| <   |  |___|  |     | |         ")
print(rf"{Gri}                              |_________|   |_________|     |_|         ")

time.sleep(2)
""

state = {""
    'yukari_yuz': ['beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', ],
    'sag_yuz': ['beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', ],
    'on_yuz': ['beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', ],
    'asag_yuzi_yuz': ['beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', ],
    'sol_yuz': ['beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', ],
    'arka_yuz': ['beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', 'beyaz', ]
}

sign_conv = {
    'Sarı': 'D',
    'Gırmızı': 'R',
    'Yesil': 'F',
    'Beyaz': 'U',
    'Mavi': 'B',
    'Turuncu': 'L'
}

color = {
    'gırmızı': (0, 0, 255),
    'turuncu': (0, 165, 255),
    'mavi': (255, 0, 0),
    'yesil': (0, 255, 0),
    'beyaz': (255, 255, 255),
    'sari': (0, 255, 255)
}

stickers = {
    'main': [
        [200, 120], [300, 120], [400, 120],
        [200, 220], [300, 220], [400, 220],
        [200, 320], [300, 320], [400, 320]
    ],
    'son_form': [
        [20, 20], [54, 20], [88, 20],
        [20, 54], [54, 54], [88, 54],
        [20, 88], [54, 88], [88, 88]
    ],
    'onizleme': [
        [20, 130], [54, 130], [88, 130],
        [20, 164], [54, 164], [88, 164],
        [20, 198], [54, 198], [88, 198]
    ],
    'sol_yuz': [
        [50, 280], [94, 280], [138, 280],
        [50, 324], [94, 324], [138, 324],
        [50, 368], [94, 368], [138, 368]
    ],
    'on_yuz': [
        [188, 280], [232, 280], [276, 280],
        [188, 324], [232, 324], [276, 324],
        [188, 368], [232, 368], [276, 368]
    ],
    'sag_yuz': [
        [326, 280], [370, 280], [414, 280],
        [326, 324], [370, 324], [414, 324],
        [326, 368], [370, 368], [414, 368]
    ],
    'yukari_yuz': [
        [188, 128], [232, 128], [276, 128],
        [188, 172], [232, 172], [276, 172],
        [188, 216], [232, 216], [276, 216]
    ],
    'asag_yuzi_yuz': [
        [188, 434], [232, 434], [276, 434],
        [188, 478], [232, 478], [276, 478],
        [188, 522], [232, 522], [276, 522]
    ],
    'arka_yuz': [
        [464, 280], [508, 280], [552, 280],
        [464, 324], [508, 324], [552, 324],
        [464, 368], [508, 368], [552, 368]
    ],
}

font = cv2.FONT_HERSHEY_SIMPLEX
textPoints = {
    'yukari_yuz': [['U', 242, 202], ['W', (255, 255, 255), 260, 208]],
    'sag_yuz': [['R', 380, 354], ['R', (0, 0, 255), 398, 360]],
    'on_yuz': [['F', 242, 354], ['G', (0, 255, 0), 260, 360]],
    'asag_yuzi_yuz': [['D', 242, 508], ['Y', (0, 255, 255), 260, 514]],
    'sol_yuz': [['L', 104, 354], ['O', (0, 165, 255), 122, 360]],
    'arka_yuz': [['B', 518, 354], ['B', (255, 0, 0), 536, 360]],
}

check_state = []
sol_yuzution = []
sol_yuzved = False

cap = cv2.VideoCapture(0)
cv2.namedWindow('canli')


def rotate(side):
    main = state[side]
    on_yuz = state['on_yuz']
    sol_yuz = state['sol_yuz']
    sag_yuz = state['sag_yuz']
    yukari_yuz = state['yukari_yuz']
    asag_yuzi_yuz = state['asag_yuzi_yuz']
    arka_yuz = state['arka_yuz']

    if side == 'on_yuz':
        sol_yuz[2], sol_yuz[5], sol_yuz[8], yukari_yuz[6], yukari_yuz[7], yukari_yuz[8], sag_yuz[0], sag_yuz[3], sag_yuz[6], asag_yuzi_yuz[0], asag_yuzi_yuz[1], asag_yuzi_yuz[2] = asag_yuzi_yuz[
            0], asag_yuzi_yuz[1], asag_yuzi_yuz[2], sol_yuz[8], sol_yuz[5], sol_yuz[2], yukari_yuz[6], yukari_yuz[7], yukari_yuz[8], sag_yuz[6], sag_yuz[3], sag_yuz[0]
    elif side == 'yukari_yuz':
        sol_yuz[0], sol_yuz[1], sol_yuz[2], arka_yuz[0], arka_yuz[1], arka_yuz[2], sag_yuz[0], sag_yuz[1], sag_yuz[2], on_yuz[0], on_yuz[1], \
        on_yuz[2] = on_yuz[0], on_yuz[1], on_yuz[2], sol_yuz[0], sol_yuz[1], sol_yuz[2], arka_yuz[0], arka_yuz[1], arka_yuz[2], sag_yuz[0], \
        sag_yuz[1], sag_yuz[2]
    elif side == 'asag_yuzi_yuz':
        sol_yuz[6], sol_yuz[7], sol_yuz[8], arka_yuz[6], arka_yuz[7], arka_yuz[8], sag_yuz[6], sag_yuz[7], sag_yuz[8], on_yuz[6], on_yuz[7], \
        on_yuz[8] = arka_yuz[6], arka_yuz[7], arka_yuz[8], sag_yuz[6], sag_yuz[7], sag_yuz[8], on_yuz[6], on_yuz[7], on_yuz[8], sol_yuz[6], \
        sol_yuz[7], sol_yuz[8]
    elif side == 'arka_yuz':
        sol_yuz[0], sol_yuz[3], sol_yuz[6], yukari_yuz[0], yukari_yuz[1], yukari_yuz[2], sag_yuz[2], sag_yuz[5], sag_yuz[8], asag_yuzi_yuz[6], asag_yuzi_yuz[7], asag_yuzi_yuz[8] = yukari_yuz[2], \
        yukari_yuz[1], yukari_yuz[0], sag_yuz[2], sag_yuz[5], sag_yuz[8], asag_yuzi_yuz[8], asag_yuzi_yuz[7], asag_yuzi_yuz[6], sol_yuz[0], sol_yuz[3], sol_yuz[6]
    elif side == 'sol_yuz':
        on_yuz[0], on_yuz[3], on_yuz[6], asag_yuzi_yuz[0], asag_yuzi_yuz[3], asag_yuzi_yuz[6], arka_yuz[2], arka_yuz[5], arka_yuz[8], yukari_yuz[0], yukari_yuz[3], yukari_yuz[6] = yukari_yuz[
            0], yukari_yuz[3], yukari_yuz[6], on_yuz[0], on_yuz[3], on_yuz[6], asag_yuzi_yuz[6], asag_yuzi_yuz[3], asag_yuzi_yuz[0], arka_yuz[8], arka_yuz[5], arka_yuz[2]
    elif side == 'sag_yuz':
        on_yuz[2], on_yuz[5], on_yuz[8], asag_yuzi_yuz[2], asag_yuzi_yuz[5], asag_yuzi_yuz[8], arka_yuz[0], arka_yuz[3], arka_yuz[6], yukari_yuz[2], yukari_yuz[5], yukari_yuz[8] = \
        asag_yuzi_yuz[2], asag_yuzi_yuz[5], asag_yuzi_yuz[8], arka_yuz[6], arka_yuz[3], arka_yuz[0], yukari_yuz[8], yukari_yuz[5], yukari_yuz[2], on_yuz[2], on_yuz[5], on_yuz[8]

    main[0], main[1], main[2], main[3], main[4], main[5], main[6], main[7], main[8] = main[6], main[3], main[0], main[
        7], main[4], main[1], main[8], main[5], main[2]


def revrotate(side):
    main = state[side]
    on_yuz = state['on_yuz']
    sol_yuz = state['sol_yuz']
    sag_yuz = state['sag_yuz']
    yukari_yuz = state['yukari_yuz']
    asag_yuzi_yuz = state['asag_yuzi_yuz']
    arka_yuz = state['arka_yuz']

    if side == 'on_yuz':
        sol_yuz[2], sol_yuz[5], sol_yuz[8], yukari_yuz[6], yukari_yuz[7], yukari_yuz[8], sag_yuz[0], sag_yuz[3], sag_yuz[6], asag_yuzi_yuz[0], asag_yuzi_yuz[1], asag_yuzi_yuz[2] = yukari_yuz[8], \
        yukari_yuz[7], yukari_yuz[6], sag_yuz[0], sag_yuz[3], sag_yuz[6], asag_yuzi_yuz[2], asag_yuzi_yuz[1], asag_yuzi_yuz[0], sol_yuz[2], sol_yuz[5], sol_yuz[8]
    elif side == 'yukari_yuz':
        sol_yuz[0], sol_yuz[1], sol_yuz[2], arka_yuz[0], arka_yuz[1], arka_yuz[2], sag_yuz[0], sag_yuz[1], sag_yuz[2], on_yuz[0], on_yuz[1], \
        on_yuz[2] = arka_yuz[0], arka_yuz[1], arka_yuz[2], sag_yuz[0], sag_yuz[1], sag_yuz[2], on_yuz[0], on_yuz[1], on_yuz[2], sol_yuz[0], \
        sol_yuz[1], sol_yuz[2]
    elif side == 'asag_yuzi_yuz':
        sol_yuz[6], sol_yuz[7], sol_yuz[8], arka_yuz[6], arka_yuz[7], arka_yuz[8], sag_yuz[6], sag_yuz[7], sag_yuz[8], on_yuz[6], on_yuz[7], \
        on_yuz[8] = on_yuz[6], on_yuz[7], on_yuz[8], sol_yuz[6], sol_yuz[7], sol_yuz[8], arka_yuz[6], arka_yuz[7], arka_yuz[8], sag_yuz[6], \
        sag_yuz[7], sag_yuz[8]
    elif side == 'arka_yuz':
        sol_yuz[0], sol_yuz[3], sol_yuz[6], yukari_yuz[0], yukari_yuz[1], yukari_yuz[2], sag_yuz[2], sag_yuz[5], sag_yuz[8], asag_yuzi_yuz[6], asag_yuzi_yuz[7], asag_yuzi_yuz[8] = asag_yuzi_yuz[
            6], asag_yuzi_yuz[7], asag_yuzi_yuz[8], sol_yuz[6], sol_yuz[3], sol_yuz[0], yukari_yuz[0], yukari_yuz[1], yukari_yuz[2], sag_yuz[8], sag_yuz[5], sag_yuz[2]
    elif side == 'sol_yuz':
        on_yuz[0], on_yuz[3], on_yuz[6], asag_yuzi_yuz[0], asag_yuzi_yuz[3], asag_yuzi_yuz[6], arka_yuz[2], arka_yuz[5], arka_yuz[8], yukari_yuz[0], yukari_yuz[3], yukari_yuz[6] = \
        asag_yuzi_yuz[0], asag_yuzi_yuz[3], asag_yuzi_yuz[6], arka_yuz[8], arka_yuz[5], arka_yuz[2], yukari_yuz[0], yukari_yuz[3], yukari_yuz[6], on_yuz[0], on_yuz[3], on_yuz[6]
    elif side == 'sag_yuz':
        on_yuz[2], on_yuz[5], on_yuz[8], asag_yuzi_yuz[2], asag_yuzi_yuz[5], asag_yuzi_yuz[8], arka_yuz[0], arka_yuz[3], arka_yuz[6], yukari_yuz[2], yukari_yuz[5], yukari_yuz[8] = yukari_yuz[
            2], yukari_yuz[5], yukari_yuz[8], on_yuz[2], on_yuz[5], on_yuz[8], asag_yuzi_yuz[8], asag_yuzi_yuz[5], asag_yuzi_yuz[2], arka_yuz[6], arka_yuz[3], arka_yuz[0]

    main[0], main[1], main[2], main[3], main[4], main[5], main[6], main[7], main[8] = main[2], main[5], main[8], main[
        1], main[4], main[7], main[0], main[3], main[6]


def sol_yuzve(state):
    raw = ''
    for i in state:
        for j in state[i]:
            raw += sign_conv[j]
    print("answer:", Cube.sol_yuzve(raw))
    return Cube.sol_yuzve(raw)


def color_detect(h, s, v):
    # print(h,s,v)
    if h < 5 and s > 5:
        return 'gırmızı'
    elif h < 10 and h >= 3:
        return 'turuncu'
    elif h <= 25 and h > 10:
        return 'sari'
    elif h >= 70 and h <= 85 and s > 100 and v < 180:
        return 'yesil'
    elif h <= 130 and s > 70:
        return 'mavi'
    elif h <= 100 and s < 10 and v < 200:
        return 'beyaz'

    return 'beyaz'


def draw_stickers(frame, stickers, name):
    for x, y in stickers[name]:
        cv2.rectangle(frame, (x, y), (x + 30, y + 30), (255, 255, 255), 2)


def draw_onizleme_stickers(frame, stickers):
    stick = ['on_yuz', 'arka_yuz', 'sol_yuz', 'sag_yuz', 'yukari_yuz', 'asag_yuzi_yuz']
    for name in stick:
        for x, y in stickers[name]:
            cv2.rectangle(frame, (x, y), (x + 40, y + 40), (255, 255, 255), 2)


def texton_onizleme_stickers(frame, stickers):
    stick = ['on_yuz', 'arka_yuz', 'sol_yuz', 'sag_yuz', 'yukari_yuz', 'asag_yuzi_yuz']
    for name in stick:
        for x, y in stickers[name]:
            sym, x1, y1 = textPoints[name][0][0], textPoints[name][0][1], textPoints[name][0][2]
            cv2.putText(onizleme, sym, (x1, y1), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
            sym, col, x1, y1 = textPoints[name][1][0], textPoints[name][1][1], textPoints[name][1][2], \
            textPoints[name][1][3]
            cv2.putText(onizleme, sym, (x1, y1), font, 0.5, col, 1, cv2.LINE_AA)


def fill_stickers(frame, stickers, sides):
    for side, colors in sides.items():
        num = 0
        for x, y in stickers[side]:
            cv2.rectangle(frame, (x, y), (x + 40, y + 40), color[colors[num]], -1)
            num += 1


def process(operation):
    replace = {
        "F": [rotate, 'on_yuz'],
        "F2": [rotate, 'on_yuz', 'on_yuz'],
        "F'": [revrotate, 'on_yuz'],
        "U": [rotate, 'yukari_yuz'],
        "U2": [rotate, 'yukari_yuz', 'yukari_yuz'],
        "U'": [revrotate, 'yukari_yuz'],
        "L": [rotate, 'sol_yuz'],
        "L2": [rotate, 'sol_yuz', 'sol_yuz'],
        "L'": [revrotate, 'sol_yuz'],
        "R": [rotate, 'sag_yuz'],
        "R2": [rotate, 'sag_yuz', 'sag_yuz'],
        "R'": [revrotate, 'sag_yuz'],
        "D": [rotate, 'asag_yuzi_yuz'],
        "D2": [rotate, 'asag_yuzi_yuz', 'asag_yuzi_yuz'],
        "D'": [revrotate, 'asag_yuzi_yuz'],
        "B": [rotate, 'arka_yuz'],
        "B2": [rotate, 'arka_yuz', 'arka_yuz'],
        "B'": [revrotate, 'arka_yuz']
    }
    a = 0
    for i in operation:
        for j in range(len(replace[i]) - 1):
            replace[i][0](replace[i][j + 1])
        cv2.putText(onizleme, i, (700, a + 50), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
        fill_stickers(onizleme, stickers, state)
        sol_yuzution.append(onizleme)
        cv2.imshow('sol_yuzution', onizleme)
        cv2.waitKey()
        cv2.putText(onizleme, i, (700, 50), font, 1, (0, 0, 0), 1, cv2.LINE_AA)


if __name__ == '__main__':

    onizleme = np.zeros((700, 800, 3), np.uint8)

    while True:
        hsv = []
        son_form_state = []
        ret, img = cap.read()
        # img=cv2.flip(img,1)
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = np.zeros(frame.shape, dtype=np.uint8)

        draw_stickers(img, stickers, 'main')
        draw_stickers(img, stickers, 'son_form')
        draw_onizleme_stickers(onizleme, stickers)
        fill_stickers(onizleme, stickers, state)
        texton_onizleme_stickers(onizleme, stickers)

        for i in range(9):
            hsv.append(frame[stickers['main'][i][1] + 10][stickers['main'][i][0] + 10])

        a = 0
        for x, y in stickers['son_form']:
            color_name = color_detect(hsv[a][0], hsv[a][1], hsv[a][2])
            cv2.rectangle(img, (x, y), (x + 30, y + 30), color[color_name], -1)
            a += 1
            son_form_state.append(color_name)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        elif k == ord('u'):
            state['yukari_yuz'] = son_form_state
            check_state.append('u')
        elif k == ord('r'):
            check_state.append('r')
            state['sag_yuz'] = son_form_state
        elif k == ord('l'):
            check_state.append('l')
            state['sol_yuz'] = son_form_state
        elif k == ord('d'):
            check_state.append('d')
            state['asag_yuzi_yuz'] = son_form_state
        elif k == ord('f'):
            check_state.append('f')
            state['on_yuz'] = son_form_state
        elif k == ord('b'):
            check_state.append('b')
            state['arka_yuz'] = son_form_state
        elif k == ord('\r'):
            # process(["R","R'"])
            if len(set(check_state)) == 6:
                try:
                    sol_yuzved = sol_yuzve(state)
                    if sol_yuzved:
                        operation = sol_yuzved.split(' ')
                        process(operation)
                except:
                    print(
                        "Algılamada hata meydana geldi. Sırayı takip etmediniz ya da bazı renkler algılanmadı. Tekrar deneyiniz.")
            else:
                print("Tüm yüzler taranmadı hangi , Hangi yüzün taranacağını bulmak için -canli- penceresini kontrol edin.")
                print("sol yüzü tarayın:", 6 - len(set(check_state)))
        cv2.imshow('onizleme', onizleme)
        cv2.imshow('canli', img[0:500, 0:500])

    cv2.destroyAllWindows()