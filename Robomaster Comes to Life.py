'''Robomaster S1 Comes to Life upgrade 3.0'''

# Make Robomaster S1 come to life. Simply copy or download this program example.

# You must copy and paste the program code into your Robomaster app. After that,
# simply click the blue play button, then clap your hands three times to wake him
# up. To make him sleep, simply tap any one of his bottom hit detectors.

# This Robomaster program example uses two powerful random generator options,
# the random.randint() and the random.choice() functions. These two, random
# generator functions are what make the Robomaster S1 come to life.

# To avoid damaging your Robomaster S1, never set any speeds higher than they
# are shown here, especially in smaller play areas. Note: be cautious when setting
# the drive_speed variable higher than 0.2 and the seconds variable, who's default
# is 1 second per drive time distance.

# IMPORTANT! Never pick up or move the Robomaster S1, while its program is
# running. Doing so may cause damage to the unit; you must stop the program first.

# Robomaster S1 features illustrated here are as follows:

# Robot Start
# Gimbal Free Mode
# Chassis Free Mode
# Chassis Follow Gimbal
# Scan Search with sound effect
# Blaster Fire with sound effect
# Sleep Mode
# Detection Applause
# Hit Detection

# Note: Gimbal Follow Chassis feature has been removed from this Robomaster S1 Python
# program example. However, I will be adding more Robomaster S1 features along the way.

# I sure hope other Robomaster people find this program very enjoyable and useful. I
# sure put a lot of time into creating it. It sure wasn't no cakewalk when the gimbal
# and chassis would conflict each other during practice execution/runs before I finally
# figured it all out.

robot=robot_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
media=media_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

rotate_speed=20,30,40,50,60
scan_speed=40;drive_speed=.2
wheel_degree=0,180,90,-90,45,-45,135,-135
l1,l2=0,255;blink_rate=2,3,4,5,6
seconds=1;a,b,c=1,2,3

def start():
    media.enable_sound_recognition(define.sound_detection_applause)
    armor.set_hit_sensitivity(10)
    
# Robot Start:

    def robot_start():
        led.gun_led_off()                
        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_breath)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_breath)
        gimbal.recenter()
        
        media.cond_wait(define.cond_sound_recognized_applause_thrice)
        
        led.set_flash(define.armor_all,1)
        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
        media.play_sound(define.media_sound_count_down,wait_for_complete_flag=True)
        gimbal.recenter()

# Gimbal Free Mode:

    def gimbal_free_mode():

        def gimbal_free_mode_right():

            robot.set_mode(define.robot_mode_free)

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_left,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_left,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)
                    
                    if commands_exit==a:continue
                    elif commands_exit==b:
                        robot.set_mode(define.robot_mode_chassis_follow)
                        break

        gimbal_free_mode_right()

        def gimbal_free_mode_left():

            robot.set_mode(define.robot_mode_free)

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_right,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_right,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.chassis_left,randrotate)
                    
                    if commands_exit==a:continue
                    elif commands_exit==b:
                        robot.set_mode(define.robot_mode_chassis_follow)
                        break

        gimbal_free_mode_left()

# Chassis Free Mode:

    def chassis_free_mode():

        def chassis_free_mode_right():

            robot.set_mode(define.robot_mode_free)

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_left,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_left,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    chassis.set_rotate_speed(randspeed)
                    chassis.rotate_with_degree(define.clockwise,randrotate)
                    
                    if commands_exit==a:continue
                    elif commands_exit==b:
                        robot.set_mode(define.robot_mode_chassis_follow)
                        break

        chassis_free_mode_right()

        def chassis_free_mode_left():
            
            robot.set_mode(define.robot_mode_free)

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_right,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_right,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    chassis.set_rotate_speed(randspeed)
                    chassis.rotate_with_degree(define.anticlockwise,randrotate)
                    
                    if commands_exit==a:continue
                    elif commands_exit==b:
                        robot.set_mode(define.robot_mode_chassis_follow)
                        break

        chassis_free_mode_left()

