from pathlib import Path

from modules._platform import get_platform
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from threads.downloader import Downloader
from threads.extractor import Extractor
from ui.update_window_ui import UpdateWindowUI
from windows.base_window import BaseWindow


class UpdateWindow(QMainWindow, BaseWindow, UpdateWindowUI):
    def __init__(self, parent, tag):
        super().__init__()
        self.setWindowTitle("Update")
        self.setWindowFlag(Qt.SubWindow)
        self.setupUi(self)

        self.parent = parent
        self.tag = tag

        self.download()

    def download(self):
        self.link = "https://github.com/DotBow/Blender-Launcher/releases/download/{0}/Blender_Launcher_{0}_{1}_x64.zip".format(
            self.tag, get_platform())
        self.thread = Downloader(self.parent.manager, self.link)
        self.thread.progress_changed.connect(self.set_progress_bar)
        self.thread.finished.connect(self.extract)
        self.thread.start()

        self.show()

    def extract(self, source):
        dist = Path.cwd().as_posix()
        self.thread = Extractor(self.parent.manager, source, dist)
        self.thread.progress_changed.connect(self.set_progress_bar)
        self.thread.start()