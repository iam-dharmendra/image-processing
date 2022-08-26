
from tkinter import *
from tkinter import ttk
import cv2
import pygame, sys
from PIL import Image
import os
import glob
import sys
import tkinter.font as tkFont



pygame.init()
count=0
clock = pygame.time.Clock()

def displayImage(screen, px, topleft, prior,text):
    # ensure that the rect always has positive width, height
    x, y = topleft
    width =  pygame.mouse.get_pos()[0] - topleft[0]
    height = pygame.mouse.get_pos()[1] - topleft[1] 
    if width < 0:
        x += width
        width = abs(width)
    if height < 0:
        y += height
        height = abs(height)

    # eliminate redundant drawing cycles (when mouse isn't moving)
    current = x, y, width, height
    if not (width and height):
        return current
    if current == prior:
        return current

    # draw transparent box and blit it onto canvas


    # top1=px.get_rect().top+45
    # width1=px.get_rect().width
    # left1=px.get_rect().left
    # height1=px.get_rect().height

    # print(im.get_rect())
   
    screen.blit(px,px.get_rect())
    # screen.blit(px,(left1,top1,width1,height1))
    im = pygame.Surface((width, height))
    im.fill((128, 128, 128))

    # top2=im.get_rect().top+15
    # width2=im.get_rect().width
    # left2=im.get_rect().left
    # height2=im.get_rect().height

    # print(im.get_rect())
    pygame.draw.rect(im, (32, 32, 32), im.get_rect(), 1)
   
   
    # pygame.draw.rect(im, (32, 32, 32),(left2,top2,width2,height2), 1)
    im.set_alpha(128)
    
    screen.blit(im,(x, y))
    screen.blit(text,(710,720))
    pygame.display.flip()
    pygame.display.update()

    # return current box extents
    return (x, y, width, height)

# for selcting rectangle area in jpg file
def setup(path,name):
    
    # Use the second argument or (flag value) zero
    # that specifies the image is to be read in grayscale mode
    img = cv2.imread(path)
    ret, thresh1 = cv2.threshold(img, 185, 255, cv2.THRESH_BINARY)
    
    px = pygame.surfarray.make_surface(thresh1)
    px = pygame.transform.rotate(px,270)
    px = pygame.transform.flip(px,True,False)
  
    print(px.get_rect(),'kkkkkkkkkkkkk')
    # screen = pygame.display.set_mode( px.get_rect()[2:])
    screen = pygame.display.set_mode((1500,800))
    
    
    
    fontObj = pygame.font.SysFont('Lohit Devanagari', 55)
    text =fontObj.render("  "+name+"  ", True,"blue",'#D3D3D3')

    
    # pygame.display.flip()
    # middle=px.get_rect(center=screen.get_rect().center)

    # top=px.get_rect().top+25
    # left=px.get_rect().left
    # width=px.get_rect().width
    # height=px.get_rect().height


    # screen.blit(px,(left,top,width,height))
    screen.blit(px,(px.get_rect()))
    pygame.display.flip()
    screen.blit(text,(710,720))
    # screen.fill(10)
    pygame.display.update()
  
    return screen,px,text

def mainLoop1(screen,px,count,text):
    topleft = bottomright = prior = None
    n=0

    while n!=1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                
                if event.__dict__['button']==4: 
                    pass
                elif event.__dict__['button']==5:
                    pass
                elif not topleft:
                    topleft = event.pos    
                else:
                    bottomright = event.pos
                    n=1
            if event.type==pygame.KEYDOWN:

                # list_of_files = glob.glob('/home/user/Music/dharmendra/image_processing/images/'+'/*')

                list_of_files = glob.glob(f'{os.getcwd()}/Menuscript//'+'/*')
                if event.key ==pygame.K_LEFT:
                
                    if count >=1 and count <= len(list_of_files) :
                        print('left')
                        count-=1 
                        topleft = (0,0)
                        bottomright = (0,0)
                        n=1
                      
                if event.key ==pygame.K_RIGHT: 
                    if count >=0 and count <(len(list_of_files)-1) : 
                        print('right')
                        count+=1
                        topleft = (0,0)
                        bottomright = (0,0)
                        n=1 
                if (event.key == pygame.K_ESCAPE) or (event.type == pygame.QUIT): 
                    sys.exit()
                   
        if topleft:
                prior = displayImage(screen, px, topleft, prior,text)
               
    return (topleft + bottomright+(count,0))

