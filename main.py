from xlsx import Export2XLSX
import ui_main
import time
import cv2


if __name__ == '__main__':
    start = time.time()
    # work = Export2XLSX('./tables/biyesheji.png', verbose='vv')
    # work.ocr_process()
    # work.export_to_xlsx()
    end = time.time()
    print("time: " + str(end - start))
    ui_main.start_ui()
