#parameters

import wx

# GITHUB
website = "https://github.com/Aassem-Ibrahim/dcm-test-tool"

# GUI PARAMETERS
win_x = 718
win_y = 450
winpos_x = 10
winpos_y = 10

# GUI TEXT
win_title = "DCM Test Tool"
win_logo = "ain_shams_logo.bmp"
win_title_0 = "AIN SHAMS UNIVERSITY"
win_title_1 = "ASUSAR v2.0 - DCM Test Tool"
win_textbox_not_received = "Not Received"
win_block0_label = ("Cable:",
                    "Active Session:",
                    "Security Level:")
win_block1_label = ("Request:",
                    "Response (hex):")
win_block2_label = ("Requested Service:",
                    "Response Status:",
                    "NRC Info:")
win_block3_label = ("Engine Speed:",
                    "Air Temperature:",
                    "Intake Pressure:",
                    "Throttle Position:")
win_block4_label = ("Mass Flow Rate:",
                    "<\>")
win_block5_label = ("Received:",
                    "Sent:")
win_block3_info = ("RPM",
                   "°C",
                   "psi",
                   "%")
win_block4_info = ("g/s",
                   "<\>")
win_block5_info = ("Bytes",
                   "Messages",
                   "Messages")
win_block0_box0 = ("Make sure it is connected",
                   "Connected!",
                   "Disconnected!")
win_block0_box1 = ("None",
                   "Default",
                   "Extended")
win_block0_box2 = ("None",
                   "Unlocked",
                   "Level 1")
win_block2_box0 = ("None",
                   "Session Control",
                   "Security Access",
                   "Read Data by Identifier")
win_block2_box1 = ("None",
                   "Positive Response (+ve)",
                   "Negative Response (-ve)")
win_block2_box2 = ("None",
                   "Security access denied!",
                   "Service not supported in active session!",
                   "General reject!",
                   "Security key mismatch!",
                   "Number of attempts exceeded!")

win_throttle = '4.7812'
win_menu_file = ("File",
                 "New",
                 "Exit")
win_menu_help = ("Help",
                 "Receive Message",
                 "Receive HEX",
                 "Not programmed")
win_menu_about = ("About",
                 "Source Code [Github]")
win_button = ("Send",
              "Clear")
win_hex_block = "0x"
win_empty_byte = "00"
win_empty_number_box = '0'
win_info1 = 'Supervised by Prof. Dr. Sherif Hammad and Eng. M. Abdelhay'
win_info2 = 'ASUSAR v2.0, 2020'
win_bottom_text = ' '*8 + win_info1 + ' '*67 + win_info2

win_color_norm = wx.Colour(240, 240, 240)
win_color_none = wx.Colour(180, 180, 180)
win_color_warning = wx.Colour(255, 238, 122)
win_color_good = wx.Colour(166, 255, 166)
win_color_bad = wx.Colour(255, 166, 166)
win_color_blue = wx.Colour(166, 166, 255)
win_color_fixed = wx.Colour(230, 230, 230)
win_color_received = wx.Colour(255, 220, 160)
win_color_extended = wx.Colour(248, 253, 179)

eof = "00"
space = ' '

# CONSOLE
check_connection_time = 0.4  #in seconds
console_text_not_connected = ">> MESSAGE: Make sure ECU (TIVA-C) is connected!"
console_text_connected = "\nConnecting to ECU (TIVA-C) through"
console_text_line = '-' * (len(console_text_connected) + 5)
console_text_failure = "Press 'Enter' to exit "
console_text_cable_error = ">> MESSAGE (ERR): Cable not connected!"
# COM
com_device_name = "Stellaris Virtual Serial Port"
com_baudrate = 115200
