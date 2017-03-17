#tatat1clicker
import pyautogui, time
print('Press Ctrl-C to quit.')

flag = 1
riload = 0
loop1 = 200

while loop1>0:
    #switch to chrome window
    x, y =(1070, 10)
    print(x, y)
    print('Switching to chrome')
    pyautogui.moveTo(x,y)
    pyautogui.click()

    #move to first tab
    x, y =(741, 31)
    print(x, y)
    print('Moving to first tab')
    pyautogui.moveTo(x,y,duration=0.5)
    pyautogui.click()

    if riload == 1:
        #Reload first tab
        x, y =(788, 66)
        print(x, y)
        print('Reloading first tab')
        pyautogui.moveTo(x,y,duration=0.5)
        pyautogui.click()
        time.sleep(10)

    loop1 = loop1-1
    loop2 = 10
    
    while loop2>0:
        # checking for previous used card
        print('Taking ScreenShot')
        im = pyautogui.screenshot()
        rs,gs,bs = im.getpixel((755,260))
        print(rs,gs,bs)
        ru,gu,bu = im.getpixel((755,471))
        print(ru,gu,bu)
        
        if rs==255 and gs==255 and bs==255 and ru==255 and gu==255 and bu==255 :
            #move to first tab
            x, y =(741, 31)
            print(x, y)
            print('Moving to first tab')
            pyautogui.moveTo(x,y,duration=0)
            pyautogui.click()
            #press Back button
            x, y =(731, 65)
            print(x, y)
            print('Pressing back button')
            pyautogui.moveTo(x,y,duration=0)
            pyautogui.click()
            time.sleep(10)
            rs,gs,bs=(0,0,0)
            ru,gu,bu=(0,0,0)
            if flag==1:
                flag=2
            elif flag==2:
                flag=1
            continue

        rh,gh,bh = im.getpixel((976,205))
        rr,gr,br = im.getpixel((834,457))
        rp,gp,bp = im.getpixel((1290,197))
        if not(rh== 255 and gh==204 and bh==0 and rr==216 and gr==0 and br==0 and rp==255 and gp==255 and bp==255):
            rh,gh,bh=(0,0,0)
            rr,gr,br=(0,0,0)
            rp,gp,bp=(0,0,0)
            #switch to chrome window
            x, y =(1070, 10)
            print(x, y)
            print('Switching to chrome')
            pyautogui.moveTo(x,y)
            pyautogui.click()
            #move to first tab
            x, y =(741, 31)
            print(x, y)
            print('Moving to first tab')
            pyautogui.moveTo(x,y)
            pyautogui.click()
            #Reload first tab
            x, y =(788, 66)
            print(x, y)
            print('Reloading first tab')
            pyautogui.moveTo(x,y)
            pyautogui.click()
            time.sleep(10)
            continue

        
        if flag == 1:
            # checking for previous used card
            im = pyautogui.screenshot()
            r,g,b = im.getpixel((1186,284))
            r2,g2,b2 = im.getpixel((1186,270))
            if (r==255 and g==192 and b==0) or (r2==255 and g2==192 and b2==0) :
                #move to first tab
                x, y =(741, 31)
                print(x, y)
                print('Moving to first tab')
                pyautogui.moveTo(x,y)
                pyautogui.click()
                #Reload first tab
                x, y =(788, 66)
                print(x, y)
                print('Reloading first tab')
                pyautogui.moveTo(x,y)
                pyautogui.click()
                time.sleep(10)
                r,g,b=(0,0,0)
                r2,g2,b2=(0,0,0)
                continue

            #Sequence S1
            print('Genetating sequence 1')
            #move to first Player
            x, y =(967, 354)
            print(x, y)
            print('Choosing S1-1')
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()

            #move to Second Player
            x, y =(1258, 588)
            print(x, y)
            print('Choosing S1-2')
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()

            #Scrolling for third player
            x, y =(1340, 340)
            dragdistance=145
            print(x, y)
            print('Scrolling')
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()
            pyautogui.dragRel(0, dragdistance, duration=0.25)

            #move to third Player
            x, y =(1258, 511)
            print(x, y)
            print('Choosing S1-3')
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()

            # checking for previous used card
            im = pyautogui.screenshot()
            r,g,b = im.getpixel((1186,284))
            r2,g2,b2 = im.getpixel((1186,270))
            if (r==255 and g==192 and b==0) or (r2==255 and g2==192 and b2==0) :
                flag=2
                #move to first tab
                x, y =(741, 31)
                print(x, y)
                print('Moving to first tab')
                pyautogui.moveTo(x,y)
                pyautogui.click()
                #Reload first tab
                x, y =(788, 66)
                print(x, y)
                print('Reloading first tab')
                pyautogui.moveTo(x,y)
                pyautogui.click()
                time.sleep(10)
                r,g,b=(0,0,0)
                r2,g2,b2=(0,0,0)
                continue
           
            #move to House button
            x, y =(977, 206)
            print(x, y)
            print('Clicking House Button')
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()
            time.sleep(1.5)
            pyautogui.click()
            time.sleep(1.5)
            pyautogui.click()
            flag = 2

        elif flag == 2:
            # checking for previous used card
            im = pyautogui.screenshot()
            r,g,b = im.getpixel((1186,284))
            r2,g2,b2 = im.getpixel((1186,270))
            if (r==255 and g==192 and b==0) or (r2==255 and g2==192 and b2==0) :
                #move to first tab
                x, y =(741, 31)
                print(x, y)
                print('Moving to first tab')
                pyautogui.moveTo(x,y,duration=0.5)
                pyautogui.click()
                #Reload first tab
                x, y =(788, 66)
                print(x, y)
                print('Reloading first tab')
                pyautogui.moveTo(x,y,duration=0.5)
                pyautogui.click()
                time.sleep(13)
                r,g,b=(0,0,0)
                r2,g2,b2=(0,0,0)
                continue

            #Sequence S2
            print('Genetating sequence 2')
            #move to first Player
            x, y =(1110, 360)
            print(x, y)
            print('Choosing S2-1')
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()

            #Scrolling for third player
            x, y =(1340, 361)
            dragdistance=179
            print(x, y)
            print('Scrolling')
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()
            pyautogui.dragRel(0, dragdistance, duration=0.25)

            #move to Second Player
            x, y =(817, 395)
            print(x, y)
            print('Choosing S2-2')
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()

            #move to first Player
            x, y =(960, 614)
            print(x, y)
            print('Choosing S2-3')
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()

                       
            # checking for previous used card
            im = pyautogui.screenshot()
            r,g,b = im.getpixel((1186,284))
            r2,g2,b2 = im.getpixel((1186,270))
            if (r==255 and g==192 and b==0) or (r2==255 and g2==192 and b2==0) :
                flag=1
                #move to first tab
                x, y =(741, 31)
                print(x, y)
                print('Moving to first tab')
                pyautogui.moveTo(x,y)
                pyautogui.click()
                #Reload first tab
                x, y =(788, 66)
                print(x, y)
                print('Reloading first tab')
                pyautogui.moveTo(x,y)
                pyautogui.click()
                time.sleep(13)
                r,g,b=(0,0,0)
                r2,g2,b2=(0,0,0)
                continue

            #move to House button
            x, y =(977, 206)
            print(x, y)
            print('Clicking House Button')
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()
            time.sleep(1.5)
            pyautogui.click()
            time.sleep(1.5)
            pyautogui.click()           
            flag = 1

        #Now to screen 2- challange screen 
        time.sleep(2)
        #press challange button
        x, y =(1077, 488)
        print(x, y)
        print('Pressing challange button')
        pyautogui.moveTo(x,y,duration=0.5)
        pyautogui.click()
        time.sleep(2)
        pyautogui.click()
         
        time.sleep(8)
        #press Play again button
        x, y =(1037, 381)
        print(x, y)
        print('Pressing Play again button')
        pyautogui.moveTo(x,y,duration=0.5)
        pyautogui.click()
        time.sleep(1.5)
        pyautogui.click()
        loop2 = loop2-1
        print('Loop1:')
        print(loop1)
        print('Loop2:')
        print(loop2)
        time.sleep(7)
        




