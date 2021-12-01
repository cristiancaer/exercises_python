class HangManDrawing:
    BACKGROUND = """
    **  **    ***    **   **  *******   **      **    ***    **   **  
    **  **   ** **   ***  **  **        ***    ***   ** **   ***  **  
    ******   *****   **** **  **  ***   ****  ****   *****   **** **  
    **  **  **   **  ** ****  **   **   ** **** **  **   **  ** ****  
    **  **  **   **  **  ***  *******   **  **  **  **   **  **  ***  
            ||                                   
            ||===================                                                      
            ||                                                      
            ||                                                      
            ||                                                      
            ||                                                      
            ||                                                      
            ||                                                      
            ||                                                       
            ||                                                      
            ||                                                        
            ||                                                       
            ||                                                      
            ======@         ============                             
            ||                         ||                              
            ||                         ||                              
            ||                         ||                               
            """
    MAP_BACKGROUND=[[char for char in row] for row in BACKGROUND.split('\n')]
    LIST_ELEMENTS=['HEAD','TORSO','LEFT_ARM','RIGHT_AMR','LEFT_LEG','RIGHT_LEG','TRAMP_OPENNED']
    ELEMENTS = {'HEAD':(
                (8, 23, '|',),
                (9, 23, '|',),
                (10, 22, '_',),
                (10, 23, '_',),
                (10, 24, '_',),
                (11, 20, '|',),
                (11, 22, '.',),
                (11, 24, '.',),
                (11, 26, '|',),

                (12, 21, '\\',),
                (12, 23, '_',),
                (12, 25, '/',),
            ),

            'TORSO' : (
                (13, 23, '|',),
                (13, 24, '|',),
                (14, 23, '|',),
                (14, 24, '|',),
                (15, 23, '|',),
                (15, 24, '|',),
                (16, 23, '|',),
                (16, 24, '|',),
            ),

            'LEFT_ARM' : (
                (14, 20, '=',),
                (14, 21, '=',),
                (14, 22, '=',),
            ),

            'RIGHT_AMR':(
                (14, 25, '=',),
                (14, 26, '=',),
                (14, 27, '=',),
            ),

            'LEFT_LEG':(
                (17, 22, '/',),
                (17, 23, '/',),
                (18, 21, '/',),
                (18, 22, '/',),
            ),

            'RIGHT_LEG': (
                (17, 24, '\\',),
                (17, 25, '\\',),
                (18, 25, '\\',),
                (18, 26, '\\',),
            ),
            
            'TRAMP_OPENNED':(
                (19, 19, '\\',),
                (19, 20, '\\',),
                (20, 20, '\\',),
                (20, 21, '\\',),
                (21, 21, '\\',),
                (21, 22, '\\',),
                (22, 22, '\\',),
                (22, 23, '\\',),
            )
    }
    TRAMP_CLOSED= (
                (19, 19, '=',),
                (19, 20, '=',),
                (19, 21, '=',),
                (19, 22, '=',),
                (19, 23, '=',),
                (19, 24, '=',),
                (19, 25, '=',),
                (19, 26, '=',),
                (19, 27, '=',),
            )
    def get_element(self, index_drawing:int):
        return self.ELEMENTS[self.LIST_ELEMENTS[index_drawing]]
    def add_tramp(self,draw_map):
        for x,y,char in self.TRAMP_CLOSED:
            draw_map[x][y]=char
        return draw_map
    def del_trap(self,draw_map:list):
        for x,y,_ in self.TRAMP_CLOSED:
            draw_map[x][y]=' '
        return draw_map
def decorate_text(text:str)->str:

    output=" "+"_"*(1+len(text))+'\n'
    output+='/'+"_"*(len(text))+"/|"+'\n'
    output+='|'+" "*(len(text))+"||"+'\n'
    output+="|"+text+"||"+'\n'
    output+='|'+"_"*(len(text))+'|/'+'\n'
    return output
if __name__=='__main__':
    text=decorate_text('word in game')
    print(text)
    draw=HangManDrawing()
    name=draw.LIST_ELEMENTS[0]
    print(draw.ELEMENTS[name])