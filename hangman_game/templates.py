from models.hanger_man_drawing import HangManDrawing
class HangManRender:
    drawing=HangManDrawing()
    def __init__(self,level) -> None:
        self.initialize()
        self.level=level
    def initialize(self):
        self.render_buffer=self.drawing.MAP_BACKGROUND
        self.render_buffer=self.drawing.add_tramp(self.render_buffer)
        self.levels={'low':[[i] for i in range(7)],
                'medium':[[0,1],[2,3],[4,5],[6]],
                'high':[[0,1,],[2,3,4,5],[6]],
                }

    def add_render(self):
        game_over=False
        list_steps=self.levels.get(self.level)
        if len(list_steps)>0:
            steps_to_draw=list_steps.pop(0)
            self.levels[self.level]=list_steps
            for index_drawing in steps_to_draw:
                if index_drawing==6:
                    self.render_buffer=self.drawing.del_trap(self.render_buffer)
                drawings=self.drawing.get_element(index_drawing)
                for x,y,char in drawings:
                    zx=len(self.render_buffer)
                    zy=len(self.render_buffer[x])
                    # print(self.render_buffer[x][y])
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

if __name__=='__main__':
    render_easy=HangManRender('low')
    render_medium=HangManRender('medium')
    render_high=HangManRender('high')
    game=render_high
    while True:
        draw,game_over=game.add_render()
        if game_over:
            break
        print(draw)
    # print('a')