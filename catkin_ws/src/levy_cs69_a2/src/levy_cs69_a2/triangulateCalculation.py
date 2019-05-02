import math
import rospy
class TriangulateCalculation:
    def __init__(self):
        pass    
    
    """
    Triangulation code modeled after Amulya Khare's: https://stackoverflow.com/questions/19723641/find-intersecting-point-of-three-circles-programmatically

    Input: a dictionary with its keys as signal strengths and its values as the positions associated with those strengths
    Output: a point representing the source of the signal

    Triangulate:
        - takes in inputs
        - calculates the distances between the source of the signal and the position the signal was read  
        - constructs three circles with the positions as the centers and their distances from the source as the radii
        - solve for the intersection of the three circles 

    Distances are found by backwards-solving the Free Space Path Loss Model

    """
    def triangulate(self, points, error):
        strength=[0,0,0]
        x=[0,0,0]
        y=[0,0,0]
        i = 0
        
        #read inputs into local variables
        for key, value in points.items():
            strength[i] = key

            x[i] = value[0]
            y[i] = value[1]
            i += 1
    
############### Solving for Distances ####################
        #total path loss
        Pl_0 = strength[0]
        Pl_1 = strength[1]
        Pl_2 = strength[2]
    
        #relative path loss between two points
        Plo0_1 = strength[1] - strength[0]
        Plo1_2 = strength[2] - strength[1]
    
        #distances between points 0->1 and 1->2
        d_x = x[1]-x[0]
        d_y = y[1]-y[0]
        d = math.sqrt(d_x**2 + d_y**2)
        d_x_2 = x[2] - x[1]
        d_y_2 = y[2] - y[1]
        d_2 = math.sqrt(d_x_2**2 + d_y_2**2)

        #the signal at full strength
        deb0 = 20*math.log10(0.001 * 0.1) + 20*math.log10(1000 * 2.4) + 32.44 

        #the distances that should result in the total path loss seen in Pl_0, Pl_1, Pl_2
        radius_0 =1000 * 10**(((-Pl_0 * deb0)/10 -32.44- 20*math.log10(1000 * 2.4))/20) 
        radius_1 =1000 * 10**(((-Pl_1 * deb0)/10 -32.44- 20*math.log10(1000 * 2.4))/20) 
        radius_2 =1000 * 10**(((-Pl_2 * deb0)/10 -32.44- 20*math.log10(1000 * 2.4))/20) 
        
############# Solving for Intersection of Three Circles ################

        #distance to radical axis between circles 0 and 1 from circle 0
        a = (radius_0**2 - radius_1**2 + d**2 )/(2*d) 

        #the x and y points that lie on the radical axis inbetween the intersection points
        x_intersect = x[0] + d_x*(a/d)
        y_intersect = y[0] + d_y*(a/d)


        #distance from point a to the intersection points
        h = math.sqrt(abs((radius_0**2) - (a**2)))

        #intersection points between circles 0 and 1
        intersectionPoint1_x = x_intersect - d_y * (h/d)
        intersectionPoint1_y = y_intersect + d_x * (h/d)
        intersectionPoint2_x = x_intersect + d_y * (h/d)
        intersectionPoint2_y = y_intersect - d_x * (h/d)
        
        #Distances from each intersection point to the center of circle 2 
        intersect1dx = intersectionPoint1_x - x[2]
        intersect1dy = intersectionPoint1_y - y[2]
        d1 = math.sqrt((intersect1dx**2) + (intersect1dy**2))

        intersect2dx = intersectionPoint2_x - x[2]
        intersect2dy = intersectionPoint2_y - y[2]
        d2 = math.sqrt((intersect2dx**2) + (intersect2dy**2))

        #checking which point lies on the circumference of circle 2. The point that does is the intersection point of the three circles.
        if(d1-radius_2 < error):
            goal_x = intersectionPoint1_x
            goal_y =intersectionPoint1_y
        elif(d2-radius_2< error):
            goal_x = intersectionPoint2_x
            goal_y =intersectionPoint2_y
        else:
            goal_x = 0
            goal_y = 0

        return goal_x,goal_y



               
