import threading
from templates import *
from threading import Thread
class HangManGame(Thread):
    is_running=True
    render=HangManRender()
    PRINCIPAL_MENU=['Play','Exit']
    PLAY_OPTIONS=['Easy','Medium,','High','back']
    IN_GAME_MENU=['Solve, Start new Game','GO to principal menu']




    