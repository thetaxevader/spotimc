'''
Created on 12/07/2011

@author: mikel
'''


class ViewManager:
    __window = None
    __view_list = None
    __position = None
    
    
    def __init__(self, window):
        self.__window = window
        self.__view_list = []
        self.__position = -1
    
    
    def num_views(self):
        return len(self.__view_list)
    
    
    def position(self):
        return self.__position
    
    
    def has_next(self):
        return(
            self.num_views() > 0
            and self.position() < self.num_views() - 1
        )
    
    
    def next(self):
        #Fail if no next window
        if not self.has_next():
            raise IndexError("No more views available")
        
        #If there's one active
        if self.__position != -1:
            self.__view_list[self.__position].hide(self.__window)
        
        #Show the next one
        self.__position += 1
        self.__view_list[self.__position].show(self.__window)
    
    
    def has_previous(self):
        return self.__position > 0
    
    
    def previous(self):
        #Fail if no previous window
        if not self.has_previous():
            raise IndexError("No previous views available")
        
        #Hide current
        self.__view_list[self.__position].hide(self.__window)
        
        #Show previous
        self.__position -= 1
        self.__view_list[self.__position].show(self.__window)
    
    
    def add_view(self, view):
        #Remove all views that come next (if any)
        del self.__view_list[self.__position:]
        
        #Add the new one
        self.__view_list.append(view)
        
        #Go to the next view
        self.next()



class BaseView:
    def click(self, window, control_id):
        pass
    
    def show(self, window):
        pass
    
    def hide(self, window):
        pass
    
    #def get_control(self, window, control_id):
    #    pass
    
    def back(self, window):
        pass