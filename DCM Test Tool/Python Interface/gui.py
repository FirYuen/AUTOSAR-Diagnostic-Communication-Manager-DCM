import wx, webbrowser, com, serial
from parameters import *

def IsHex(x):
    return (x >= 48 and x < 58) or (x >= 97 and x < 103)

def ByteCharacterInput(key, box1, box2):
    if (IsHex(key)):
        box1.AppendText(chr(key))
        if (len(box1.GetValue()) >= 2):
            box2.SetFocus()

def ByteBoxFocus(box):
    if (len(box.GetValue())):
        box.Clear()

def UnfocusedByteBox(box):
    box.SetValue('0'*(2-len(box.GetValue())) + box.GetValue())

def SetNumber(box, value):
    if value == -1:
        box.SetValue(win_textbox_not_received)
        box.SetBackgroundColour(win_color_none)
    else:
        box.SetValue(str(value))
        box.SetBackgroundColour(win_color_norm)

class FrameMain(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self,
                          parent,
                          id=wx.ID_ANY,
                          title=win_title,
                          pos=wx.Point(winpos_x, winpos_y),
                          size=wx.Size(win_x, win_y),
                          style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize,
                          wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizerFrame = wx.GridBagSizer(0, 0)
        gbSizerFrame.SetFlexibleDirection(wx.BOTH)
        gbSizerFrame.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gbSizerFrame.SetEmptyCellSize(wx.Size(0, 0))

        gbSizerFrame.Add((0, 10), wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gbSizer_logo = wx.GridBagSizer(0, 0)
        gbSizer_logo.SetFlexibleDirection(wx.BOTH)
        gbSizer_logo.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gbSizer_logo.SetEmptyCellSize(wx.Size(100, 8))

        self.bitmap_logo = wx.StaticBitmap(self,
                                           wx.ID_ANY,
                                           wx.Bitmap(win_logo, wx.BITMAP_TYPE_ANY),
                                           wx.Point(100, 32),
                                           wx.DefaultSize, 0)

        gbSizer_logo.Add(self.bitmap_logo, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        gbSizer_title = wx.GridBagSizer(0, 0)
        gbSizer_title.SetFlexibleDirection(wx.BOTH)
        gbSizer_title.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gbSizer_title.SetEmptyCellSize(wx.Size(0, 12))

        self.label_title_university = wx.StaticText(self,
                                                    wx.ID_ANY,
                                                    win_title_0,
                                                    wx.DefaultPosition,
                                                    wx.Size(-1, -1),
                                                    wx.ALIGN_CENTER_HORIZONTAL)
        self.label_title_university.Wrap(-1)
        self.label_title_university.SetFont(wx.Font(24,
                                                    wx.FONTFAMILY_DEFAULT,
                                                    wx.FONTSTYLE_NORMAL,
                                                    wx.FONTWEIGHT_NORMAL,
                                                    False,
                                                    wx.EmptyString))

        gbSizer_title.Add(self.label_title_university, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.label_title_program = wx.StaticText(self,
                                                 wx.ID_ANY,
                                                 win_title_1,
                                                 wx.DefaultPosition,
                                                 wx.Size(-1, -1),
                                                 wx.ALIGN_CENTER_HORIZONTAL)
        self.label_title_program.Wrap(-1)
        self.label_title_program.SetFont(wx.Font(18,
                                                 wx.FONTFAMILY_DEFAULT,
                                                 wx.FONTSTYLE_NORMAL,
                                                 wx.FONTWEIGHT_NORMAL,
                                                 False,
                                                 wx.EmptyString))

        gbSizer_title.Add(self.label_title_program, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        gbSizer_logo.Add(gbSizer_title, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gbSizerFrame.Add(gbSizer_logo, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gbSizerMain = wx.GridBagSizer(0, 0)
        gbSizerMain.SetFlexibleDirection(wx.BOTH)
        gbSizerMain.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        gbSizer_leftSide = wx.GridBagSizer(0, 0)
        gbSizer_leftSide.SetFlexibleDirection(wx.BOTH)
        gbSizer_leftSide.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gbSizer_leftSide.SetEmptyCellSize(wx.Size(-1, 12))

        gbSizer_block0 = wx.GridBagSizer(0, 0)
        gbSizer_block0.SetFlexibleDirection(wx.BOTH)
        gbSizer_block0.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.label_lt0 = wx.StaticText(self,
                                       wx.ID_ANY,
                                       win_block0_label[0],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_lt0.Wrap(-1)

        self.label_lt0.SetMinSize(wx.Size(110, -1))

        gbSizer_block0.Add(self.label_lt0, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.label_lt1 = wx.StaticText(self, wx.ID_ANY,
                                       win_block0_label[1],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_lt1.Wrap(-1)

        self.label_lt1.SetMinSize(wx.Size(110, -1))

        gbSizer_block0.Add(self.label_lt1, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.label_lt2 = wx.StaticText(self, wx.ID_ANY,
                                       win_block0_label[2],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_lt2.Wrap(-1)

        self.label_lt2.SetMinSize(wx.Size(110, -1))

        gbSizer_block0.Add(self.label_lt2, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.textbox_lt0 = wx.TextCtrl(self, wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY)
        self.textbox_lt0.SetMinSize(wx.Size(250, -1))

        gbSizer_block0.Add(self.textbox_lt0, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_lt1 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY)
        self.textbox_lt1.SetMinSize(wx.Size(250, -1))

        gbSizer_block0.Add(self.textbox_lt1, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_lt2 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY)
        self.textbox_lt2.SetMinSize(wx.Size(250, -1))

        gbSizer_block0.Add(self.textbox_lt2, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        gbSizer_leftSide.Add(gbSizer_block0, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gbSizer_block1 = wx.GridBagSizer(0, 0)
        gbSizer_block1.SetFlexibleDirection(wx.BOTH)
        gbSizer_block1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gbSizer_block1.SetEmptyCellSize(wx.Size(0, 0))

        gbSizer1q = wx.GridBagSizer(0, 0)
        gbSizer1q.SetFlexibleDirection(wx.BOTH)
        gbSizer1q.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gbSizer1q.SetEmptyCellSize(wx.Size(0, 0))

        self.label_in = wx.StaticText(self, wx.ID_ANY, win_block1_label[0], wx.Point(-1, -1), wx.Size(-1, -1), wx.ALIGN_RIGHT)
        self.label_in.SetLabelMarkup(win_block1_label[0])
        self.label_in.Wrap(-1)

        self.label_in.SetMinSize(wx.Size(110, -1))

        gbSizer1q.Add(self.label_in, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.textbox_qh = wx.TextCtrl(self,
                                      wx.ID_ANY,
                                      win_hex_block,
                                      wx.DefaultPosition,
                                      wx.DefaultSize,
                                      wx.TE_READONLY)
        self.textbox_qh.SetMinSize(wx.Size(24, -1))
        self.textbox_qh.SetBackgroundColour(win_color_none)
        
        gbSizer1q.Add(self.textbox_qh, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_q0 = wx.TextCtrl(self, wx.ID_ANY, space, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.textbox_q0.SetMaxLength(2)
        self.textbox_q0.SetMinSize(wx.Size(24, -1))

        gbSizer1q.Add(self.textbox_q0, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_q1 = wx.TextCtrl(self, wx.ID_ANY, space, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textbox_q1.SetMaxLength(2)
        self.textbox_q1.SetMinSize(wx.Size(24, -1))

        gbSizer1q.Add(self.textbox_q1, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_q2 = wx.TextCtrl(self, wx.ID_ANY, space, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textbox_q2.SetMaxLength(2)
        self.textbox_q2.SetMinSize(wx.Size(24, -1))

        gbSizer1q.Add(self.textbox_q2, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_q3 = wx.TextCtrl(self, wx.ID_ANY, space, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textbox_q3.SetMaxLength(2)
        self.textbox_q3.SetMinSize(wx.Size(24, -1))

        gbSizer1q.Add(self.textbox_q3, wx.GBPosition(0, 5), wx.GBSpan(1, 1), wx.ALL, 2)

        gbSizer1q.Add((1, 0), wx.GBPosition(0, 6), wx.GBSpan(1, 1), wx.EXPAND, 5)

        self.btn_send = wx.Button(self, wx.ID_ANY, win_button[0], wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_send.SetLabelMarkup(win_button[0])
        self.btn_send.SetDefault()
        self.btn_send.SetMinSize(wx.Size(54, -1))

        gbSizer1q.Add(self.btn_send, wx.GBPosition(0, 7), wx.GBSpan(1, 1), wx.ALL, 0)

        gbSizer1q.Add((2, 0), wx.GBPosition(0, 8), wx.GBSpan(1, 1), wx.EXPAND, 5)

        self.btn_clear = wx.Button(self, wx.ID_ANY, win_button[1], wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_clear.SetLabelMarkup(win_button[1])
        self.btn_clear.SetMinSize(wx.Size(54, -1))

        gbSizer1q.Add(self.btn_clear, wx.GBPosition(0, 9), wx.GBSpan(1, 1), wx.ALL, 0)

        gbSizer_block1.Add(gbSizer1q, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gbSizer1s = wx.GridBagSizer(0, 0)
        gbSizer1s.SetFlexibleDirection(wx.BOTH)
        gbSizer1s.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gbSizer1s.SetEmptyCellSize(wx.Size(0, 0))

        self.label_out = wx.StaticText(self, wx.ID_ANY,
                                       win_block1_label[1],
                                       wx.DefaultPosition,
                                       wx.Size(-1, -1),
                                       wx.ALIGN_RIGHT)
        self.label_out.SetLabelMarkup(win_block1_label[1])
        self.label_out.Wrap(-1)

        self.label_out.SetMinSize(wx.Size(110, -1))

        gbSizer1s.Add(self.label_out, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.textbox_ss = []

        for i in range(9):
            self.textbox_ss.append(wx.TextCtrl(self,
                                          wx.ID_ANY,
                                          space,
                                          wx.DefaultPosition,
                                          wx.DefaultSize,
                                          wx.TE_READONLY))
            self.textbox_ss[i].SetMaxLength(2)
            self.textbox_ss[i].SetMinSize(wx.Size(24, -1))
            self.textbox_ss[i].SetBackgroundColour(win_color_fixed)
        
            gbSizer1s.Add(self.textbox_ss[i], wx.GBPosition(1, i+1), wx.GBSpan(1, 1), wx.ALL, 2)

        gbSizer_block1.Add(gbSizer1s, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gbSizer_leftSide.Add(gbSizer_block1, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.EXPAND, 0)

        gbSizer_block2 = wx.GridBagSizer(0, 0)
        gbSizer_block2.SetFlexibleDirection(wx.BOTH)
        gbSizer_block2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gbSizer_block2.SetEmptyCellSize(wx.Size(0, 0))

        self.label_lb0 = wx.StaticText(self,
                                       wx.ID_ANY,
                                       win_block2_label[0],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_lb0.Wrap(-1)

        self.label_lb0.SetMinSize(wx.Size(110, -1))

        gbSizer_block2.Add(self.label_lb0, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.label_lb1 = wx.StaticText(self,
                                       wx.ID_ANY,
                                       win_block2_label[1],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_lb1.Wrap(-1)

        self.label_lb1.SetMinSize(wx.Size(110, -1))

        gbSizer_block2.Add(self.label_lb1, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.label_lb2 = wx.StaticText(self,
                                       wx.ID_ANY,
                                       win_block2_label[2],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_lb2.Wrap(-1)

        self.label_lb2.SetMinSize(wx.Size(110, -1))

        gbSizer_block2.Add(self.label_lb2, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.textbox_lb0 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY)
        self.textbox_lb0.SetMinSize(wx.Size(250, -1))

        gbSizer_block2.Add(self.textbox_lb0, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_lb1 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY)
        self.textbox_lb1.SetMinSize(wx.Size(250, -1))

        gbSizer_block2.Add(self.textbox_lb1, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_lb2 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY)
        self.textbox_lb2.SetMinSize(wx.Size(250, -1))

        gbSizer_block2.Add(self.textbox_lb2, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        gbSizer_leftSide.Add(gbSizer_block2, wx.GBPosition(5, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gbSizerMain.Add(gbSizer_leftSide, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gbSizer_rightSide = wx.GridBagSizer(0, 0)
        gbSizer_rightSide.SetFlexibleDirection(wx.BOTH)
        gbSizer_rightSide.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gbSizer_rightSide.SetEmptyCellSize(wx.Size(-1, 12))

        gbSizer_block3 = wx.GridBagSizer(0, 0)
        gbSizer_block3.SetFlexibleDirection(wx.BOTH)
        gbSizer_block3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.label_rt0 = wx.StaticText(self,
                                       wx.ID_ANY,
                                       win_block3_label[0],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_rt0.Wrap(-1)

        self.label_rt0.SetMinSize(wx.Size(110, -1))

        gbSizer_block3.Add(self.label_rt0, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.label_rt1 = wx.StaticText(self, wx.ID_ANY,
                                       win_block3_label[1],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_rt1.Wrap(-1)

        self.label_rt1.SetMinSize(wx.Size(110, -1))

        gbSizer_block3.Add(self.label_rt1, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.label_rt2 = wx.StaticText(self,
                                       wx.ID_ANY,
                                       win_block3_label[2],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_rt2.Wrap(-1)

        self.label_rt2.SetMinSize(wx.Size(110, -1))

        gbSizer_block3.Add(self.label_rt2, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.label_rt3 = wx.StaticText(self,
                                       wx.ID_ANY,
                                       win_block3_label[3],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_rt3.Wrap(-1)

        self.label_rt3.SetMinSize(wx.Size(110, -1))

        gbSizer_block3.Add(self.label_rt3, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.textbox_rt0 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY | wx.TE_RIGHT)
        self.textbox_rt0.SetMinSize(wx.Size(100, -1))

        gbSizer_block3.Add(self.textbox_rt0, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rt1 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY | wx.TE_RIGHT)
        self.textbox_rt1.SetMinSize(wx.Size(100, -1))

        gbSizer_block3.Add(self.textbox_rt1, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rt2 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY | wx.TE_RIGHT)
        self.textbox_rt2.SetMinSize(wx.Size(100, -1))

        gbSizer_block3.Add(self.textbox_rt2, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rt3 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY | wx.TE_RIGHT)
        self.textbox_rt3.SetMinSize(wx.Size(100, -1))

        gbSizer_block3.Add(self.textbox_rt3, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rt0i = wx.TextCtrl(self,
                                        wx.ID_ANY,
                                        win_block3_info[0],
                                        wx.DefaultPosition,
                                        wx.DefaultSize,
                                        wx.TE_CENTER | wx.TE_READONLY)
        self.textbox_rt0i.SetMinSize(wx.Size(70, -1))
        self.textbox_rt0i.SetBackgroundColour(win_color_fixed)
        
        gbSizer_block3.Add(self.textbox_rt0i, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rt1i = wx.TextCtrl(self,
                                        wx.ID_ANY,
                                        win_block3_info[1],
                                        wx.DefaultPosition,
                                        wx.DefaultSize,
                                        wx.TE_CENTER | wx.TE_READONLY)
        self.textbox_rt1i.SetMinSize(wx.Size(70, -1))
        self.textbox_rt1i.SetBackgroundColour(win_color_fixed)

        gbSizer_block3.Add(self.textbox_rt1i, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rt2i = wx.TextCtrl(self,
                                        wx.ID_ANY,
                                        win_block3_info[2],
                                        wx.DefaultPosition,
                                        wx.DefaultSize,
                                        wx.TE_CENTER | wx.TE_READONLY)
        self.textbox_rt2i.SetMinSize(wx.Size(70, -1))
        self.textbox_rt2i.SetBackgroundColour(win_color_fixed)

        gbSizer_block3.Add(self.textbox_rt2i, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rt3i = wx.TextCtrl(self,
                                        wx.ID_ANY,
                                        win_block3_info[3],
                                        wx.DefaultPosition,
                                        wx.DefaultSize,
                                        wx.TE_CENTER | wx.TE_READONLY)
        self.textbox_rt3i.SetMinSize(wx.Size(70, -1))
        self.textbox_rt3i.SetBackgroundColour(win_color_fixed)

        gbSizer_block3.Add(self.textbox_rt3i, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.ALL, 2)

        gbSizer_rightSide.Add(gbSizer_block3, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gbSizer_block4 = wx.GridBagSizer(0, 0)
        gbSizer_block4.SetFlexibleDirection(wx.BOTH)
        gbSizer_block4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.label_rm0 = wx.StaticText(self,
                                       wx.ID_ANY,
                                       win_block4_label[0],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_rm0.Wrap(-1)

        self.label_rm0.SetMinSize(wx.Size(110, -1))

        gbSizer_block4.Add(self.label_rm0, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.textbox_rm0 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY | wx.TE_RIGHT)
        self.textbox_rm0.SetMinSize(wx.Size(100, -1))

        gbSizer_block4.Add(self.textbox_rm0, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rm0i = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       win_block4_info[0],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_CENTER | wx.TE_READONLY)
        self.textbox_rm0i.SetMinSize(wx.Size(70, -1))
        self.textbox_rm0i.SetBackgroundColour(win_color_fixed)
        
        gbSizer_block4.Add(self.textbox_rm0i, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 2)

        gbSizer_rightSide.Add(gbSizer_block4, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gbSizer_block5 = wx.GridBagSizer(0, 0)
        gbSizer_block5.SetFlexibleDirection(wx.BOTH)
        gbSizer_block5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.label_rb0 = wx.StaticText(self,
                                       wx.ID_ANY,
                                       win_block5_label[0],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_rb0.Wrap(-1)

        self.label_rb0.SetMinSize(wx.Size(110, -1))

        gbSizer_block5.Add(self.label_rb0, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.label_rb1 = wx.StaticText(self,
                                       wx.ID_ANY,
                                       wx.EmptyString,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_rb1.Wrap(-1)

        self.label_rb1.SetMinSize(wx.Size(110, -1))

        gbSizer_block5.Add(self.label_rb1, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.label_rb2 = wx.StaticText(self,
                                       wx.ID_ANY,
                                       win_block5_label[1],
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.ALIGN_RIGHT)
        self.label_rb2.Wrap(-1)

        self.label_rb2.SetMinSize(wx.Size(110, -1))

        gbSizer_block5.Add(self.label_rb2, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.textbox_rb0 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY | wx.TE_RIGHT)
        self.textbox_rb0.SetMinSize(wx.Size(100, -1))

        gbSizer_block5.Add(self.textbox_rb0, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rb1 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY | wx.TE_RIGHT)
        self.textbox_rb1.SetMinSize(wx.Size(100, -1))

        gbSizer_block5.Add(self.textbox_rb1, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rb2 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       space,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       wx.TE_READONLY | wx.TE_RIGHT)
        self.textbox_rb2.SetMinSize(wx.Size(100, -1))

        gbSizer_block5.Add(self.textbox_rb2, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rb0i = wx.TextCtrl(self,
                                        wx.ID_ANY,
                                        win_block5_info[0],
                                        wx.DefaultPosition,
                                        wx.DefaultSize,
                                        wx.TE_CENTER | wx.TE_READONLY)
        self.textbox_rb0i.SetMinSize(wx.Size(70, -1))
        self.textbox_rb0i.SetBackgroundColour(win_color_fixed)

        gbSizer_block5.Add(self.textbox_rb0i, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rb1i = wx.TextCtrl(self,
                                        wx.ID_ANY,
                                        win_block5_info[1],
                                        wx.DefaultPosition,
                                        wx.DefaultSize,
                                        wx.TE_CENTER | wx.TE_READONLY)
        self.textbox_rb1i.SetMinSize(wx.Size(70, -1))
        self.textbox_rb1i.SetBackgroundColour(win_color_fixed)

        gbSizer_block5.Add(self.textbox_rb1i, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL, 2)

        self.textbox_rb2i = wx.TextCtrl(self,
                                        wx.ID_ANY,
                                        win_block5_info[2],
                                        wx.DefaultPosition,
                                        wx.DefaultSize,
                                        wx.TE_CENTER | wx.TE_READONLY)
        self.textbox_rb2i.SetMinSize(wx.Size(70, -1))
        self.textbox_rb2i.SetBackgroundColour(win_color_fixed)

        gbSizer_block5.Add(self.textbox_rb2i, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL, 2)

        gbSizer_rightSide.Add(gbSizer_block5, wx.GBPosition(5, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gbSizerMain.Add(gbSizer_rightSide, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.EXPAND, 5)

        self.staticLine = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        gbSizerMain.Add(self.staticLine, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 5)

        gbSizerFrame.Add(gbSizerMain, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)
        
        self.label_appinfo = wx.StaticText(self, wx.ID_ANY, win_bottom_text, wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_appinfo.Wrap(-1)

        self.label_appinfo.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(),
                                            wx.FONTFAMILY_DEFAULT,
                                            wx.FONTSTYLE_NORMAL,
                                            wx.FONTWEIGHT_BOLD,
                                            False,
                                            wx.EmptyString))
        self.label_appinfo.SetForegroundColour(wx.Colour(255, 255, 255))
        
        gbSizerFrame.Add(self.label_appinfo, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.SetSizer(gbSizerFrame)
        self.Layout()
        self.menuBar = wx.MenuBar(0)
        self.menuBar.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(),
                                     wx.FONTFAMILY_DEFAULT,
                                     wx.FONTSTYLE_NORMAL,
                                     wx.FONTWEIGHT_NORMAL,
                                     False,
                                     wx.EmptyString))

        self.menu_file = wx.Menu()
        self.menuItem_new = wx.MenuItem(self.menu_file,
                                        wx.ID_ANY,
                                        win_menu_file[1],
                                        wx.EmptyString,
                                        wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuItem_new)

        self.menuItem_exit = wx.MenuItem(self.menu_file,
                                         wx.ID_ANY,
                                         win_menu_file[2],
                                         wx.EmptyString,
                                         wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuItem_exit)

        self.menuBar.Append(self.menu_file, win_menu_file[0])

        self.menu_help = wx.Menu()
        self.menuItem_i1 = wx.MenuItem(self.menu_help,
                                       wx.ID_ANY,
                                       win_menu_help[1],
                                       wx.EmptyString,
                                       wx.ITEM_NORMAL)
        self.menu_help.Append(self.menuItem_i1)

        self.menuItem_i2 = wx.MenuItem(self.menu_help,
                                       wx.ID_ANY,
                                       win_menu_help[2],
                                       wx.EmptyString,
                                       wx.ITEM_NORMAL)
        self.menu_help.Append(self.menuItem_i2)

        self.menuItem_i3 = wx.MenuItem(self.menu_help,
                                       wx.ID_ANY,
                                       win_menu_help[3],
                                       wx.EmptyString,
                                       wx.ITEM_NORMAL)
        self.menu_help.Append(self.menuItem_i3)

        self.menuBar.Append(self.menu_help, win_menu_help[0])

        self.menu_about = wx.Menu()
        self.menuItem_website = wx.MenuItem(self.menu_about,
                                            wx.ID_ANY,
                                            win_menu_about[1],
                                            wx.EmptyString,
                                            wx.ITEM_NORMAL)
        self.menu_about.Append(self.menuItem_website)

        self.menuBar.Append(self.menu_about, win_menu_about[0])

        self.SetMenuBar(self.menuBar)

        self.Centre(wx.BOTH)

        self.timer0 = wx.Timer(self, 0)
        self.Bind(wx.EVT_TIMER, self.check_connection, self.timer0)
        self.timer0.Start(100)    # 100 ms

        self.timer1 = wx.Timer(self, 1)
        self.Bind(wx.EVT_TIMER, self.check_receive, self.timer1)
        self.timer1.Start(25)     # 25 ms

        self.flag_connection = False
        self.flag_connection_repeat = True
        self.flag_no_connection_repeat = True

        self.num_of_rxbytes = 0
        self.num_of_rxmsgs = 0
        self.num_of_txmsgs = 0

        self.ecu_session = 0
        self.ecu_security = 0

        self.ecu_response = 0
        
        # Connect Events
        self.textbox_q0.Bind(wx.EVT_CHAR, self.q0_char)
        self.textbox_q1.Bind(wx.EVT_CHAR, self.q1_char)
        self.textbox_q2.Bind(wx.EVT_CHAR, self.q2_char)
        self.textbox_q3.Bind(wx.EVT_CHAR, self.q3_char)
        self.textbox_q0.Bind(wx.EVT_KILL_FOCUS, self.q0_unfocus)
        self.textbox_q1.Bind(wx.EVT_KILL_FOCUS, self.q1_unfocus)
        self.textbox_q2.Bind(wx.EVT_KILL_FOCUS, self.q2_unfocus)
        self.textbox_q3.Bind(wx.EVT_KILL_FOCUS, self.q3_unfocus)
        self.textbox_q0.Bind(wx.EVT_SET_FOCUS, self.q0_focus)
        self.textbox_q1.Bind(wx.EVT_SET_FOCUS, self.q1_focus)
        self.textbox_q2.Bind(wx.EVT_SET_FOCUS, self.q2_focus)
        self.textbox_q3.Bind(wx.EVT_SET_FOCUS, self.q3_focus)
        self.btn_send.Bind(wx.EVT_BUTTON, self.click_send)
        self.btn_clear.Bind(wx.EVT_BUTTON, self.click_clear)
        self.Bind(wx.EVT_MENU, self.click_new, id=self.menuItem_new.GetId())
        self.Bind(wx.EVT_MENU, self.click_exit, id=self.menuItem_exit.GetId())
        self.Bind(wx.EVT_MENU, self.click_help_1, id=self.menuItem_i1.GetId())
        self.Bind(wx.EVT_MENU, self.click_help_2, id=self.menuItem_i2.GetId())
        self.Bind(wx.EVT_MENU, self.click_help_3, id=self.menuItem_i3.GetId())
        self.Bind(wx.EVT_MENU, self.click_website, id=self.menuItem_website.GetId())

        self.click_new(None)
        
    def __del__(self):
        pass

    def check_receive(self, event):
        if (self.flag_connection):
            try:
                x = com.ser.readline().hex()
            except serial.SerialException:
                x = ""
            if len(x):
                x = x[:-2]
                self.ShowReceived(x)
                print(">> MESSAGE: 0x" + x + " is response.")
                self.SetReceivedMessages(1)
                self.SetReceivedBytes(len(x)//2)

                ############
                if x[:2] == "7f":
                    self.SetResponseStatus(2)
                    if len(x) > 4: 
                        if x[4:6] == "33":
                            self.SetNRC(1)
                        elif x[4:6] == "7f":
                            self.SetNRC(2)
                        elif x[4:6] == "35":
                            self.SetNRC(4)
                        elif x[4:6] == "36":
                            self.SetNRC(5)
                        else:
                            self.SetNRC(3)

                        if x[2:4] == "22":
                            self.SetRequestedService(3)
                        elif x[2:4] == "10":
                            self.SetRequestedService(1)
                        elif x[2:4] == "27":
                            self.SetRequestedService(2)
                        else:
                            self.SetRequestedService(0)
                    else:
                        self.SetNRC(3)
                else:
                    if x[:2] == "62":
                        self.SetRequestedService(3)
                    elif x[:2] == "50":
                        self.SetRequestedService(1)
                    elif x[:2] == "67":
                        self.SetRequestedService(2)
                    else:
                        self.SetRequestedService(0)
                        
                    self.SetResponseStatus(1)
                    self.SetNRC(0)
                    
                if x == '5002':
                    self.SetSession(2)
                    self.ecu_session = 1
                elif len(x) == 8 and x[:4] == "6701":
                    seed = int(x[4:], 16)
                    key = hex((seed ^ 0xffff) + 1)[2:]
                    print(">> MESSAGE: Security seed is 0x" + x[4:])
                    print(">> MESSAGE: Response key is 0x%s"%key)
                elif x == '6702':
                    self.ecu_security = 1
                    self.SetSecurityLevel(2)
                    print(">> MESSAGE: Security Lv.1 accessed!")
                elif x[:6] == "62f190":
                    rpm = int(x[6:10], 16)
                    tmp = int(x[10:12], 16)
                    prs = int(x[12:14], 16)
                    thr = int(x[16:18], 16)
                    
                    self.SetEngineSpeed(rpm)
                    self.SetTemperature(tmp)
                    self.SetPressure(prs)
                    self.SetThrottle(thr)
                    self.SetMassFlowRate(win_throttle)
                #############

    def check_connection(self, event):
        if not com.UpdateSerState():
            if self.flag_no_connection_repeat:
                if not self.flag_connection:
                    self.SetCable(0)
                else:
                    self.SetCable(2)
                    self.SetSession(0)
                    self.SetSecurityLevel(0)
                self.flag_connection, self.flag_connection_repeat, self.flag_no_connection_repeat = False, True, False
                print(console_text_not_connected)
        else:
            if self.flag_connection_repeat:
                self.SetSession(self.ecu_session+1)
                self.SetSecurityLevel(self.ecu_security+1)
                if self.flag_connection == False:
                    self.flag_connection = True
                    if com.EstablishConnection():
                        self.SetCable(1)
                    else:
                        print(console_text_failure)
                    
                self.flag_connection_repeat, self.flag_no_connection_repeat = False, True
                print(console_text_connected, com.GetComPort())
                print(console_text_line)
                

    def q0_unfocus(self, event):
        UnfocusedByteBox(self.textbox_q0)
        event.Skip()
        
    def q1_unfocus(self, event):
        UnfocusedByteBox(self.textbox_q1)
        event.Skip()
        
    def q2_unfocus(self, event):
        UnfocusedByteBox(self.textbox_q2)
        event.Skip()
        
    def q3_unfocus(self, event):
        UnfocusedByteBox(self.textbox_q3)
        event.Skip()
        
    def q0_char(self, event):
        ByteCharacterInput(event.GetKeyCode(), self.textbox_q0, self.textbox_q1)
        
    def q1_char(self, event):
        ByteCharacterInput(event.GetKeyCode(), self.textbox_q1, self.textbox_q2)
        
    def q2_char(self, event):
        ByteCharacterInput(event.GetKeyCode(), self.textbox_q2, self.textbox_q3)

    def q3_char(self, event):
        ByteCharacterInput(event.GetKeyCode(), self.textbox_q3, self.btn_send)
        
    def q0_focus(self, event):
        ByteBoxFocus(self.textbox_q0)
        event.Skip()
        
    def q1_focus(self, event):
        ByteBoxFocus(self.textbox_q1)
        event.Skip()
        
    def q2_focus(self, event):
        ByteBoxFocus(self.textbox_q2)
        event.Skip()
        
    def q3_focus(self, event):
        ByteBoxFocus(self.textbox_q3)
        event.Skip()
        
    def click_clear(self, event):
        self.textbox_q0.SetValue(win_empty_byte)
        self.textbox_q1.SetValue(win_empty_byte)
        self.textbox_q2.SetValue(win_empty_byte)
        self.textbox_q3.SetValue(win_empty_byte)
    
    def click_send(self, event):
        if self.flag_connection:
            buffer = self.textbox_q0.GetValue() + self.textbox_q1.GetValue() + \
                     self.textbox_q2.GetValue() + self.textbox_q3.GetValue()
            if (self.textbox_q0.GetValue() != "00"):
                number_of_bytes = 4
            elif (self.textbox_q1.GetValue() != "00"):
                number_of_bytes = 3
                buffer = buffer[2:]
            elif (self.textbox_q2.GetValue() != "00"):
                number_of_bytes = 2
                buffer = buffer[4:]
            elif (self.textbox_q3.GetValue() != "00"):
                number_of_bytes = 1
                buffer = buffer[6:]
            else:
                number_of_bytes = 0
                buffer = buffer[8:]

            buffer += eof
            number_of_bytes += 1
            if number_of_bytes > 1:
                for i in range(number_of_bytes):
                    pos = i*2
                    data_to_send = int(buffer[pos:pos+2], 16).to_bytes(1, byteorder='big')
                    com.ser.write(data_to_send)

                print(">> MESSAGE: 0x" + buffer[:-2] + " is sent.")
                self.SetSentMessages(1)
            else:
                print(">> MESSAGE: Empty message")
        else:
            print(console_text_cable_error)
            
    def click_new(self, event):
        self.SetFocus()

        self.flag_connection_repeat = True
        self.flag_no_connection_repeat = True
        
        self.click_clear(None)
        self.SetSession(0)
        self.SetSecurityLevel(0)
        self.SetRequestedService(0)
        self.SetResponseStatus(0)
        self.SetNRC(0)

        self.SetEngineSpeed(-1)
        self.SetTemperature(-1)
        self.SetPressure(-1)
        self.SetThrottle(-1)
        self.SetMassFlowRate(-1)

        self.num_of_rxbytes = 0
        self.num_of_rxmsgs = 0
        self.num_of_txmsgs = 0
        
        self.SetReceivedBytes(0)
        self.SetReceivedMessages(0)
        self.SetSentMessages(0)

        self.ShowReceived("")

    def click_exit(self, event):
        exit()
        event.Skip()

    def click_help_1(self, event):
        print("TODO: help #1")
        event.Skip()

    def click_help_2(self, event):
        print("TODO: help #2")
        event.Skip()

    def click_help_3(self, event):
        print("TODO: help #3")
        event.Skip()

    def click_website(self, event):
        webbrowser.open(website)
        event.Skip()

    def SetCable(self, index):
        self.textbox_lt0.SetValue(win_block0_box0[index])
        if (index == 0):
            self.textbox_lt0.SetBackgroundColour(win_color_warning)
        elif (index == 1):
            self.textbox_lt0.SetBackgroundColour(win_color_good)
        elif (index == 2):
            self.textbox_lt0.SetBackgroundColour(win_color_bad)
            
    def SetSession(self, index):
        self.textbox_lt1.SetValue(win_block0_box1[index])
        if (index == 0):
            self.textbox_lt1.SetBackgroundColour(win_color_none)
        elif (index == 1):
            self.textbox_lt1.SetBackgroundColour(win_color_norm)
        elif (index == 2):
            self.textbox_lt1.SetBackgroundColour(win_color_extended)

    def SetSecurityLevel(self, index):
        self.textbox_lt2.SetValue(win_block0_box2[index])
        if (index == 0):
            self.textbox_lt2.SetBackgroundColour(win_color_none)
        elif (index == 1):
            self.textbox_lt2.SetBackgroundColour(win_color_norm)
        elif (index == 2):
            self.textbox_lt2.SetBackgroundColour(win_color_blue)

    def SetRequestedService(self, index):
        self.textbox_lb0.SetValue(win_block2_box0[index])
        if (index == 0):
            self.textbox_lb0.SetBackgroundColour(win_color_none)
        elif (index == 1):
            self.textbox_lb0.SetBackgroundColour(win_color_norm)
        elif (index == 2):
            self.textbox_lb0.SetBackgroundColour(win_color_blue)
        elif (index == 3):
            self.textbox_lb0.SetBackgroundColour(win_color_norm)
            
    def SetResponseStatus(self, index):
        self.textbox_lb1.SetValue(win_block2_box1[index])
        if (index == 0):
            self.textbox_lb1.SetBackgroundColour(win_color_none)
        elif (index == 1):
            self.textbox_lb1.SetBackgroundColour(win_color_good)
        elif (index == 2):
            self.textbox_lb1.SetBackgroundColour(win_color_bad)
            
    def SetNRC(self, index):
        self.textbox_lb2.SetValue(win_block2_box2[index])
        if (index == 0):
            self.textbox_lb2.SetBackgroundColour(win_color_none)
        else:
            self.textbox_lb2.SetBackgroundColour(win_color_bad)

    def SetEngineSpeed(self, value):
        SetNumber(self.textbox_rt0, value)

    def SetTemperature(self, value):
        SetNumber(self.textbox_rt1, value)

    def SetPressure(self, value):
        SetNumber(self.textbox_rt2, value)

    def SetThrottle(self, value):
        SetNumber(self.textbox_rt3, value)

    def SetMassFlowRate(self, value):
        SetNumber(self.textbox_rm0, value)
        
    def SetReceivedBytes(self, value):
        self.num_of_rxbytes += value
        self.textbox_rb0.SetValue(str(self.num_of_rxbytes))

    def SetReceivedMessages(self, value):
        self.num_of_rxmsgs += value
        self.textbox_rb1.SetValue(str(self.num_of_rxmsgs))
        
    def SetSentMessages(self, value):
        self.num_of_txmsgs += value
        self.textbox_rb2.SetValue(str(self.num_of_txmsgs))

    def ShowReceived(self, buffer):
        buffer = buffer[:18]
        if len(buffer)%2:
            buffer = '0' + buffer
        stop = (len(buffer)+1)//2
        buffer = '0'*(9-stop)*2 + buffer
        for i in range(8, 8-stop, -1):
            pos = i*2
            self.textbox_ss[i].SetValue(buffer[pos:pos+2])
            self.textbox_ss[i].SetBackgroundColour(win_color_received)
        for i in range(9-stop):
            self.textbox_ss[i].SetValue(win_empty_byte)
            self.textbox_ss[i].SetBackgroundColour(win_color_none)
    
            
def StartApp():
    global app
    
    app = wx.App()
    FrameMain(None).Show(True)
    app.MainLoop()

