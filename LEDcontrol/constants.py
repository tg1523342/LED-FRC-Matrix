class MatrixConstants:
     WIDTH = 64
     HEIGHT = 32
     PANEL_COUNT = 2
     BRIGHTNESS = 80


class GifConstants:
    # idenifies the files
     PATH = "LEDcontrol/media/gif/" # <-- This might change depending on where you put it.

     STARTUP = PATH + "startup.gif"
     IDLE = PATH + "idle.gif"
     BoyKisser = PATH + "BK1.gif"
     FeedMe = PATH + "feed me.gif"
     Yipee = PATH + "Yipeeeeeeeeeeeeeeee.gif"
     

class ImageConstants:
     PATH = "LEDcontrol/media/png/"

     LOADING = PATH + "loading.png"

     PROOT_PATH = "LEDcontrol/media/prootImg/"


class NetworkTableConstants:
     ROBOT_IP = "192.168.211.1"

     LED_DATA_TABLE = "LED Data"
     INDEX_TAB_NAME = "Shuffleboard/Index"
     SHOOTER_TAB_NAME = "Shuffleboard/Shooter"

     LED_INDEX_KEY = "LED Mode"
     IS_BALL_DETECTED_KEY = "Is Ball Detected"