import time
import re
import pyautogui


def play(sheet, mode):
    sheet = sheet.lower()

    x = 1

    if mode == "[]":
        sheet = sheet.split()
        a = len(sheet)
        for note in sheet:
            if note.startswith('['):
                note = list(note)
                note = note[1:-1]
                pyautogui.press(note)
                print(str(x) + " / " + str(a) + " " + str(note))
                time.sleep(0.4)
            else:
                pyautogui.press(note)
                print(str(x) + " / " + str(a) + " " + note)
                time.sleep(0.4)
            x += 1
    elif mode == "-":
        sheet = re.split("(\[\w\w\])", sheet)
        for line in sheet:
            if line.startswith('['):
                line = list(line)
                line = line[1:-1]
                pyautogui.press(line)
            else:
                for note in line:
                    if note == '-':
                        time.sleep(0.1)
                    elif note == ' ':
                        time.sleep(0.3)
                    else:
                        pyautogui.press(note)


if __name__ == '__main__':
    time.sleep(4)

    #example song sheet in "-" mode
    # play("[HN]----D----H----D----[JB]----D----J----D----V----D----H----[JD]----[QC]----[JD]----H----[JD]----["
    #      "HX]----N----V----[FN]"
    #      "----[DZ]----N----D----N----M----H----W----H----D----[WX]----N----[WS]----N----["
    #      "EZ]----N----D----N----M----D----W"
    #      "----[ED]----[RN]----[ED]----W----[ED]----[JC]----N----S----N--H--["
    #      "JC]----N----S----N----C----M----D----M----C----[HV]"
    #      "---------H---------[JB]----[AN]---------H----[JN]----[QZ]----[JA]----[HD]----[JN]----["
    #      "HV]----N----A----F----[DA]---------------------------------D----["
    #      "JC]----N----D----N----S----N----A----C----[NM]"
    #      "---------J----Q----[RD]----E----[JC]----Q----[JN]-------N--N--N----N--[HM]--M----M--M--M----M----["
    #      "DA]--A----A--A--A"
    #      "----A--[QS]--S----S--[WS]--S----S----[EV]--N--M--N--D--N--M--W-E-[JV]--N--M--N--D--N--M--H-J----["
    #      "DX]--N--M--N--D--N"
    #      "--M--S-D-[MC]---------[NC]----N-------------------H-------------------H", mode="-")

    #example song sheet in "[]" mode
    # play("N [AN] S [DN] H [GN] F [DN] [AV] D [BM] S [VN] C"
    #      "B [NC] [DFG] [FDS] J [GC] [DG] [HDG] [HD] [SB] N G [DC]"
    #      "N [AN] S [DN] H [GN] F [DN] [AN] [DG] [DH]"
    #      "[VHQ] [JB] [GD] [VHE] [JB] G [HV] [JQ] [JB] H [JQW] [JE]"
    #      "[DHJ] [QNAD] [JH] [GBM] [DS] [SV] [AG] [DZC] [VN] [MA] [SC] [BS] [FZ] [DS] [DM]"
    #      "[DHJ] [QNAD] [JQ] [WBM] [QW] [RVN] [EW] [QZC] [QV] E [JB] [QJ] [HNAD]"
    #      "[DHJ] [QNAD] [JH] [GBM] [DS] [SV] [AG] [DZC] [VN] [MA] [SC] [BS] [FZ] [DS] [DM]"
    #      "[DHJ] [QNAD] [JQ] [WBM] [QW] [RVN] [EW] [QZC] [QV] E [JB] [QJ] [HNAD]", mode="[]")