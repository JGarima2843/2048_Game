from tkinter import Frame,Label,CENTER
import main as LogicsPointer
import constant as c 


# IN THIS WE ARE MAKING THE GAME CLASS BY INHERITING THE PYTHON TKINTER MODULE FRAME CLASS
class Game2048(Frame):
    def __init__(self) -> None:
        # super().__init__();
        # CALLING THE SUPER CLASS CONSTRUCTOR
        Frame.__init__(self);
        self.grid();
        self.master.title('2048');
        self.master.bind("<Key>",self.key_down);
        # SETTING THE COMMANDS AND RELATED KEYS
        self.commands={
            c.KEY_UP:LogicsPointer.move_Top,c.KEY_DOWN:LogicsPointer.move_down,
            c.KEY_LEFT:LogicsPointer.move_left,c.KEY_RIGHT:LogicsPointer.move_right
            };
        
        # SETTING THE GRID OF THE GAME 2048
        self.grid_cells=[]

        # CALLING THE INIT_MATRIX AS IT WILL START THE GAME AND SET THE VALUES OF EACH CELL
        self.init_matrix()

        # NOW CALLING TO THIS AS IT WILL START THE GAME AND SET ALL THE GRID UI  
        self.init_grid()
        
        #NOW CALLING THIS FUNCTION WHICH WILL UPDATE  MATRIX IF ANY CHANGES HAPPEN
        self.update_grid_cells()

        # AND THIS FOR CALLING THE SAME FUNCTION REPEATEDLY
        self.mainloop()
    
    def init_grid(self):
        # SETTING THE BACKGROUND COLOR AND ALL
        background=Frame(self,bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE,height=c.SIZE)
        background.grid()

        # LOOPING OUR EACH AND EVERY CELL OF THE GRID
        for i in range(c.GRID_LENS):
            grid_row=[]  #THIS IS FOR THE GRID ROW


            for j in range(c.GRID_LENS):
                # SETTING THE ALL UI OF A CELL
                cell=Frame(background,bg=c.BACKGROUND_EMPTY_CELL_COLOR,width=c.SIZE/c.GRID_LENS,height=c.SIZE/c.GRID_LENS)
                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)

                # THIS IS THE INNER BOX OF THE CELL WHERE OUR TEXT COMES AND DISTANCE FROM CELL
                t=Label(master=cell,text="",bg=c.BACKGROUND_EMPTY_CELL_COLOR,justify=CENTER,font=c.FONT,width=10,height=5)
                t.grid()


            # t.grid()
            # APPENDING THIS CELL IN ROW
                grid_row.append(t)

            #APPENDING THE ROW IN GRID
            self.grid_cells.append(grid_row)

# IN THIS WE ARE STARTING OUR GAME
    def init_matrix(self):
        self.matrix=LogicsPointer.start_Game()
        LogicsPointer.make_new_position_2(self.matrix)
        # LogicsPointer.make_new_position_2(self.matrix)


    # IN THIS I AM UPDATING THE GRID CELLS THAT WHETHER ANY NEW POSITION IS OCCUPIED IF IT IS THE ADJUST IT TEXT AND ALL COLOR TO GRID
    def update_grid_cells(self):

        for i in range(c.GRID_LENS):
            for j in range(c.GRID_LENS):
                new_number=self.matrix[i][j]
                if new_number==0:
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_EMPTY_CELL_COLOR)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),bg=c.BACKGROUND_COLOR_DICT[new_number],fg=c.CELL_COLOR_DICT[new_number])
                
                self.update_idletasks()

# THIS IS INVOKED WHEN THERE IS ANY KEY DOWN IN THE KEYBOARD
    def key_down(self,event):
        # TAKING OUT THE KEY
        key=repr(event.char)
        # print(key,self.commands)
        # key=str(key)
        

        # CHECKING WHETHER THAT KEY PRESENT
        if key in self.commands:
            # print("here")
            self.matrix,changed=self.commands[key](self.matrix)
            # IF ACTUALLY OUR MATRIX CHANGED FROM THAT 2
            if changed:
                # LogicsPointer.make_new_position_2(self.matrix)

                # NOW UPDATING OUR GRID WITH THAT NEW NUMBER AND SETTING THE UI
                self.update_grid_cells()
                changed=False

                # IF I WON THE GAME 
                if LogicsPointer.get_Current_State(self.matrix)=="WON":
                    self.grid_cells[1][1].configure(
                        text="YOU",bg="#ffffff"
                    )

                    self.grid_cells[1][2].configure(
                        text="WIN 🥳🍾" ,bg="#ffffff"
                    )
                    return 
                # IF I LOST THE GAME
                elif LogicsPointer.get_Current_State(self.matrix)=="LOST":
                    self.grid_cells[1][1].configure(
                        text="YOU",bg=c.BACKGROUND_EMPTY_CELL_COLOR
                    )

                    self.grid_cells[1][2].configure(
                        text="LOST !" ,bg=c.BACKGROUND_EMPTY_CELL_COLOR
                    )
                    return



# IT IS THE ENTRY POINT OF OUR WHOLE PROGRAMME
Gamegrid = Game2048()


    
    
    



    


        
        
        

        
        


        












