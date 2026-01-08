# %%
move = 0 

def TowerOfHanoi(n, source, auxillary, destination):
    global move
    if n == 1: 
        move += 1
        print(f"Move disk 1 from {source} to {destination} (Move {move})")
        return
    
    TowerOfHanoi(n-1, source, auxillary, destination)
    
    move += 1
    print(f"Move disk {n} from {source} to {destination} (Move {move})")
    
    TowerOfHanoi(n-1, auxillary, source, destination)

# %%
def two_stage_Tower_Of_Hanoi(n):
    TowerOfHanoi(n - 1, "A", "B", "C")
    global move
    move += 1
    print(f"Move disk {n} from A to C (Move {move})")
    TowerOfHanoi(n - 1, "B", "A", "C")

#driver for 4 disks
two_stage_Tower_Of_Hanoi(4)

#final total moves
print(f"\nTotal moves used: {move}")
