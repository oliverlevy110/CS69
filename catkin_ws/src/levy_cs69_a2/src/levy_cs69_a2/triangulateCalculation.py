import math
import rospy
class TriangulateCalculation:
    def __init__(self):
        pass    
    
    """
    Triangulation code modeled after Amulya Khare's: https://stackoverflow.com/questions/19723641/find-intersecting-point-of-three-circles-programmatically

    """
    def triangulate(self, points, error):
        strength=[0,0,0]
        x=[0,0,0]
        y=[0,0,0]
        i = 0
        for key, value in points.items():
            strength[i] = key

            x[i] = value[0]
            y[i] = value[1]
            i += 1

        Pl_0 = strength[0]
        Pl_1 = strength[1]
        Pl_2 = strength[2]
        Plo0_1 = strength[1] - strength[0]
        Plo1_2 = strength[2] - strength[1]
        d_x = x[1]-x[0]
        d_y = y[1]-y[0]
        d = math.sqrt(d_x**2 + d_y**2)
    


        deb0 = 20*math.log10(0.001 * 0.1) + 20*math.log10(1000 * 2.4) + 32.44 
        radius_0 =1000 * 10**(((-Pl_0 * deb0)/10 -32.44- 20*math.log10(1000 * 2.4))/20) 
        radius_1 =1000 * 10**(((-Pl_1 * deb0)/10 -32.44- 20*math.log10(1000 * 2.4))/20) 
        radius_2 =1000 * 10**(((-Pl_2 * deb0)/10 -32.44- 20*math.log10(1000 * 2.4))/20) 

        d_x_2 = x[2] - x[1]
        d_y_2 = y[2] - y[1]

        d_2 = math.sqrt(d_x_2**2 + d_y_2**2)

        #distance of intersection from point 0
        a = (radius_0**2 - radius_1**2 + d**2 )/(2*d) 

        x_intersect = x[0] + d_x*(a/d)
        y_intersect = y[0] + d_y*(a/d)



        h = math.sqrt((radius_0**2) - (a**2))

        intersectionPoint1_x = x_intersect - d_y * (h/d)
        intersectionPoint1_y = y_intersect + d_x * (h/d)
        intersectionPoint2_x = x_intersect + d_y * (h/d)
        intersectionPoint2_y = y_intersect - d_x * (h/d)
        
        intersect1dx = intersectionPoint1_x - x[2]
        intersect1dy = intersectionPoint1_y - y[2]
        d1 = math.sqrt((intersect1dx**2) + (intersect1dy**2))

        intersect2dx = intersectionPoint2_x - x[2]
        intersect2dy = intersectionPoint2_y - y[2]
        d2 = math.sqrt((intersect2dx**2) + (intersect2dy**2))
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



               
