def debug_week0_thursday(x,y,u,v):
    if x > y:
        x = x - y;
        u = u + v;
        print(str(x) + " " + str(y) + " " + str(u) + " " + str(v));
        debug_week0_thursday(x,y,u,v);
    elif y > x:
        y = y - x;
        v = v + u;
        print(str(x) + " " + str(y) + " " + str(u) + " " + str(v));
        debug_week0_thursday(x,y,u,v);        
    else: 
        print((x + y) / 2 * (u + v) / 2);
debug_week0_thursday(36,10,36,10)