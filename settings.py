class Settings:
    def __init__(self):
        """ Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800    
        self.bg_color = (255, 255, 255)

        self.ship_speed = 1.5
        self.ship_limit = 2
# Bullet settings - dark grey bullets that a re 3 pixels wide and 15 pixels high. Bullets travel slower than the ship.
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left.
        #self.fleet_direction = 1

        #how fast the aliens will speed up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change during game"""
        self.ship_speed = 1.5
        self.bullte_speed = 1.5
        self.alien_speed = 1.0

        self.fleet_direction = 1

        #scoring
        self.alien_points = 50
        
    
    def increase_speed(self):
        """Increase speed of aliens"""
        self.ship_speed *= self.speedup_scale 
        self.bullet_speed *=self.speedup_scale
        self.alien_speed *=self.speedup_scale






    
    

       

