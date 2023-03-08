import random


def Compressor_grid(matrix,move):

    # THIS FUNCTION IS TO FIRSTLY ASSEMBLE ALL NON-ZERO POSITION OF THE GRID AND THEN DOING THE MERGING AND REMOVING THE SAME OCCURRING COUPLE ELEMENTS WITH THEIR TWICE

    # SETTING A NEW MATRIX
    new_matrix=[[0 for i in range(4)] for j in range(4)]
    pos=0 
    
    # HERE WE IN LOOP I AM  JUST CHECKING THAT WHETHER THE GIVEN POSITION IS NON-ZERO OR NOT IF IT IS THEN JUST REPLACING THE NEW-MATRIX TO THAT POSITION
    # THIS IS WHEN THE LEFT MOVE IS GIVEN TO US 
    if move=="left":
        # 😵‍💫 in this rows are const
        for i in range(4):
            pos=0 
            for j in range(4):
                if matrix[i][j]!=0:
                    new_matrix[i][pos]=matrix[i][j]
                    pos+=1

    # THIS IS FOR THE RIGHT MOVE GIVEN
    elif move=="right":
            # 😵‍💫  row is constant 
        for i in range(4):
            pos=3
            for j in range(3,-1,-1):
                if matrix[i][j]!=0:
                    new_matrix[i][pos]=matrix[i][j]
                    pos-=1
    # THIS IS FOR THE TOP MOVE GIVEN
    elif move=="top":
            # 😵‍💫 Column is constant 
        for col in range(4):
            pos=0
            for row in range(4):
                if matrix[row][col]!=0:
                    new_matrix[pos][col]=matrix[row][col]
                    pos+=1
    # THIS IS FOR THE DOWN MOVE GIVEN TO US
    elif move=="down":
        for col in range(4):
            pos=3
            for row in range(3,-1,-1):
                if matrix[row][col]!=0:
                    new_matrix[pos][col]=matrix[row][col]
                    pos-=1


    # JUST FOR CHECKING PURPOSE 😵‍💫😵‍💫-------
    print("After compressing it to the ",move)
    print_Grid(new_matrix)
    # ---------------------------------------


    # THIS IS TO CALL NOW ON THE NEW_MATRIX TO SUBMERGE THE SAME POSITION ELEMENT IN THE MATRIX
    changed=merge_Grid(new_matrix,move)
    # IT IS RETURNING THE BOOLEAN VARIABLE DENOTING THAT IS OUR MATRIX CHANGED OR NOT??

    return new_matrix,changed


def make_new_position_2(matrix):

    # THIS IS FUNCTION IS FOR MAKING NEW TWO POSITION IN THE MATRIX 
    
    pos_r=random.randint(0,3)
    pos_c=random.randint(0,3)

    # THIS IS TO CHECK WHETHER THE POSITION INDX GENERATED IS FREE OR NOT IN OUR MATRIX

    while matrix[pos_r][pos_c] !=0:
        pos_r=random.randint(0,3)
        pos_c=random.randint(0,3)
    
    matrix[pos_r][pos_c]=2 
    # JUST FOR CHECKING PURPOSE 😵‍💫😵‍💫-------
    print_Grid(matrix)



def merge_Grid(matrix,move):
    changed=False

    # THIS IS THE FUNCTION IN WHICH I AM SUBSTITUTING THE VALUES OF THE SAME POSITIONED ELEMENT THAT IS IN THE COMPRESSED MATRIX 

    # TO CHECK FOR LEFT MOVE
    if move=="left":
        for i in range(4):
            for j in range(3):
                if matrix[i][j]==matrix[i][j+1]:
                    matrix[i][j]=2*matrix[i][j]
                    matrix[i][j+1]=0 
                    changed=True

    # TO CHECK FOR THE RIGHT MOVE

    elif move=="right":
        for i in range(4):
            for j in range(3,0,-1):
                if matrix[i][j]==matrix[i][j-1]:
                    matrix[i][j]=2*matrix[i][j]
                    matrix[i][j-1]=0 
                    changed=True

    # TO CHECK FOR THE TOP MOVE
    
    elif move=="top":

        for col in range(4):
            for row in range(3):

                if matrix[row][col]==matrix[row+1][col]:
                    matrix[row][col]=2*matrix[row][col]
                    matrix[row+1][col]=0 
                    changed=True

    # TO CHECK FOR THE DOWN MOVE
    elif move=="down":
        
        for col in range(4):
            for row in range(3,0,-1):

                if matrix[row][col]==matrix[row-1][col]:
                    matrix[row][col]=2*matrix[row][col]
                    matrix[row-1][col]=0 
                    changed=True


    # JUST FOR CHECKING PURPOSE 😵‍💫😵‍💫-------
    print("AFTER the merge func")
    print_Grid(matrix)

    print("AFTER the new position 2")
    # --------------------------------------

    # AFTER THE MERGING AND THE SUBSTITUTION I HAVE JUST CALLED THE FUNCTION TO ADD NE 2 POSITION FOR THE NEXT MOVE 
    make_new_position_2(matrix)
    return changed 