# Chassis Follow Gimbal:

    def chassis_follow_gimbal():

        def chassis_follow_gimbal_right():

            robot.set_mode(define.robot_mode_chassis_follow)

            while True:
                randspeed=random.choice(rotate_speed)
                randwheel=random.choice(wheel_degree)
                randrotate=random.randint(1,180)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=180:
                    led.set_top_led(define.armor_top_left,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_left,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,l2,l1,l1,define.effect_always_on)

                    chassis.set_trans_speed(drive_speed)
                    chassis.move_with_time(randwheel,seconds)

                    if randwheel==0:chassis.move_with_time(wheel_degree[1],seconds)
                    elif randwheel==180:chassis.move_with_time(wheel_degree[0],seconds)
                    elif randwheel==90:chassis.move_with_time(wheel_degree[3],seconds)
                    elif randwheel==-90:chassis.move_with_time(wheel_degree[2],seconds)
                    elif randwheel==45:chassis.move_with_time(wheel_degree[7],seconds)
                    elif randwheel==-45:chassis.move_with_time(wheel_degree[6],seconds)
                    elif randwheel==135:chassis.move_with_time(wheel_degree[5],seconds)
                    elif randwheel==-135:chassis.move_with_time(wheel_degree[4],seconds)
                    
                    if commands_exit==a:continue
                    elif commands_exit==b:
                        robot.set_mode(define.robot_mode_chassis_follow)
                        break

        chassis_follow_gimbal_right()

        def chassis_follow_gimbal_left():

            robot.set_mode(define.robot_mode_chassis_follow)

            while True:
                randspeed=random.choice(rotate_speed)
                randwheel=random.choice(wheel_degree)
                randrotate=random.randint(1,180)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=180:
                    led.set_top_led(define.armor_top_right,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_right,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_left,randrotate)

                    led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,l2,l1,l1,define.effect_always_on)

                    chassis.set_trans_speed(drive_speed)
                    chassis.move_with_time(randwheel,seconds)

                    if randwheel==0:chassis.move_with_time(wheel_degree[1],seconds)
                    elif randwheel==180:chassis.move_with_time(wheel_degree[0],seconds)
                    elif randwheel==90:chassis.move_with_time(wheel_degree[3],seconds)
                    elif randwheel==-90:chassis.move_with_time(wheel_degree[2],seconds)
                    elif randwheel==45:chassis.move_with_time(wheel_degree[7],seconds)
                    elif randwheel==-45:chassis.move_with_time(wheel_degree[6],seconds)
                    elif randwheel==135:chassis.move_with_time(wheel_degree[5],seconds)
                    elif randwheel==-135:chassis.move_with_time(wheel_degree[4],seconds)
                    
                    if commands_exit==a:continue
                    elif commands_exit==b:
                        robot.set_mode(define.robot_mode_chassis_follow)
                        break

        chassis_follow_gimbal_left()

# Scan Search:

    def scan_search():

        def scan_search_right():

            robot.set_mode(define.robot_mode_free)

            gimbal.set_rotate_speed(scan_speed)
            led.set_top_led(define.armor_top_all,l1,l2,l1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_all,l1,l2,l1,define.effect_breath)
            led.gun_led_on()

            while True:
                randgimbal_speed=random.randint(20,100)
                randrotate=random.randint(1,250)
                randangle=random.randint(-15,35)
                commands_exit=random.randint(a,b)

                gimbal.set_rotate_speed(randgimbal_speed)
                media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

                gimbal.set_rotate_speed(scan_speed)
                media.play_sound(define.media_sound_scanning,wait_for_complete_flag=False)
                gimbal.angle_ctrl(randrotate,randangle)
                
                if commands_exit==a:continue
                elif commands_exit==b:
                    gimbal.recenter()
                    led.gun_led_off()
                    break

        scan_search_right()

        def scan_search_left():

            robot.set_mode(define.robot_mode_free)

            gimbal.set_rotate_speed(scan_speed)
            led.set_top_led(define.armor_top_all,l1,l2,l1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_all,l1,l2,l1,define.effect_breath)
            led.gun_led_on()

            while True:
                randgimbal_speed=random.randint(20,100)
                randrotate=random.randint(-250,1)
                randangle=random.randint(-15,35)
                commands_exit=random.randint(a,b)

                gimbal.set_rotate_speed(randgimbal_speed)
                media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

                gimbal.set_rotate_speed(scan_speed)
                media.play_sound(define.media_sound_scanning,wait_for_complete_flag=False)
                gimbal.angle_ctrl(randrotate,randangle)
                
                if commands_exit==a:continue
                elif commands_exit==b:
                    gimbal.recenter()
                    led.gun_led_off()
                    break

        scan_search_left()

# Blaster Fire:

    def blaster_fire():

        robot.set_mode(define.robot_mode_free)

        while True:
            randgimbal_speed=random.randint(20,100)
            randup=random.randint(1,55)
            commands_exit=random.randint(a,b)

            gimbal.set_rotate_speed(randgimbal_speed)
            media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

            led.set_flash(define.armor_all,6)
            led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
            led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)

            gimbal.rotate_with_degree(define.gimbal_up,randup)

            led.set_flash(define.armor_all,8)
            led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_flash)
            led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_flash)

            media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
            media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
            
            if commands_exit==a:continue
            elif commands_exit==b:
                led.set_flash(define.armor_all,6)
                led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
                led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
                gimbal.recenter()
                break

# Sleep_mode:

    def sleep_mode():

        robot.set_mode(define.robot_mode_free)

        while True:
            randdelay=random.randint(1,4)
            commands_exit=random.randint(a,c)

            led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_back,l2,l1,l1,define.effect_breath)
            gimbal.recenter()
            time.sleep(randdelay)
            
            if commands_exit==a:continue
            elif commands_exit==b:break

    robot_start()      
    
    while True:
        randfunc=random.randint(1,5)
        randloop=random.randint(1,4)
        randscan=random.randint(1,15)
        
        if randfunc==1:
            for i in range(randloop):                    
                chassis_follow_gimbal()

        elif randfunc==2:gimbal_free_mode()
        elif randfunc==3:chassis_free_mode()
        elif randfunc==4:blaster_fire()
        elif randfunc==5:sleep_mode()

        if randscan==8:
            scan_search()
            
def armor_hit_detection_all(msg):    
    led.gun_led_off()
    led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_breath)
    led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_breath)
    gimbal.recenter()
    
    media.cond_wait(define.cond_sound_recognized_applause_thrice)
    
    led.set_flash(define.armor_all,1)
    led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
    led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
    media.play_sound(define.media_sound_count_down,wait_for_complete_flag=True)
    gimbal.recenter()
