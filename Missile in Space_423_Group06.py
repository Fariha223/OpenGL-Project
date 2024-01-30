from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np
import random

def pixie():
    glPointSize(2)
    glColor3f(1, 1, 1)
    glBegin(GL_POINTS)
    for i in range(0, 200):
        glVertex(random.randint(-1000, 1000), random.randint(-1000, 1000))
    glEnd()


def dust(x1,x2,y1,y2,n,x):
    glPointSize(x)
    glBegin(GL_POINTS)
    for i in range(0, n):
        glVertex(random.randint(x1, x2), random.randint(y1, y2))
    glEnd()

def draw_points(x,y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1000, 1000, -1000, 1000, -1.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    input1 = input('Enter:')
    if input1 == 'start':
        pixie()
        missile()
        earth()
        asteroid(-750, 800)
    elif input1 == 'next':
        pixie()
        moveup_missile()
        asteroid(-550, 600)
        earth()
    elif input1 == 'phase3':
        pixie()
        asteroid(-400, 450)
        close_missile()
        earth()
    elif input1 == 'hit':
        pixie()
        missile_hit()
        earth()
        asteroid(200,-400)
    elif input1 == 'cracked':
        pixie()
        missile_hit()
        cracked_earth()
        asteroid(240,-420)
    elif input1 == 'destroyed':
        pixie()
        destroyed_earth()
        end()
    elif input1 == 'saved':
        pixie()
        target_miss()
        earth()
        saved()
        asteroid(870,-550)
    glutSwapBuffers()




def translate(t_x,t_y):
    T = np.array([[1, 0, t_x],
                  [0, 1, t_y],
                  [0, 0, 1]])
    return T

def rotate(v1,v2):
    a = math.cos(math.radians(v1))
    b = math.sin(math.radians(v2))

    r = np.array([[a, -b, 0],
                  [b, a, 0],
                  [0, 0, 1]])
    return r
def sl(sc):
    s = np.array([[sc, 0, 0],
                  [0, sc, 0],
                  [0, 0, 1]])
    return s
def end():
    glColor3f(0.85, 0.3, 0)
    make_line(-700,300,-700,150)
    make_line(-700,300,-620,300)
    make_line(-700,150,-620,150)
    make_line(-700,225,-650,225)
    make_line(-600,300,-600,150)
    make_line(-600,300,-520,150)
    make_line(-520,300,-520,150)
    make_line(-500,300,-500,150)
    make_line(-420,270,-420,180)
    make_line(-500,150,-420,180)
    make_line(-500,300,-420,270)
def saved():
    glColor3f(0, 0.5, 0)
    make_line(-700,300,-620,300)
    make_line(-700,300,-700,225)
    make_line(-700,225,-620,225)
    make_line(-620,225,-620,150)
    make_line(-700,150,-620,150)
    make_line(-600,150,-560,300)
    make_line(-560,300,-520,150)
    make_line(-585,225,-555,225)
    make_line(-500,300,-460,150)
    make_line(-460,150,-420,300)
    make_line(-400,300,-400,150)
    make_line(-400,300,-320,300)
    make_line(-400,150,-320,150)
    make_line(-400,225,-360,225)
    make_line(-300,300,-300,150)
    make_line(-300,300,-300,150)
    make_line(-220,270,-220,180)
    make_line(-300,150,-220,180)
    make_line(-300,300,-220,270)

def circle_points():
    put_circle=np.array([[600],
                         [200],
                         [1]])
    return put_circle

def MidpointCircle(xc,yc,r):
    d=1-r
    x=0
    y=r
    while (x<=y):
        if d<0:
            d=d+(2*x)+3
            x=x+1
        else:
            d=d+(2*x)-(2*y)+5
            x=x+1
            y=y-1
        draw_points(xc+x,yc+y)
        draw_points(xc-x,yc+y)
        draw_points(xc+x,yc-y)
        draw_points(xc-x,yc-y)
        draw_points(xc+y,yc+x)
        draw_points(xc-y,yc+x)
        draw_points(xc+y,yc-x)
        draw_points(xc-y,yc-x)

def frag1(xc,yc,r):
    d=1-r
    x=0
    y=r
    while (x<=y):
        if d<0:
            d=d+(2*x)+3
            x=x+1
        else:
            d=d+(2*x)-(2*y)+5
            x=x+1
            y=y-1
        draw_points(xc + x, yc + y)
def frag2(xc,yc,r):
    d=1-r
    x=0
    y=r
    while (x<=y):
        if d<0:
            d=d+(2*x)+3
            x=x+1
        else:
            d=d+(2*x)-(2*y)+5
            x=x+1
            y=y-1
        draw_points(xc - x, yc - y)

def frag3(xc,yc,r):
    d=1-r
    x=0
    y=r
    while (x<=y):
        if d<0:
            d=d+(2*x)+3
            x=x+1
        else:
            d=d+(2*x)-(2*y)+5
            x=x+1
            y=y-1
        draw_points(xc - y, yc + x)
def frag4(xc,yc,r):
    d=1-r
    x=0
    y=r
    while (x<=y):
        if d<0:
            d=d+(2*x)+3
            x=x+1
        else:
            d=d+(2*x)-(2*y)+5
            x=x+1
            y=y-1
        draw_points(xc + y, yc - x)
def destroyed_earth():
    r=200
    glColor3f(0.35, 0, 0)
    for i in range(0,-60,-1):
        frag4(600,200,r+i)
    glColor3f(0.5,0.2,0)
    for i in range(50,30,-1):
        frag4(600,200,r+i)
    glColor3f(0.6,0.1,0)
    for i in range(59,30,-1):
        frag4(600,200,r-i)
    glColor3f(0.75,0,0)
    for i in range(29,15,-1):
        frag4(600,200,r-i)
    circle_scale=np.matmul(sl(0.3),circle_points())
    circle_translate = np.matmul(translate(540,350), circle_scale)
    xc = circle_translate[0][0]
    yc = circle_translate[1][0]
    glColor3f(0.35, 0, 0)
    for i in range(0,-40,-1):
        frag1(xc, yc, (r/3)+i)
    glColor3f(0, 0.5, 0)
    for i in range(50,40,-1):
        frag1(xc,yc,(r/3)-i)
    circle_translate = np.matmul(translate(640,450), circle_scale)
    xc = circle_translate[0][0]
    yc = circle_translate[1][0]
    glColor3f(0.35, 0.13, 0)
    for i in range(0,-25,-1):
        frag1(xc, yc, (r/4)+i)

    circle_translate = np.matmul(translate(300,-80), circle_scale)
    xc = circle_translate[0][0]
    yc = circle_translate[1][0]
    glColor3f(0.35, 0.13, 0)
    for i in range(0,-45,-1):
        frag2(xc, yc, (r/2)+i)
    glColor3f(0.35, 0, 0)
    for i in range(20,0,-1):
        frag2(xc,yc,(r/2)+i)
    glColor3f(0.7,0,0)
    for i in range(60,45,-1):
        frag2(xc,yc,(r/2)-i)

    circle_translate = np.matmul(translate(400,-120), circle_scale)
    xc = circle_translate[0][0]
    yc = circle_translate[1][0]
    glColor3f(0.35,0.17,0)
    for i in range(0,-30,-1):
        frag2(xc,yc,(r/5)+i)

    circle_translate = np.matmul(translate(290,310), circle_scale)
    xc = circle_translate[0][0]
    yc = circle_translate[1][0]
    glColor3f(0.25,0.17,0)
    for i in range(0,30,1):
        frag3(xc,yc,(r/2)+i)
    glColor3f(0.5, 0.12, 0)
    for i in range(50,10,-1):
        frag3(xc,yc,(r/2)-i)
    glColor3f(0.5,0.2,0)
    dust(580,680,120,300,80,1.5)
    glColor3f(0.5,0.2,0)
    dust(370,850,-40,470,150,2)
    glColor3f(0.9,0.4,0)
    for i in range(0,-20,-1):
        MidpointCircle(600,200,r/4+i)


def earth():
    glColor3f(0, 0.3, 0.4)
    for i in range(0,-200,-1):
        MidpointCircle(600,200,200+i)
    glColor3f(0, 0.5, 0)
    for i in range(0,-32,-1):
        make_line(635, 250+i, 672, 275+i)
        make_line(700,80+i,660,60+i)
    for i in range(-32,0,1):
        make_line(672, 275+i, 710, 260+i)
    for i in range(0,50,1):
        make_line(672, 200 + i, 635, 220 + i)
        make_line(550, 280 + i, 590, 340+i)
    for i in range(0, 60, 1):
        make_line(550, 280 + i, 520, 290 + i)
    for i in range(0,-20,-1):
        make_line(590,390+i,520,350+i)
    for i in range(32,0,-1):
        make_line(672,200+i,710,230+i)
    for i in range(0,-50,-1):
        make_line(500,150+i,480,190+i)
    for i in range(-40,0,1):
        make_line(500,150+i,450,120+i)
        make_line(480,190+i,450,120+i)

def cracked_earth():
    earth()
    glColor3f(0,0,0)
    make_line(400, 190, 450, 160)
    make_line(450,160,495,205)
    make_line(495,205,520,170)
    glColor3f(1,0.2,0)
    dust(370,405,190,210,20,2.2)
    dust(370,405,170,190,15,2)


def asteroid(x,y):
    r=200
    circle_scale=np.matmul(sl(0.3),circle_points())
    circle_translate = np.matmul(translate(x,y), circle_scale)
    xc = circle_translate[0][0]
    yc = circle_translate[1][0]
    for i in range(0, -50, -1):
        glColor3f(0.502, 0.502, 0.502)
        MidpointCircle(xc, yc, (r / 4) + i)
        glColor3f(0, 0, 0)
        MidpointCircle(xc-20,yc-65,(r/9)+i)
        glColor3f(0, 0, 0)
        MidpointCircle(xc+30,yc+65,(r/9)+i)
        glColor3f(0, 0, 0)
        MidpointCircle(xc+65,yc-20,(r/9)+i)
def missile():
    glColor3f(0.85,0.3,0)#body
    dust(-685,-640,-790,-660,50,2)
    for i in range(0, -120, -1):
        glColor3f(0.5,0.3,0.4)
        make_line(-600 + i, -350, -600 + i, -650)

    for i in range(0, -90, -1):#rightedge
        glColor3f(0.1, 0.6, 0.4)
        make_line(-660, -300 + i, -600, -350 + i)

    for i in range(-90, 0, 1):  # leftedge
        glColor3f(0.1, 0.6, 0.4)
        make_line(-660, -300 + i, -720, -350 + i)

    for i in range(0, -10, -1):  # rightwing
        glColor3f(0.8, 0.7, 1)
        make_line(-595, -580 + i, -550, -610 + i)

    for i in range(-10, 0, 1):  # leftwing
        glColor3f(0.8, 0.7, 1)
        make_line(-725, -580 + i, -775, -615 + i)

    for i in range(-35, 0, 1):
        glColor3f(0.85, 0.3, 0)
        make_line(-720, -650 + i, -680, -710 + i)

    for i in range(0, -35, -1):
        glColor3f(0.85, 0.3, 0)
        make_line(-600, -650 + i, -630, -710 + i)
def moveup_missile():
    v1=np.array([[-600],
                 [-350],
                 [1]])
    v2=np.array([[-600],
                 [-650],
                 [1]])
    vs1=np.matmul(sl(0.6),v1)
    vs2=np.matmul(sl(0.6),v2)
    vs11=np.matmul(translate(-150,50),vs1)
    vs22=np.matmul(translate(-150,50),vs2)
    rb=np.matmul(rotate(-80,-50),vs11)
    rb2=np.matmul(rotate(-80,-50),vs22)
    x1=rb[0][0]
    y1=rb[1][0]
    x2=rb2[0][0]
    y2=rb2[1][0]
    glColor3f(0.5, 0.3, 0.4)
    for i in range(-80,0,1):
        make_line(x1, y1+i, x2, y2+i)
    ##fire right
    f_r1=np.array([[-600],
                  [-650],
                  [1]])
    f_r2=np.array([[-630],
                   [-710],
                   [1]])
    frs1 = np.matmul(sl(0.6), f_r1)
    frs2 = np.matmul(sl(0.6), f_r2)
    frs11 = np.matmul(translate(-50, 0), frs1)
    frs22 = np.matmul(translate(-50, 0), frs2)
    rb=np.matmul(rotate(-80,-50),frs11)
    rb2=np.matmul(rotate(-80,-50),frs22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.85, 0.3, 0)
    for i in range(20,0,-1):
        make_line(x1+i, y1, x2+i , y2)
    ##fire left
    f_l1=np.array([[-720],
                   [-650],
                   [1]])
    f_l2=np.array([[-680],
                   [-710],
                   [1]])
    fls1 = np.matmul(sl(0.6), f_l1)
    fls2 = np.matmul(sl(0.6), f_l2)
    fls11 = np.matmul(translate(-80, 25), fls1)
    fls22 = np.matmul(translate(-80, 25), fls2)
    rb=np.matmul(rotate(-80,-50),fls11)
    rb2=np.matmul(rotate(-80,-50),fls22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.85, 0.3, 0)
    for i in range(0,10,1):
        make_line(x1+i, y1, x2+i , y2)

    ##Wing L
    wing_left1=np.array([[-725],
                        [-580],
                        [1]])
    wing_left2=np.array([[-775],
                         [-615],
                         [1]])
    wing_1 = np.matmul(sl(0.6), wing_left1)
    wing_2 = np.matmul(sl(0.6), wing_left2)
    wing11 = np.matmul(translate(-80, 25), wing_1)
    wing22 = np.matmul(translate(-80, 25), wing_2)
    rb=np.matmul(rotate(-80,-50),wing11)
    rb2=np.matmul(rotate(-80,-50),wing22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.8, 0.7, 1)
    for i in range(0,10,1):
        make_line(x1+i, y1, x2+i , y2)

    ##Wing R
    wing_right1=np.array([[-595],
                          [-580],
                          [1]])
    wing_right2=np.array([[-550],
                          [-610],
                          [1]])
    wing_1 = np.matmul(sl(0.6), wing_right1)
    wing_2 = np.matmul(sl(0.6), wing_right2)
    wing11 = np.matmul(translate(-50, 5), wing_1)
    wing22 = np.matmul(translate(-50, 5), wing_2)
    rb=np.matmul(rotate(-80,-50),wing11)
    rb2=np.matmul(rotate(-80,-50),wing22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.8, 0.7, 1)
    for i in range(0,10,1):
        make_line(x1+i, y1, x2+i, y2)

    ##Sharp edge Left
    glColor3f(0.1, 0.6, 0.4)
    for i in range(40,0,-1):
        make_line(-215+i,362-i,-250+i,352-i)

    ##Sharp edge Right
    glColor3f(0.1, 0.6, 0.4)
    for i in range(0,35,1):
        make_line(-205+i, 285+i,-250+i, 270+i)


def close_missile():
    v1=np.array([[-600],
                 [-350],
                 [1]])
    v2=np.array([[-600],
                 [-650],
                 [1]])
    vs1=np.matmul(sl(0.3),v1)
    vs2=np.matmul(sl(0.3),v2)
    vs11=np.matmul(translate(-150,300),vs1)
    vs22=np.matmul(translate(-150,300),vs2)
    rb=np.matmul(rotate(-100,-80),vs11)
    rb2=np.matmul(rotate(-100,-80),vs22)
    x1=rb[0][0]
    y1=rb[1][0]
    x2=rb2[0][0]
    y2=rb2[1][0]
    glColor3f(0.5, 0.3, 0.4)
    for i in range(-50,0,1):
        make_line(x1, y1+i, x2, y2+i)

    ##fire right
    f_r1 = np.array([[-600],
                     [-650],
                     [1]])
    f_r2 = np.array([[-630],
                     [-710],
                     [1]])
    frs1 = np.matmul(sl(0.3), f_r1)
    frs2 = np.matmul(sl(0.3), f_r2)
    frs11 = np.matmul(translate(-110, 300), frs1)
    frs22 = np.matmul(translate(-110, 300), frs2)
    rb = np.matmul(rotate(-100, -80), frs11)
    rb2 = np.matmul(rotate(-100, -80), frs22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.85, 0.3, 0)
    for i in range(8,0,-1):
        make_line(x1,y1-i,x2,y2-i)
    ##left fire
    f_l1 = np.array([[-720],
                     [-650],
                     [1]])
    f_l2 = np.array([[-680],
                     [-710],
                     [1]])
    fls1 = np.matmul(sl(0.3), f_l1)
    fls2 = np.matmul(sl(0.3), f_l2)
    fls11 = np.matmul(translate(-110, 300), fls1)
    fls22 = np.matmul(translate(-110, 300), fls2)
    rb = np.matmul(rotate(-100, -80), fls11)
    rb2 = np.matmul(rotate(-100, -80), fls22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.85, 0.3, 0)
    for i in range(0, 8, 1):
        make_line(x1, y1-i, x2, y2+i)
    ##left wing
    wing_left1 = np.array([[-725],
                           [-580],
                           [1]])
    wing_left2 = np.array([[-775],
                           [-615],
                           [1]])
    wing_1 = np.matmul(sl(0.3), wing_left1)
    wing_2 = np.matmul(sl(0.3), wing_left2)
    wing11 = np.matmul(translate(-120, 300), wing_1)
    wing22 = np.matmul(translate(-130, 300), wing_2)
    rb = np.matmul(rotate(-100, -80), wing11)
    rb2 = np.matmul(rotate(-100, -80), wing22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.8, 0.7, 1)
    for i in range(0, 6, 1):
        make_line(x1 + i, y1, x2 + i, y2)


    ##Wing Right
    wing_right1=np.array([[-595],
                          [-580],
                          [1]])
    wing_right2=np.array([[-550],
                          [-610],
                          [1]])
    wing_1 = np.matmul(sl(0.3), wing_right1)
    wing_2 = np.matmul(sl(0.3), wing_right2)
    wing11 = np.matmul(translate(-92, 300), wing_1)
    wing22 = np.matmul(translate(-82, 300), wing_2)
    rb=np.matmul(rotate(-100,-80),wing11)
    rb2=np.matmul(rotate(-100,-80),wing22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.8, 0.7, 1)
    for i in range(0,6,1):
        make_line(x1+i, y1, x2+i, y2)
    ##left edge
    left_edge1=np.array([[-660],
                         [-300],
                         [1]])
    left_edge2=np.array([[-720],
                         [-350],
                         [1]])
    l_edge = np.matmul(sl(0.3), left_edge1)
    l_edge2 = np.matmul(sl(0.3), left_edge2)
    l_edge11 = np.matmul(translate(-110, 280), l_edge)
    l_edge22 = np.matmul(translate(-110, 280), l_edge2)
    rb=np.matmul(rotate(-100,-80),l_edge11)
    rb2=np.matmul(rotate(-100,-80),l_edge22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.1, 0.6, 0.4)
    for i in range(0,30,1):
        make_line(x1+i, y1, x2+i, y2)
    ##right edge
    right_edge = np.array([[-660],
                           [-300],
                           [1]])
    right_edge2 = np.array([[-600],
                            [-350],
                            [1]])
    r_edge = np.matmul(sl(0.3), right_edge)
    r_edge2 = np.matmul(sl(0.3), right_edge2)
    r_edge11 = np.matmul(translate(-102, 272), r_edge)
    r_edge22 = np.matmul(translate(-102, 272), r_edge2)
    rb = np.matmul(rotate(-100, -80), r_edge11)
    rb2 = np.matmul(rotate(-100, -80), r_edge22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.1, 0.6, 0.4)
    for i in range(0, 40, 1):
        make_line(x1 + i, y1, x2 + i, y2)

def missile_hit():
    v1=np.array([[-600],
                 [-350],
                 [1]])
    v2=np.array([[-600],
                 [-650],
                 [1]])
    vs1=np.matmul(sl(0.19),v1)
    vs2=np.matmul(sl(0.19),v2)
    vs11=np.matmul(translate(-150,400),vs1)
    vs22=np.matmul(translate(-150,400),vs2)
    rb=np.matmul(rotate(-100,-80),vs11)
    rb2=np.matmul(rotate(-100,-80),vs22)
    x1=rb[0][0]
    y1=rb[1][0]
    x2=rb2[0][0]
    y2=rb2[1][0]
    glColor3f(0.5, 0.3, 0.4)
    for i in range(-30,0,1):
        make_line(x1, y1+i, x2, y2+i)

        ##fire right
    f_r1 = np.array([[-600],
                     [-650],
                     [1]])
    f_r2 = np.array([[-630],
                     [-710],
                     [1]])
    frs1 = np.matmul(sl(0.25), f_r1)
    frs2 = np.matmul(sl(0.25), f_r2)
    frs11 = np.matmul(translate(-90, 435), frs1)
    frs22 = np.matmul(translate(-90, 435), frs2)
    rb = np.matmul(rotate(-100, -80), frs11)
    rb2 = np.matmul(rotate(-100, -80), frs22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.85, 0.3, 0)
    for i in range(3,0,-1):
        make_line(x1,y1-i,x2,y2-i)

    ##left fire
    f_l1 = np.array([[-720],
                     [-650],
                     [1]])
    f_l2 = np.array([[-680],
                     [-710],
                     [1]])
    fls1 = np.matmul(sl(0.25), f_l1)
    fls2 = np.matmul(sl(0.25), f_l2)
    fls11 = np.matmul(translate(-90, 430), fls1)
    fls22 = np.matmul(translate(-90, 430), fls2)
    rb = np.matmul(rotate(-100, -80), fls11)
    rb2 = np.matmul(rotate(-100, -80), fls22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.85, 0.3, 0)
    for i in range(0, 3, 1):
        make_line(x1, y1-i, x2, y2-i)

    ##left wing
    wing_left1 = np.array([[-725],
                           [-580],
                           [1]])
    wing_left2 = np.array([[-775],
                           [-615],
                           [1]])
    wing_1 = np.matmul(sl(0.189), wing_left1)
    wing_2 = np.matmul(sl(0.189), wing_left2)
    wing11 = np.matmul(translate(-135, 400), wing_1)
    wing22 = np.matmul(translate(-135, 400), wing_2)
    rb = np.matmul(rotate(-100, -80), wing11)
    rb2 = np.matmul(rotate(-100, -80), wing22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.8, 0.7, 1)
    for i in range(0, 4, 1):
        make_line(x1, y1+i, x2, y2+i)

    ##Wing Right
    wing_right1=np.array([[-595],
                          [-580],
                          [1]])
    wing_right2=np.array([[-550],
                          [-610],
                          [1]])
    wing_1 = np.matmul(sl(0.189), wing_right1)
    wing_2 = np.matmul(sl(0.189), wing_right2)
    wing11 = np.matmul(translate(-110, 400), wing_1)
    wing22 = np.matmul(translate(-110, 400), wing_2)
    rb=np.matmul(rotate(-100,-80),wing11)
    rb2=np.matmul(rotate(-100,-80),wing22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.8, 0.7, 1)
    for i in range(0,4,1):
        make_line(x1+i, y1, x2+i, y2)
    ##left edge
    left_edge1 = np.array([[-660],
                           [-300],
                           [1]])
    left_edge2 = np.array([[-720],
                           [-350],
                           [1]])
    l_edge = np.matmul(sl(0.189), left_edge1)
    l_edge2 = np.matmul(sl(0.189), left_edge2)
    l_edge11 = np.matmul(translate(-125, 395), l_edge)
    l_edge22 = np.matmul(translate(-125, 395), l_edge2)
    rb = np.matmul(rotate(-100, -80), l_edge11)
    rb2 = np.matmul(rotate(-100, -80), l_edge22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.1, 0.6, 0.4)
    for i in range(0, 20, 1):
        make_line(x1 + i, y1, x2 + i, y2)

    ##right edge
    right_edge = np.array([[-660],
                           [-300],
                           [1]])
    right_edge2 = np.array([[-600],
                            [-350],
                            [1]])
    r_edge = np.matmul(sl(0.189), right_edge)
    r_edge2 = np.matmul(sl(0.189), right_edge2)
    r_edge11 = np.matmul(translate(-120, 395), r_edge)
    r_edge22 = np.matmul(translate(-120, 395), r_edge2)
    rb = np.matmul(rotate(-100, -80), r_edge11)
    rb2 = np.matmul(rotate(-100, -80), r_edge22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.1, 0.6, 0.4)
    for i in range(0, 20, 1):
        make_line(x1 + i, y1, x2 + i, y2)
def target_miss():
    v1=np.array([[-600],
                 [-350],
                 [1]])
    v2=np.array([[-600],
                 [-650],
                 [1]])
    vs1=np.matmul(sl(0.35),v1)
    vs2=np.matmul(sl(0.35),v2)
    vs11=np.matmul(translate(-350,950),vs1)
    vs22=np.matmul(translate(-350,950),vs2)
    rb=np.matmul(rotate(-80,-50),vs11)
    rb2=np.matmul(rotate(-80,-50),vs22)
    x1=rb[0][0]
    y1=rb[1][0]
    x2=rb2[0][0]
    y2=rb2[1][0]
    glColor3f(0.5, 0.3, 0.4)
    for i in range(-60,0,1):
        make_line(x1, y1+i, x2, y2+i)

    f_r1 = np.array([[-600],
                     [-650],
                     [1]])
    f_r2 = np.array([[-630],
                     [-710],
                     [1]])
    frs1 = np.matmul(sl(0.35), f_r1)
    frs2 = np.matmul(sl(0.35), f_r2)
    frs11 = np.matmul(translate(-280, 900), frs1)
    frs22 = np.matmul(translate(-280, 900), frs2)
    rb = np.matmul(rotate(-80, -50), frs11)
    rb2 = np.matmul(rotate(-80, -50), frs22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.85, 0.3, 0)
    for i in range(20, 0, -1):
        make_line(x1 + i, y1, x2 + i, y2)

##fire left
    f_l1=np.array([[-720],
                   [-650],
                   [1]])
    f_l2=np.array([[-680],
                   [-710],
                   [1]])
    fls1 = np.matmul(sl(0.35), f_l1)
    fls2 = np.matmul(sl(0.35), f_l2)
    fls11 = np.matmul(translate(-310, 925), fls1)
    fls22 = np.matmul(translate(-310, 925), fls2)
    rb=np.matmul(rotate(-80,-50),fls11)
    rb2=np.matmul(rotate(-80,-50),fls22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.85, 0.3, 0)
    for i in range(0,10,1):
        make_line(x1+i, y1, x2+i , y2)

    ##Wing L
    wing_left1=np.array([[-725],
                        [-580],
                        [1]])
    wing_left2=np.array([[-775],
                         [-615],
                         [1]])
    wing_1 = np.matmul(sl(0.35), wing_left1)
    wing_2 = np.matmul(sl(0.35), wing_left2)
    wing11 = np.matmul(translate(-320, 950), wing_1)
    wing22 = np.matmul(translate(-320, 950), wing_2)
    rb=np.matmul(rotate(-80,-50),wing11)
    rb2=np.matmul(rotate(-80,-50),wing22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.8, 0.7, 1)
    for i in range(0,10,1):
        make_line(x1+i, y1, x2+i , y2)

    ##Wing R
    wing_right1=np.array([[-595],
                          [-580],
                          [1]])
    wing_right2=np.array([[-550],
                          [-610],
                          [1]])
    wing_1 = np.matmul(sl(0.35), wing_right1)
    wing_2 = np.matmul(sl(0.35), wing_right2)
    wing11 = np.matmul(translate(-275, 935), wing_1)
    wing22 = np.matmul(translate(-275, 935), wing_2)
    rb=np.matmul(rotate(-80,-50),wing11)
    rb2=np.matmul(rotate(-80,-50),wing22)
    x1 = rb[0][0]
    y1 = rb[1][0]
    x2 = rb2[0][0]
    y2 = rb2[1][0]
    glColor3f(0.8, 0.7, 1)
    for i in range(0,10,1):
        make_line(x1+i, y1, x2+i, y2)

    glColor3f(0.1, 0.6, 0.4)
    for i in range(0,-30,-1):
        make_line(540+i,568,575+i,552)
    glColor3f(0.1, 0.6, 0.4)
    for i in range(0,-30,-1):
        make_line(540+i, 518,575+i,552)
def make_line(x1,y1,x2,y2):
    def FindZone(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) >= abs(dy):
            if dx > 0 and dy > 0:
                zone = 0
            elif dx < 0 and dy > 0:
                zone = 3
            elif dx < 0 and dy < 0:
                zone = 4
            else:
                zone = 7
        else:
            if dx > 0 and dy > 0:
                zone = 1
            elif dx < 0 and dy > 0:
                zone = 2
            elif dx < 0 and dy < 0:
                zone = 5
            else:
                zone = 6
        return zone

    def ConvertZone0(X, Y, zone):
        x = X
        y = Y
        if zone == 1:
            x = Y
            y = X
        elif zone == 2:
            x = Y
            y = -X
        elif zone == 3:
            x = -X
            y = Y
        elif zone == 4:
            x = -X
            y = -Y
        elif zone == 5:
            x = -Y
            y = -X
        elif zone == 6:
            x = -Y
            y = X
        elif zone == 7:
            x = X
            y = -Y
        else:
            x = X
            y = Y
        return x, y

    def ConvertOriginal(X, Y, zone):
        x = X
        y = Y
        if zone == 1:
            x = Y
            y = X
        elif zone == 2:
            x = -Y
            y = X
        elif zone == 3:
            x = -X
            y = Y
        elif zone == 4:
            x = -X
            y = -Y
        elif zone == 5:
            x = -Y
            y = -X
        elif zone == 6:
            x = Y
            y = -X
        elif zone == 7:
            x = X
            y = -Y
        else:
            x = X
            y = Y
        return x, y

    def DrawLine(x1, y1, x2, y2):
        zone = FindZone(x1, y1, x2, y2)
        x1, y1 = ConvertZone0(x1, y1, zone)
        x2, y2 = ConvertZone0(x2, y2, zone)
        dx = x2 - x1
        dy = y2 - y1
        d = 2 * dy - dx
        incE = 2 * dy
        incNE = 2 * (dy - dx)
        y = y1
        x = x1
        while (x <= x2):
            x_1 = x
            y_1 = y
            x_1, y_1 = ConvertOriginal(x_1, y_1, zone)
            draw_points(x_1, y_1)
            if d >= 0:
                d = d + incNE
                y = y + 1
            else:
                d = d + incE
            x = x + 1
    return DrawLine(x1,y1,x2,y2)

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)

glutMainLoop()