# def make_folder(name):
#     path='/home/user/Music/dharmendra/image_processing/'+name    
#     os.mkdir(path)

def make_folder(name):
    print(name)
    path= os.path.join(os.getcwd(), name)
    if not os.path.exists(path):
        os.mkdir(path)

#  for making dropdown #
def slect_character():

    #Create an instance of tkinter frame
    win= Tk()
    #Define the size of window or frame
    win.geometry("815x450")
    #Set the Menu initially
    menu= StringVar(win)
    menu.set("Select Any Charcter")
    
# Getting data from AllChar.txt
    with open("AllChar.txt") as file:
        data = file.read()
   


    #Create a dropdown Menu

    drop=ttk.Combobox(win, textvariable=menu,values=data,font=("Helvetica",15))
    # drop= OptionMenu(win, menu,"A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

    bigfont = tkFont.Font(family="Helvetica",size=20)
    win.option_add("*TCombobox*Listbox*Font", bigfont)
    drop.pack(padx=20, pady=10)
    

    def out():
        sys.exit()

    def disable_event():
        pass    
    
    exit_button = Button(win, text="exit", command=out,fg='white',background='red',font=50)
    exit_button.place(x=750,y=5)

    ok_button = Button(win, text="OK", command=win.destroy,fg='blue',background="white",font=("Helvetica",15))
    ok_button.place(x=350,y=380)
    # ok_button.pack(side=BOTTOM)
    win.protocol("WM_DELETE_WINDOW", disable_event)
    win.resizable(False,False)
    win.mainloop()    
    return menu.get()
       


if __name__ == "__main__":

    # input_loc= glob.glob('/home/user/Music/dharmendra/image_processing/images/'+'/*')

    input_loc= glob.glob(f'{os.getcwd()}//Menuscript'+'/*')

    counter=1
    count=0

    name=slect_character()
   
    while True:
        if name=='Select Any Charcter':
            name=slect_character()
            
        elif name!='Select Any Charcter':         
            # if os.path.isdir('/home/user/Music/dharmendra/image_processing'+'/'+str(name)+'/'):         
            if os.path.isdir(f'{os.getcwd()}//'+'/'+str(name)+'/'):    
                try:
                    # list_of_files = glob.glob('/home/user/Music/dharmendra/image_processing'+'/'+str(name)+'/*') # * means all if need specific format then *.csv
                    list_of_files = glob.glob(f'{os.getcwd()}//'+'/'+str(name)+'/*')
                    latest_file = max(list_of_files, key=os.path.getctime)
                    final=str(latest_file).find('.')
                    final1=str(latest_file).rfind('/')
                    emp=''
                    for i in str(latest_file)[final1:final]:
                        if i.isdigit():
                            emp=emp+i
                    counter+=int(emp)        
                except:
                    pass
                    # make_folder(name)
            else:
                make_folder(name)
            break
            
    # output_loc = '/home/user/Music/dharmendra/image_processing'+'/'+str(name)+'/'
    output_loc = f'{os.getcwd()}//'+'/'+str(name)+'/'

    # screen, px,text = setup(input_loc[count],name)
    while True: 
        im = Image.open(input_loc[count])
        screen, px,text = setup(input_loc[count],name)
        left, upper, right, lower,index,w = mainLoop1(screen, px,count,text)
     
        print(index,count)
        if int(index) == count:
            # count=int(index)
            pass
        else:
            count=int(index)
            continue
            
        # ensure output rect always has positive width, height
        if right < left:
            left, right = right, left
        if lower < upper:
            lower, upper = upper, lower
        im = im.crop((left, upper, right, lower))
        pygame.draw.rect(px, (255, 0, 0, 0), (left, upper, right-left, lower-upper), 2)

        try:
            im.save(output_loc+'out'+str(counter)+'.png')
            counter+=1
        except:
            pass  





