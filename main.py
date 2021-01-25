def my_function():
    global c, b, a, d, 次数
    c = 1
    b = 0
    a = 0
    d = 0
    microbot.microbot_init()
    microbot.clear_light()
    WonderCam.wondercam_init()
    WonderCam.change_func(WonderCam.Functions.CLASSIFICATION)
    次数 = 0
microbot.onremote_ir_pressed(microbot.IRKEY.R0, my_function)

def my_function2():
    global a, b, c, d
    microbot.microbot_init()
    WonderCam.wondercam_init()
    WonderCam.turn_on_or_off_led(WonderCam.LED_STATE.OFF)
    WonderCam.change_func(WonderCam.Functions.NO_FUNCTION)
    a = 0
    b = 0
    c = 0
    d = 0
    microbot.clear_light()
    microbot.belt_clearLight()
    microbot.set_motor_speed(0, 0)
microbot.onremote_ir_pressed(microbot.IRKEY.A, my_function2)

def my_function3():
    global b, c, a, d, 目标Y, 目标X
    b = 1
    c = 0
    a = 0
    d = 0
    microbot.microbot_init()
    WonderCam.wondercam_init()
    WonderCam.change_func(WonderCam.Functions.FACE_DETECT)
    WonderCam.turn_on_or_off_led(WonderCam.LED_STATE.ON)
    WonderCam.set_led_brightness(100)
    microbot.set_brightness(50)
    microbot.set_pixel_rgb(microbot.Lights.LIGHT6, RGBColors.INDIGO)
    microbot.set_pixel_rgb(microbot.Lights.LIGHT5, RGBColors.INDIGO)
    microbot.show_light()
    目标Y = 150
    目标X = 160
microbot.onremote_ir_pressed(microbot.IRKEY.R2, my_function3)

def my_function4():
    global d, a, b, c
    d = 1
    a = 0
    b = 0
    c = 0
    microbot.microbot_init()
    WonderCam.wondercam_init()
    WonderCam.change_func(WonderCam.Functions.LINE_FOLLOWING)
    WonderCam.turn_on_or_off_led(WonderCam.LED_STATE.ON)
    WonderCam.set_led_brightness(100)
    microbot.set_brightness(50)
    microbot.set_pixel_rgb(microbot.Lights.LIGHT5, RGBColors.WHITE)
    microbot.set_pixel_rgb(microbot.Lights.LIGHT6, RGBColors.WHITE)
    microbot.belt_setPixelRGB(microbot.LightsBelt.LIGHT1, RGBColors.WHITE)
    microbot.show_light()
microbot.onremote_ir_pressed(microbot.IRKEY.R3, my_function4)

def my_function5():
    global a, b, c, d, 目标Y, 目标X
    a = 1
    b = 0
    c = 0
    d = 0
    microbot.microbot_init()
    WonderCam.wondercam_init()
    WonderCam.change_func(WonderCam.Functions.COLOR_DETECT)
    WonderCam.turn_on_or_off_led(WonderCam.LED_STATE.ON)
    WonderCam.set_led_brightness(100)
    microbot.set_brightness(50)
    microbot.set_pixel_rgb(microbot.Lights.LIGHT6, RGBColors.WHITE)
    microbot.set_pixel_rgb(microbot.Lights.LIGHT5, RGBColors.WHITE)
    microbot.show_light()
    目标Y = 150
    目标X = 160
microbot.onremote_ir_pressed(microbot.IRKEY.R1, my_function5)

上次的偏移 = 0
转向速度1 = 0
偏移 = 0
夹角 = 0
结果 = 0
电机2速度 = 0
电机1速度 = 0
转向速度 = 0
前进速度 = 0
中心Y = 0
中心X = 0
目标X = 0
目标Y = 0
次数 = 0
d = 0
c = 0
b = 0
a = 0
microbot.microbot_init()
a = 0
b = 0
c = 0
d = 0

