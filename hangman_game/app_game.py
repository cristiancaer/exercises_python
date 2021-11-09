from templates import *
def run():
    render=HangManRender()
    for i in render.list_render:
        print(i)

if __name__=='__main__':
    run()