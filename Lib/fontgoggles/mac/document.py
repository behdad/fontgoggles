import pathlib
import AppKit

from ..project import Project
from .mainWindow import FGMainWindowController
from ..font import sortedFontPathsAndNumbers


class FGDocument(AppKit.NSDocument):

    def __new__(cls):
        return cls.alloc().init()

    def init(self):
        self = super().init()
        self.project = Project()
        return self

    def addSourceFiles_(self, paths):
        paths = [pathlib.Path(path) for path in paths]
        sortKeys = ("familyName", "weight", "width", "italicAngle", "styleName", "suffix")
        for fontPath, fontNumber in sortedFontPathsAndNumbers(paths, sortKeys):
            self.project.addFont(fontPath, fontNumber)

    def makeWindowControllers(self):
        controller = FGMainWindowController(self.project)
        self.addWindowController_(controller)
