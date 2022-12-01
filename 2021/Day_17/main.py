def target_area(min_x,max_x,min_y,max_y):
    return ([x for x in range(min_x,max_x+1)],[y for y in range(min_y,max_y+1)], max_x+1)

def mock():
    return target_area(20,30,-10,-5)

def data():
    return target_area(150,193,-136,-86)
            
def step_calc(pos,vel):
    x_vel,y_vel = vel
    x_pos,y_pos = pos
    x_pos += x_vel
    y_pos += y_vel

    if x_vel > 0: 
        x_vel -= 1
    if x_vel < 0:
        x_vel += 1
    
    y_vel -= 1

    pos = x_pos, y_pos
    vel = x_vel, y_vel
    return pos, vel


def calculate_trajectory(x_arr,y_arr,r):
    max_vel = []
    for r_x in range(-r,r):
        for r_y in range(-r,r):
            velocity = r_x, r_y
            trajectory = []
            start_vel = [r_x,r_y]
            pos = [0,0]
            target_reached = False                        
            
            while True:
                pos, velocity = step_calc(pos,velocity)
                trajectory.append(pos)
                pos_x,pos_y = pos

                # hit
                if pos_x in x_arr and pos_y in y_arr :
                    target_reached = True
                    break
                
                # miss
                if pos_y < min(y_arr):
                    target_reached = False
                    break
                    
            if target_reached:
                max_vel.append([start_vel,max([t[1] for t in trajectory])])
    return max_vel

def main():
    # calc = 'mock'
    calc = 'data'

    
    if calc == 'mock':
        x_arr, y_arr, r = mock()
    
    if calc == 'data':
        x_arr, y_arr, r = data()
    
    trajectory_data = calculate_trajectory(x_arr, y_arr, r)
    
    # part 1
    for i in range(len(trajectory_data)):
        if trajectory_data[i][1] == max([trajectory_data[m][1] for m in range(len(trajectory_data))]):
            t=trajectory_data[i][1]
    print("Highest y pos is ", t)
    
    # part 2
    print("There are ",len(trajectory_data)," different initial velocity values")

if __name__ == "__main__":
    main()