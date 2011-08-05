'''
Created on 24/06/2011

@author: mikel
'''
import xbmcgui
import views
import views.home


class MainWindow(xbmcgui.WindowXML): 
    __file = None
    __script_path = None
    __skin_dir = None
    __view_manager = None
    
    
    def __init__(self, file, script_path, skin_dir):
        self.__file = file
        self.__script_path = script_path
        self.__skin_dir = skin_dir
        self.__view_manager = views.ViewManager(self)


    def onInit(self ):
        """
        c = self.getControl(1100)
        img = "http://1.bp.blogspot.com/_4BO-nX-j9B0/S9cS3ZGCJrI/AAAAAAAAST0/8MIRPkvxImM/s640/0720cbb017618f83601b955af55b99c0%5B1%5D.jpg"
        c.addItem(xbmcgui.ListItem('pg1. label', 'pg1. label2', img, img))
        
        img = "http://1.bp.blogspot.com/_kCfQZm97tjs/TIQfesq0EtI/AAAAAAAACgA/0Yd9xOUDWhg/s1600/172760.jpg"
        c.addItem(xbmcgui.ListItem('pg2. label', 'pg2. label2', img, img))
        """
        """
        c = self.getControl(2000)
        c.addItem(xbmcgui.ListItem('Item #1', ''))
        c.addItem(xbmcgui.ListItem('Item #2', ''))
        c.addItem(xbmcgui.ListItem('Somewhat Long Artist Name', ''))
        c.addItem(xbmcgui.ListItem('Item #4', ''))
        c.addItem(xbmcgui.ListItem('Item #5', 'active'))
        c.addItem(xbmcgui.ListItem('Item #6', ''))
        c.addItem(xbmcgui.ListItem('Item #7', ''))
        c.addItem(xbmcgui.ListItem('Item #8', ''))
        """
        #Start with the home view by default
        home_view = views.home.HomeMenuView()
        self.__view_manager.add_view(home_view)
        
    
    #def onAction(self, action):
    #    pass
    
    def onClick(self, controlID):
        #print "click (%d)!" % controlID
        #c = self.getControl(controlID)
        #si = c.getSelectedItem()
        #print "%s, %s" % (si.getLabel(), si.getLabel2())
        if controlID == 10:
            loginwin = dialogs.LoginWindow(
                "login-window.xml", self.__script_path, self.__skin_dir
            )
            loginwin.doModal()
        
        elif controlID == 11:
            loginwin = dialogs.LoginWindow(
                "album-info-dialog.xml", self.__script_path, self.__skin_dir
            )
            loginwin.doModal()
        
        elif controlID == 14:
            c = self.getControl(13)
            c.setVisible(False)
        
    
    def onFocus(self, controlID):
        pass