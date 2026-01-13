# %%
move = 0

def TowerOfHanoi(n, source, auxiliary, destination):
    global move
    if n == 1:
        move += 1
        print(f"Move disk 1 from {source} to {destination} (Move {move})")
        return
    
    TowerOfHanoi(n-1, source, destination, auxiliary)
    
    move += 1
    print(f"Move disk {n} from {source} to {destination} (Move {move})")
    
    TowerOfHanoi(n-1, auxiliary, source, destination)

# %%
def run_TowerOfHanoi(n):
    global move
    move = 0
    TowerOfHanoi(n, "A", "B", "C")
    print(f"\nTotal moves used: {move}")

# Driver for 4 disks
run_TowerOfHanoi(4)