def set_Matrix(new_matrix,matrix):
    # IT IS WHEN WE ARE MAKING THE NEW_MATRIX FOR THE COMPRESSION AND MERGE FUNCTION THEN ACTUAL MATRIX CONTENT IS NOT CHANGED SO WE ARE JUST CHANGING THAT THROUGH THIS
    for i in range(4):
        for j in range(4):
            matrix[i][j]=new_matrix[i][j]
        



    
def move_left(matrix):


    # 🔔🔔 SAME STEPS APPLY OVER ALL THE MOVES -----------------
    # ✅ Step 1) compress that given grid 
    # ✅ Step 2) merge that given grid ===>Combine the same number addition on the position
    # ✅ Step 3) place new 2 on the grid through this move on the empty positions 
    
    new_matrix,changed=Compressor_grid(matrix,"left")
    set_Matrix(new_matrix,matrix)
    return matrix,changed

    # pass

def move_right(matrix):

    new_matrix,changed=Compressor_grid(matrix,"right")
    set_Matrix(new_matrix,matrix)
    return matrix,changed

def move_Top(matrix):
    new_matrix,changed=Compressor_grid(matrix,"top")
    set_Matrix(new_matrix,matrix)
    # pass
    return matrix,changed

def move_down(matrix):
    new_matrix,changed=Compressor_grid(matrix,"down")
    set_Matrix(new_matrix,matrix)
    # pass
    return matrix,changed
    


def grid_Setter():

    # THIS FUNCTION IS FOR THE SETTING OUR INITIAL GRID FOR STARTING THE GAME

    matrix=[[0 for i in range(4)] for j in range(4)]

    # pos_r=random.randint(0,3)
    # pos_c=random.randint(0,3)

    # while matrix[pos_r][pos_c] !=0:
    #     pos_r=random.randint(0,3)
    #     pos_c=random.randint(0,3)
    
    # matrix[pos_r][pos_c]=2 

    return matrix ;

def print_Grid(matrix): #PRINTING THE 2048 GRID 

    for i in range(4):
        for j in range(4):
            print(matrix[i][j],end="  ")
        print()
    
    return     


def get_Current_State(matrix): 
    
    # IN THIS I AM RETURNING THE CURRENT STATE OF THE GAME 

    # 💸 STATE CASE 1: IN THIS WE ARE CHECKING IF ANY OF THE POSITION BECOME 2048 THE WE --> 🎵 WON 🎶
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==16:
                return "WON"
    
    # 💸STATE CASE 2: IN THIS I AM CHECKING THAT IS ANY 0 VALUE CELL THERE IS GRID THEN I HAVE-->🎶 NOT LOST 🎵
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==0:
                return "GAME NOT OVER"
            

    # 💸STATE CASE 3: IN THIS I AM CHECKING THAT IF ANY HORIZONTAL SAME CONSECUTIVE ELEMENT THEN I HAVE-->🎶  NOT LOST
    for i in range(4):
        for j in range(3):
            if matrix[i][j]==matrix[i][j+1]:
                return "GAME NOT OVER"
            
    # 💸STATE CASE 3: IN THIS I AM CHECKING THAT IF ANY VERTICAL SAME CONSECUTIVE ELEMENT THEN I HAVE -->🎵 NOT LOST
    
    for i in range(3):
        for j in range(4):
            if matrix[i][j]==matrix[i+1][j] :
                return "GAME NOT OVER"
            
    # 💸STATE CASE 4: IF ANY OF THE STATE CASE DOES NOT MATCH THEN I HAVE  -----> 🚨LOST THE GAME🚨
    
    return "LOST"




    



# 🚨 STARTING POINT OF THE CODE ...🤌🏽
def start_Game():
    matrix=grid_Setter()
    # print_Grid(matrix);
    # n=int(input())

    # while n!=0:
    #     if(n==2):
    #         move_down(matrix)
            
    #     elif(n==4):
    #         move_left(matrix)
    #     elif(n==6):
    #         move_right(matrix)
    #     elif(n==8):
    #         move_Top(matrix)
        
    #     n=int(input())

    return matrix

    

