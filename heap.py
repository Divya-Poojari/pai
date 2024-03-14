import random

def print_board(heap):
    print(f"Current heap: {'|'*heap}")
    
def get_user_move(heap):
    while True:
        try:
            sticks_to_remove=int(input(f"Enter the number of sticks to remove:(minimum1,maximum{min(heap,heap//2)})"))
            if 1<=sticks_to_remove<=min(heap,heap//2):
                break
            else:
                print(f"Invalid number enter a number between 1 and{min(heap,heap//2)}")
        except ValueError:
            print("Invalid number")
    return sticks_to_remove

def get_computer_move(heap):
    xor_sum=heap
    for i in range(heap):
        xor_sum^=i
    if xor_sum==0:
        max_sticks=min(heap,heap//2)
        sticks_to_remove=random.randint(1,max_sticks)
    else:
        max_sticks=min(heap//2,heap)
        sticks_to_remove=max(1,min(max_sticks,heap-xor_sum))
    return sticks_to_remove

def nim_game():
    heap=16
    player_turn=1
    while heap>1:
        print_board(heap)
        player_name="Player1" if player_turn==1 else"Computer"
        sticks_to_remove=get_user_move(heap) if player_turn==1 else get_computer_move(heap)
        heap-=sticks_to_remove
        print(f"{player_name} removes {sticks_to_remove} sticks")
        player_turn=3-player_turn
    print_board(heap)
    winner="player1" if player_turn==2 else "Computer"
    print(f"player {player_turn} picks the last stick")
    print(f"{winner} wins!")
if __name__=="__main__":
    nim_game()