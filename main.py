from PyQt6.QtWidgets import *
from PyQt6 import uic
import os
import cv2
class MyGUI(QMainWindow):
    folderName = ""
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("./UI/form.ui",self)
        self.show()

        # event handlers
        self.btnBrowse.clicked.connect(self.get_file_location)
        self.btnScan.clicked.connect(self.scan)

    def get_file_location(self):
        dialog = QFileDialog()
        self.folderName = dialog.getExistingDirectory(None, "Select Folder")
        self.txtLocation.insertPlainText(self.folderName)


    def scan(self):
        self.lstLog.addItem(f"selected folder : {str(self.folderName)}")
        img_dirs = []
        for entry in os.scandir(str(self.folderName)):
            if entry.is_dir():
                img_dirs.append(entry.path)
        print(img_dirs)
        for img_dir in img_dirs:
            count = 1
            self.lstLog.addItem(f"scanning the folder : {img_dir}")
            for entry in os.scandir(img_dir):
                try:
                    img = cv2.imread(str(entry.path))
                    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                except:
                    self.lstLog.addItem(f"error in file : {str(entry.path)}")
                    with open("errors.log", "a") as file:
                        file.writelines(f"error in file : {str(entry.path)}\n")
                    
                    continue
        self.lstLog.addItem(f"processed successfully")
        self.lstLog.addItem(f"errors.log generated")



def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

if __name__ == '__main__':
    main()

