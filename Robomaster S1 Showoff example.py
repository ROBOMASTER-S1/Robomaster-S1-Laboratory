# Use a multi two dimensional list to loop through RGB colours. You need to
# add this empty list box [] at position 0, since the leds on the gimbal and the
# chassis start at 1 through 8 and 1 through 4. Note: no gimbal or chassis leds
# start at 0. If you want the gimbal leds to rotate backwards, simply create a
# reverse for-loop like this illustration shows: 'for i in range(8,0,-1):'. You must
# include the start value, the end value and the step value, -1. Always use
# negative integers in the step value to cause the for-loop to reverse looping.
# If you don't set the step value to a negative integer, the for-loop still runs,
# but nothing happens. Instead the program just does nothing for the duration of
# the loop iterations.

robot=robot_ctrl
led=led_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
media=media_ctrl
define=rm_define

rotate_speed=20,30,40,50,60
scan_speed=40;drive_speed=.0
wheel_degree=0,180,90,-90,45,-45,135,-135
l1,l2=0,50;blink_rate=2,3,4,5,6;a=1;b=2
seconds,milli_seconds=1,.1

RGB1=[
    [],         # Empty list box
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    ]

RGB2=[
    [],         # Empty list box
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    ]

robot.set_mode(define.robot_mode_gimbal_follow)
chassis.set_rotate_speed(rotate_speed[4])

led.turn_off(define.armor_all)
time.sleep(seconds+1)

for i in range(l1,l2):
    led.set_top_led(define.armor_top_all,
    i,i,i,define.effect_always_on)

    led.set_bottom_led(define.armor_bottom_all,
    i,i,i,define.effect_always_on)

for i in range(l2,l1,-1):
    led.set_top_led(define.armor_top_all,
    i,i,i,define.effect_always_on)

    led.set_bottom_led(define.armor_bottom_all,
    i,i,i,define.effect_always_on)

led.set_flash(define.armor_all,4)

chassis.rotate(define.clockwise)

for i in range(1,7):
    led.gun_led_on()
    led.set_top_led(define.armor_top_all,
    RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_always_off)

    led.set_bottom_led(define.armor_bottom_all,
    RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_flash)

    for i in range(1,9):
        led.set_single_led(define.armor_top_all,
        [i],define.effect_always_on)
        time.sleep(milli_seconds)

    for i in range(1,9):
        led.set_single_led(define.armor_top_all,
        [i],define.effect_always_off)
        time.sleep(milli_seconds)
        led.gun_led_off()

for x in range(0,2):
    led.gun_led_on()
    for i in range(1,9):
        led.set_top_led(define.armor_top_all,
        RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
        led.set_single_led(define.armor_top_all,
        [i],define.effect_always_on)

        led.set_bottom_led(define.armor_bottom_all,
        RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
        time.sleep(milli_seconds)
        led.gun_led_off()

for x in range(0,3):
    led.gun_led_on()
    for i in range(1,5):
        led.set_top_led(define.armor_top_all,
        RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
        led.set_single_led(define.armor_top_all,
        [i,i+4],define.effect_always_on)

        led.set_bottom_led(define.armor_bottom_all,
        RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
        time.sleep(milli_seconds)
        led.gun_led_off()

for x in range(0,7):
    led.gun_led_on()
    for i in range(1,3):
        led.set_top_led(define.armor_top_all,
        RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
        led.set_single_led(define.armor_top_all,
        [i,i+2,i+4,i+6],define.effect_always_on)

        led.set_bottom_led(define.armor_bottom_all,
        RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
        time.sleep(milli_seconds)
        led.gun_led_off()
        
chassis.rotate(define.anticlockwise)

for x in range(0,7):
    led.gun_led_on()
    for i in range(2,0,-1):
        led.set_top_led(define.armor_top_all,
        RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
        led.set_single_led(define.armor_top_all,
        [i,i+2,i+4,i+6],define.effect_always_on)

        led.set_bottom_led(define.armor_bottom_all,
        RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
        time.sleep(milli_seconds)
        led.gun_led_off()

for x in range(0,3):
    led.gun_led_on()
    for i in range(4,0,-1):
        led.set_top_led(define.armor_top_all,
        RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
        led.set_single_led(define.armor_top_all,
        [i,i+4],define.effect_always_on)

        led.set_bottom_led(define.armor_bottom_all,
        RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
        time.sleep(milli_seconds)
        led.gun_led_off()

for x in range(0,2):
    led.gun_led_on()
    for i in range(8,0,-1):
        led.set_top_led(define.armor_top_all,
        RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
        led.set_single_led(define.armor_top_all,
        [i],define.effect_always_on)

        led.set_bottom_led(define.armor_bottom_all,
        RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
        time.sleep(milli_seconds)
        led.gun_led_off()

led.set_flash(define.armor_all,4)

for i in range(1,7):
    led.gun_led_on()
    led.set_top_led(define.armor_top_all,
    RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_always_off)

    led.set_bottom_led(define.armor_bottom_all,
    RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_flash)

    for i in range(8,0,-1):
        led.set_single_led(define.armor_top_all,
        [i],define.effect_always_on)
        time.sleep(milli_seconds)

    for i in range(8,0,-1):
        led.set_single_led(define.armor_top_all,
        [i],define.effect_always_off)
        time.sleep(milli_seconds)
        led.gun_led_off()

led.turn_off(define.armor_all)
time.sleep(seconds+.6)
chassis.stop()

led.set_flash(define.armor_all,6)
led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
gimbal_ctrl.rotate(rm_define.gimbal_up)
media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)
time.sleep(seconds+.5)

led.set_flash(define.armor_all,8)
led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_flash)
led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_flash)

led.gun_led_on()
media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
led.turn_off(define.armor_all)
led.gun_led_off()

led.set_flash(define.armor_all,6)
led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
gimbal_ctrl.rotate(rm_define.gimbal_down)
media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)
time.sleep(seconds+.2)
led.turn_off(define.armor_all)
gimbal.recenter()