def on_forever():
    global 中心X, 中心Y, 前进速度, 转向速度, 电机1速度, 电机2速度, 次数, 结果
    if a == 1:
        WonderCam.update_result()
        if WonderCam.is_detected_color_id(1):
            中心X = WonderCam.xof_color_id(WonderCam.Options.POS_X, 1)
            中心Y = WonderCam.xof_color_id(WonderCam.Options.POS_Y, 1) + WonderCam.xof_color_id(WonderCam.Options.HEIGHT, 1) / 2
            if abs(目标Y - 中心Y) > 20:
                if 目标Y > 中心Y:
                    前进速度 = (目标Y - 中心Y) * 0.12
                else:
                    前进速度 = (目标Y - 中心Y) * 0.12
            else:
                前进速度 = 0
            前进速度 = Math.constrain(前进速度, -80, 80)
            if abs(目标X - 中心X) > 40:
                转向速度 = Math.constrain((目标X - 中心X) * 0.07, -30, 30)
            else:
                转向速度 = 0
            电机1速度 = Math.constrain(前进速度 - 转向速度, -100, 100)
            电机2速度 = Math.constrain(前进速度 + 转向速度, -100, 100)
            if 电机2速度 > 0:
                电机2速度 = Math.map(电机2速度, 0, 100, 10, 90)
            elif 电机2速度 < 0:
                电机2速度 = Math.map(电机2速度, 0, -100, -10, -90)
            else:
                电机2速度 = 0
            if 电机1速度 > 0:
                电机1速度 = Math.map(电机1速度, 0, 100, 10, 90)
            elif 电机1速度 < 0:
                电机1速度 = Math.map(电机1速度, 0, -100, -10, -90)
            else:
                电机1速度 = 0
            microbot.set_motor_speed(电机1速度, 电机2速度)
        else:
            电机1速度 = 0
            电机2速度 = 0
            microbot.set_motor_speed(电机1速度, 电机2速度)
    if b == 1:
        WonderCam.update_result()
        if WonderCam.is_detected_face(1):
            music.start_melody(music.built_in_melody(Melodies.RINGTONE), MelodyOptions.ONCE)
            中心X = WonderCam.getlearned_face_y(WonderCam.Options.POS_X, 1)
            中心Y = WonderCam.getlearned_face_y(WonderCam.Options.POS_Y, 1) + WonderCam.getlearned_face_y(WonderCam.Options.HEIGHT, 1) / 2
            if abs(目标Y - 中心Y) > 20:
                if 目标Y > 中心Y:
                    前进速度 = (目标Y - 中心Y) * 0.12
                else:
                    前进速度 = (目标Y - 中心Y) * 0.12
            else:
                前进速度 = 0
            前进速度 = Math.constrain(前进速度, -80, 80)
            if abs(目标X - 中心X) > 40:
                转向速度 = Math.constrain((目标X - 中心X) * 0.07, -30, 30)
            else:
                转向速度 = 0
            电机1速度 = Math.constrain(前进速度 - 转向速度, -100, 100)
            电机2速度 = Math.constrain(前进速度 + 转向速度, -100, 100)
            if 电机2速度 > 0:
                电机2速度 = Math.map(电机2速度, 0, 100, 10, 90)
            elif 电机2速度 < 0:
                电机2速度 = Math.map(电机2速度, 0, -100, -10, -90)
            else:
                电机2速度 = 0
            if 电机1速度 > 0:
                电机1速度 = Math.map(电机1速度, 0, 100, 10, 90)
            elif 电机1速度 < 0:
                电机1速度 = Math.map(电机1速度, 0, -100, -10, -90)
            else:
                电机1速度 = 0
            microbot.set_motor_speed(电机1速度, 电机2速度)
        else:
            电机1速度 = 0
            电机2速度 = 0
            microbot.set_motor_speed(电机1速度, 电机2速度)
    if c == 1:
        WonderCam.update_result()
        if WonderCam.max_confidence_id() == 结果 and WonderCam.max_confidence_id() != 1:
            次数 += 1
        else:
            次数 = 0
            microbot.set_motor_speed(15, 15)
        结果 = WonderCam.max_confidence_id()
        if 次数 > 3:
            microbot.set_motor_speed(0, 0)
            if 结果 == 4:
                microbot.set_motor_speed(-15, 15)
                basic.pause(500)
                microbot.set_motor_speed(0, 0)
                microbot.set_motor_speed(15, 15)
            if 结果 == 5:
                microbot.set_motor_speed(15, -15)
                basic.pause(500)
                microbot.set_motor_speed(0, 0)
                microbot.set_motor_speed(15, 15)
            if 结果 == 6:
                microbot.set_motor_speed(0, 0)
                basic.pause(2000)
            if 结果 == 7:
                microbot.set_motor_speed(15, -15)
                basic.pause(1000)
                microbot.set_motor_speed(0, 0)
                microbot.set_motor_speed(15, 15)
    if a == 0 and (b == 0 and c == 0):
        microbot.set_motor_speed(0, 0)
basic.forever(on_forever)

def on_forever2():
    global 夹角, 偏移, 转向速度1, 上次的偏移
    if d == 1:
        WonderCam.update_result()
        if WonderCam.is_detected_line_id(1):
            microbot.belt_setPixelRGB(microbot.LightsBelt.LIGHT1, RGBColors.BLUE)
            microbot.belt_showLight()
            夹角 = WonderCam.start_xof_line_id(WonderCam.Line_Options.THETA, 1)
            偏移 = WonderCam.start_xof_line_id(WonderCam.Line_Options.RHO, 1)
            转向速度1 = 偏移*0.02+(偏移-上次的偏移)*0.008+夹角+0.01
            上次的偏移 = 偏移
basic.forever(on_forever2)
