import xbmc
import xbmcgui
from platform import machine

OS_MACHINE = machine()


class SkipIntro(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        if OS_MACHINE[0:5] == 'armv7':
            xbmcgui.WindowXMLDialog.__init__(self)
        else:
            xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

    def onInit(self):
        self.action_exitkeys_id = [10, 13]

    def onClick(self, controlID):
        introStart = int(xbmcgui.Window(10000).getProperty("NextUpNotification.introStart"))
        introLenght = int(xbmcgui.Window(10000).getProperty("NextUpNotification.introLenght"))
        xbmc.log('skip intro onclick: ' + str(controlID))

        if controlID == 6012:
            # skip inro selected by user
            xbmc.Player().seekTime(introStart+introLenght)
            self.close()

        pass