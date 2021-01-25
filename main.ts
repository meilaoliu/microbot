microbot.onremote_ir_pressed(microbot.IRKEY.R0, function () {
    c = 1
    b = 0
    a = 0
    d = 0
    microbot.microbotInit()
    microbot.clearLight()
    WonderCam.wondercam_init()
    WonderCam.ChangeFunc(WonderCam.Functions.Classification)
    次数 = 0
})
microbot.onremote_ir_pressed(microbot.IRKEY.A, function () {
    microbot.microbotInit()
    WonderCam.wondercam_init()
    WonderCam.TurnOnOrOffLed(WonderCam.LED_STATE.OFF)
    WonderCam.ChangeFunc(WonderCam.Functions.NoFunction)
    a = 0
    b = 0
    c = 0
    d = 0
    microbot.clearLight()
    microbot.belt_clearLight()
    microbot.setMotorSpeed(0, 0)
})
microbot.onremote_no_ir(function () {
    microbot.setMotorSpeed(0, 0)
})
microbot.onremote_ir_pressed(microbot.IRKEY.R6, function () {
    microbot.setMotorSpeed(-15, 15)
})
microbot.onremote_ir_pressed(microbot.IRKEY.LEFT, function () {
    microbot.setMotorSpeed(20, 40)
})
microbot.onremote_ir_pressed(microbot.IRKEY.R2, function () {
    b = 1
    c = 0
    a = 0
    d = 0
    microbot.microbotInit()
    WonderCam.wondercam_init()
    WonderCam.ChangeFunc(WonderCam.Functions.FaceDetect)
    WonderCam.TurnOnOrOffLed(WonderCam.LED_STATE.ON)
    WonderCam.SetLedBrightness(100)
    microbot.setBrightness(50)
    microbot.setPixelRGB(microbot.Lights.Light6, RGBColors.Indigo)
    microbot.setPixelRGB(microbot.Lights.Light5, RGBColors.Indigo)
    microbot.showLight()
    目标Y = 150
    目标X = 160
})
microbot.onremote_ir_pressed(microbot.IRKEY.RIGHT, function () {
    microbot.setMotorSpeed(40, 20)
})
microbot.onremote_ir_pressed(microbot.IRKEY.R3, function () {
    d = 1
    a = 0
    b = 0
    c = 0
    microbot.microbotInit()
    WonderCam.wondercam_init()
    WonderCam.ChangeFunc(WonderCam.Functions.LineFollowing)
    WonderCam.TurnOnOrOffLed(WonderCam.LED_STATE.ON)
    WonderCam.SetLedBrightness(100)
    microbot.setBrightness(50)
    microbot.setPixelRGB(microbot.Lights.Light5, RGBColors.White)
    microbot.setPixelRGB(microbot.Lights.Light6, RGBColors.White)
    microbot.belt_setPixelRGB(microbot.LightsBelt.Light1, RGBColors.White)
    microbot.showLight()
})
microbot.onremote_ir_pressed(microbot.IRKEY.R1, function () {
    a = 1
    b = 0
    c = 0
    d = 0
    microbot.microbotInit()
    WonderCam.wondercam_init()
    WonderCam.ChangeFunc(WonderCam.Functions.ColorDetect)
    WonderCam.TurnOnOrOffLed(WonderCam.LED_STATE.ON)
    WonderCam.SetLedBrightness(100)
    microbot.setBrightness(50)
    microbot.setPixelRGB(microbot.Lights.Light6, RGBColors.White)
    microbot.setPixelRGB(microbot.Lights.Light5, RGBColors.White)
    microbot.showLight()
    目标Y = 150
    目标X = 160
})
microbot.onremote_ir_pressed(microbot.IRKEY.UP, function () {
    microbot.setMotorSpeed(30, 30)
})
let 结果 = 0
let 电机2速度 = 0
let 电机1速度 = 0
let 转向速度 = 0
let 前进速度 = 0
let 中心Y = 0
let 中心X = 0
let 目标X = 0
let 目标Y = 0
let 次数 = 0
let d = 0
let c = 0
let b = 0
let a = 0
microbot.microbotInit()
a = 0
b = 0
c = 0
d = 0
basic.forever(function () {
    if (a == 1) {
        WonderCam.UpdateResult()
        if (WonderCam.isDetectedColorId(1)) {
            中心X = WonderCam.XOfColorId(WonderCam.Options.Pos_X, 1)
            中心Y = WonderCam.XOfColorId(WonderCam.Options.Pos_Y, 1) + WonderCam.XOfColorId(WonderCam.Options.Height, 1) / 2
            if (Math.abs(目标Y - 中心Y) > 20) {
                if (目标Y > 中心Y) {
                    前进速度 = (目标Y - 中心Y) * 0.12
                } else {
                    前进速度 = (目标Y - 中心Y) * 0.12
                }
            } else {
                前进速度 = 0
            }
            前进速度 = Math.constrain(前进速度, -80, 80)
            if (Math.abs(目标X - 中心X) > 40) {
                转向速度 = Math.constrain((目标X - 中心X) * 0.07, -30, 30)
            } else {
                转向速度 = 0
            }
            电机1速度 = Math.constrain(前进速度 - 转向速度, -100, 100)
            电机2速度 = Math.constrain(前进速度 + 转向速度, -100, 100)
            if (电机2速度 > 0) {
                电机2速度 = Math.map(电机2速度, 0, 100, 10, 90)
            } else if (电机2速度 < 0) {
                电机2速度 = Math.map(电机2速度, 0, -100, -10, -90)
            } else {
                电机2速度 = 0
            }
            if (电机1速度 > 0) {
                电机1速度 = Math.map(电机1速度, 0, 100, 10, 90)
            } else if (电机1速度 < 0) {
                电机1速度 = Math.map(电机1速度, 0, -100, -10, -90)
            } else {
                电机1速度 = 0
            }
            microbot.setMotorSpeed(电机1速度, 电机2速度)
        } else {
            电机1速度 = 0
            电机2速度 = 0
            microbot.setMotorSpeed(电机1速度, 电机2速度)
        }
    }
    if (b == 1) {
        WonderCam.UpdateResult()
        if (WonderCam.IsDetectedFace(1)) {
            music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.Once)
            中心X = WonderCam.getlearnedFaceY(WonderCam.Options.Pos_X, 1)
            中心Y = WonderCam.getlearnedFaceY(WonderCam.Options.Pos_Y, 1) + WonderCam.getlearnedFaceY(WonderCam.Options.Height, 1) / 2
            if (Math.abs(目标Y - 中心Y) > 20) {
                if (目标Y > 中心Y) {
                    前进速度 = (目标Y - 中心Y) * 0.12
                } else {
                    前进速度 = (目标Y - 中心Y) * 0.12
                }
            } else {
                前进速度 = 0
            }
            前进速度 = Math.constrain(前进速度, -80, 80)
            if (Math.abs(目标X - 中心X) > 40) {
                转向速度 = Math.constrain((目标X - 中心X) * 0.07, -30, 30)
            } else {
                转向速度 = 0
            }
            电机1速度 = Math.constrain(前进速度 - 转向速度, -100, 100)
            电机2速度 = Math.constrain(前进速度 + 转向速度, -100, 100)
            if (电机2速度 > 0) {
                电机2速度 = Math.map(电机2速度, 0, 100, 10, 90)
            } else if (电机2速度 < 0) {
                电机2速度 = Math.map(电机2速度, 0, -100, -10, -90)
            } else {
                电机2速度 = 0
            }
            if (电机1速度 > 0) {
                电机1速度 = Math.map(电机1速度, 0, 100, 10, 90)
            } else if (电机1速度 < 0) {
                电机1速度 = Math.map(电机1速度, 0, -100, -10, -90)
            } else {
                电机1速度 = 0
            }
            microbot.setMotorSpeed(电机1速度, 电机2速度)
        } else {
            电机1速度 = 0
            电机2速度 = 0
            microbot.setMotorSpeed(电机1速度, 电机2速度)
        }
    }
    if (c == 1) {
        WonderCam.UpdateResult()
        if (WonderCam.MaxConfidenceID() == 结果 && WonderCam.MaxConfidenceID() != 1) {
            次数 += 1
        } else {
            次数 = 0
            microbot.setMotorSpeed(15, 15)
        }
        结果 = WonderCam.MaxConfidenceID()
        if (次数 > 3) {
            microbot.setMotorSpeed(0, 0)
            if (结果 == 4) {
                microbot.setMotorSpeed(-15, 15)
                basic.pause(500)
                microbot.setMotorSpeed(0, 0)
                microbot.setMotorSpeed(15, 15)
            }
            if (结果 == 5) {
                microbot.setMotorSpeed(15, -15)
                basic.pause(500)
                microbot.setMotorSpeed(0, 0)
                microbot.setMotorSpeed(15, 15)
            }
            if (结果 == 6) {
                microbot.setMotorSpeed(0, 0)
                basic.pause(2000)
            }
            if (结果 == 7) {
                microbot.setMotorSpeed(15, -15)
                basic.pause(1000)
                microbot.setMotorSpeed(0, 0)
                microbot.setMotorSpeed(15, 15)
            }
        }
    }
})
basic.forever(function () {
    if (d == 1) {
        WonderCam.UpdateResult()
        if (WonderCam.isDetectedLineId(1)) {
            microbot.belt_setPixelRGB(microbot.LightsBelt.Light1, RGBColors.Blue)
            microbot.belt_showLight()
        }
    }
})
