import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

#code to create evenly split angles
def angle_gen(num):
    step=75/num
    nums=[0]
    for i in range(1,round(num/2)+1):
        nums.append(0+i*step)
        nums.append(0-i*step)
    if len(nums)!=num:
        nums=nums[:-1]
    return nums

#code to generate colours from red to orange and then to cyan that are graduated so that cyan is reached by num
def color_gen(num):
    colours=[]
    step=765/num
    r=255
    g=0
    b=0
    for i in range(0,num):
        if g<255:
            g+=step
        elif g==255 and r!=0:
            r-=step
        elif b<255:
            b+=step
        else:
            r=255
            g=0
            b=0
        r=min(r,255)
        r=max(r,0)
        g=min(g,255)
        g=max(g,0)
        b=min(b,255)
        b=max(b,0)
        colours.append((r,g,b))
    return colours

#specify the architecture you wish to visualise here
architecture=list(range(12,4,-1))+list(range(6,13,1))
#starts with an x value of 0
x=0

#this is so we don't try to link the first layers neurons to any previous layer as there isn't a previous layer
first=True
neurons=[]
#generate colors for highest number in the architecture
colours=color_gen(max(architecture))
#for each layer in the architecture
for num in architecture:
    #generates the list of angles to place neurons at
    angles=angle_gen(num)
    #copies the current neurons list to old_neuron
    old_neurons=neurons
    #reinits neurons
    neurons=[]
    #for each neuron
    for i in range(0,num):
        #make the pen the colour for that neuron number
        t.color(colours[i])
        #lifts the pen
        t.penup()
        #sets turtle's angle to the angle for this neuron number
        t.setheading(angles[i])
        #moves forwards in the direction of the previously set angle
        t.forward(100)
        #puts the pen down
        t.pendown()
        #puts a dot down to show that neuron
        t.dot(5)
        #appends turtle's current position to the neurons list
        neurons.append(t.pos())
        #lifts the pen 
        t.penup()
        #goes back to the begining
        t.goto(x,0)
    #if it isn't the first layer
    if first!=True:
        i=0
        #for each neuron in the previous layer
        for old_neuron in old_neurons:
            #set the color to the correct color for that neuron number
            t.color(colours[i])
            #for each neuron in the new layer
            for neuron in neurons:
                #go to the old neuron
                t.goto(old_neuron)
                #put the pen down
                t.pendown()
                #go to the new neuron
                t.goto(neuron)
                #lift the pen up
                t.penup()
                #go back to the old neuron
                t.goto(old_neuron)
            i+=1
    #so the origin point for the next layer is further x
    x+=100
    #go to the new origin
    t.goto(x,0)
    #it's no longer the first layer
    first=False
