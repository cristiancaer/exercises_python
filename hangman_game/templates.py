from models.hanger_man_drawing import HangManDrawing, decorate_text
class HangManRender:
    drawing=HangManDrawing()
    def __init__(self,level: str='easy') -> None:
        """ the game has three class of levels
            :param level= 'easy' or 'medium' or 'high'
        """
        self.initialize()
        self.level=level
    def initialize(self):
        self.render_buffer=self.drawing.MAP_BACKGROUND
        self.render_buffer=self.drawing.add_tramp(self.render_buffer)
        self.levels={'low':[[i] for i in range(7)],# 6 step until game over
                'medium':[[0,1],[2,3],[4,5],[6]],# 4 steps until game over
                'high':[[0,1,],[2,3,4,5],[6]],# 3 steps until game over
                }

    def add_render(self):
        game_over=False
        #steps to be plotted according to level
        list_steps=self.levels.get(self.level)
        if len(list_steps)>0:# the game is over if there are no more steps to plot
            # get and del steps to be plotted, the list has just pending steps to be plotted
            steps_to_draw=list_steps.pop(0)
            # update step list to be ploted
            self.levels[self.level]=list_steps
            #each step has the index of the drawing to be plotted
            for index_drawing in steps_to_draw:
                # we must del  the closed trap to draw the openned trap
                if index_drawing==6:
                    self.render_buffer=self.drawing.del_trap(self.render_buffer)
                drawings=self.drawing.get_element(index_drawing)
                # each element has 2 cordenats to specify it's position and a character to be ploteed  
                for x,y,char in drawings:
                    self.render_buffer[x][y]=char
            
        else:
            game_over=True
        drawing=[]
        #join elements by row
        for row in self.render_buffer:
            drawing.append(''.join(row))
        #join rows
        drawing='\n'.join(drawing)
        return drawing,game_over
    def set_word_game(self,word:str):
        self.word_game=[char for char in word]
        self.word_buffer=['_ ' for _ in range(len(word))]
    def add_character_render(self,char:str):
        ret=False
        if (len(char)==1 )and (char in self.word_game):
            ret=True
            for i,char_in_word in enumerate(self.word_game):
                if char==char_in_word:
                    self.word_buffer[i]=char
                
        output=decorate_text(''.join(self.word_buffer))

        return ret,output

if __name__=='__main__':
    render_easy=HangManRender('low')
    render_medium=HangManRender('medium')
    render_high=HangManRender('high')
    game=render_high
    game.set_word_game('lion')
    ret,word=game.add_character_render('a')
    print(word)
    ret,word=game.add_character_render('i')
    print(word)
    while True:
        draw,game_over=game.add_render()
        if game_over:
            break
        print(draw)
    # print('a')