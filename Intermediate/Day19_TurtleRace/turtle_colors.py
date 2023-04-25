class TurtleColors:
    """List of the available turtle colors"""
    
    
    def __init__(self):
        """List of colors for the turtle racers"""
        
        
        self.colors_list = ["red",
                       "green",
                       "blue",
                       "orange",
                       "cyan",
                       "purple",]


    def get_colors(self):
        """Returns all the available colors of Turtles to pick from"""
        
        
        options = ""
        for color in self.colors_list:
            options += f"{color}/"
        return options[:-1]