import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import pandas


def bobot_proc(values):

	obj_size = ctrl.Antecedent(np.arange(146.981, 312.082, 33.020 ), 'size')
	bobot = ctrl.Consequent(np.arange(0.73, 1.55 , 0.1639), 'bobot') #bobot asli 0.164

	obj_size['1'] = fuzz.trimf(obj_size.universe,[ 113.961, 146.981, 180.001])
	obj_size['2'] = fuzz.trimf(obj_size.universe,[ 146.981, 180.001, 213.021])
	obj_size['3'] = fuzz.trimf(obj_size.universe,[ 180.001, 213.021, 246.041])
	obj_size['4'] = fuzz.trimf(obj_size.universe,[ 213.021, 246.041, 279.061])
	obj_size['5'] = fuzz.trimf(obj_size.universe,[ 246.041, 279.061, 312.081])
	obj_size['6'] = fuzz.trimf(obj_size.universe,[ 279.061, 312.081, 345.101])

	bobot['1'] = fuzz.trimf(bobot.universe,[0.566, 0.73, 0.894])
	bobot['2'] = fuzz.trimf(bobot.universe,[0.73, 0.894, 1.058])
	bobot['3'] = fuzz.trimf(bobot.universe,[0.894, 1.058, 1.222])
	bobot['4'] = fuzz.trimf(bobot.universe,[1.058, 1.222, 1.386])
	bobot['5'] = fuzz.trimf(bobot.universe,[1.222, 1.386, 1.55])
	bobot['6'] = fuzz.trimf(bobot.universe,[1.386, 1.55, 1.715])

	# Rules

	p1 = ctrl.Rule(obj_size['2'],bobot['1'])
	p2 = ctrl.Rule(obj_size['2'],bobot['1'])
	p3 = ctrl.Rule(obj_size['2'],bobot['1'])
	p4 = ctrl.Rule(obj_size['2'],bobot['1'])
	p5 = ctrl.Rule(obj_size['2'],bobot['2'])
	p6 = ctrl.Rule(obj_size['2'],bobot['2'])
	p7 = ctrl.Rule(obj_size['1'],bobot['2'])
	p8 = ctrl.Rule(obj_size['2'],bobot['2'])
	p9 = ctrl.Rule(obj_size['2'],bobot['2'])
	p10 = ctrl.Rule(obj_size['2'],bobot['2'])
	p11 = ctrl.Rule(obj_size['2'],bobot['2'])
	p12 = ctrl.Rule(obj_size['2'],bobot['2'])
	p13 = ctrl.Rule(obj_size['2'],bobot['2'])
	p14 = ctrl.Rule(obj_size['2'],bobot['2'])
	p15 = ctrl.Rule(obj_size['2'],bobot['2'])
	p16 = ctrl.Rule(obj_size['1'],bobot['2'])
	p17 = ctrl.Rule(obj_size['2'],bobot['2'])
	p18 = ctrl.Rule(obj_size['2'],bobot['2'])
	p19 = ctrl.Rule(obj_size['2'],bobot['2'])
	p20 = ctrl.Rule(obj_size['2'],bobot['2'])
	p21 = ctrl.Rule(obj_size['2'],bobot['2'])
	p22 = ctrl.Rule(obj_size['2'],bobot['2'])
	p23 = ctrl.Rule(obj_size['2'],bobot['2'])
	p24 = ctrl.Rule(obj_size['2'],bobot['2'])
	p25 = ctrl.Rule(obj_size['2'],bobot['2'])
	p26 = ctrl.Rule(obj_size['1'],bobot['2'])
	p27 = ctrl.Rule(obj_size['2'],bobot['2'])
	p28 = ctrl.Rule(obj_size['2'],bobot['2'])
	p29 = ctrl.Rule(obj_size['2'],bobot['2'])
	p30 = ctrl.Rule(obj_size['2'],bobot['2'])
	p31 = ctrl.Rule(obj_size['2'],bobot['2'])
	p32 = ctrl.Rule(obj_size['2'],bobot['2'])
	p33 = ctrl.Rule(obj_size['3'],bobot['2'])
	p34 = ctrl.Rule(obj_size['3'],bobot['2'])
	p35 = ctrl.Rule(obj_size['1'],bobot['2'])
	p36 = ctrl.Rule(obj_size['3'],bobot['2'])

	p37 = ctrl.Rule(obj_size['3'],bobot['3'])
	p38 = ctrl.Rule(obj_size['3'],bobot['3'])
	p39 = ctrl.Rule(obj_size['3'],bobot['3'])
	p40 = ctrl.Rule(obj_size['3'],bobot['3'])
	p41 = ctrl.Rule(obj_size['3'],bobot['3'])
	p42 = ctrl.Rule(obj_size['3'],bobot['3'])
	p43 = ctrl.Rule(obj_size['3'],bobot['3'])
	p44 = ctrl.Rule(obj_size['3'],bobot['3'])
	p45 = ctrl.Rule(obj_size['3'],bobot['3'])
	p46 = ctrl.Rule(obj_size['1'],bobot['3'])
	p47 = ctrl.Rule(obj_size['3'],bobot['3'])
	p48 = ctrl.Rule(obj_size['3'],bobot['3'])
	p49 = ctrl.Rule(obj_size['3'],bobot['3'])
	p50 = ctrl.Rule(obj_size['3'],bobot['3'])
	p51 = ctrl.Rule(obj_size['3'],bobot['3'])

	p52 = ctrl.Rule(obj_size['3'],bobot['4'])
	p53 = ctrl.Rule(obj_size['3'],bobot['4'])
	p54 = ctrl.Rule(obj_size['4'],bobot['4'])
	p55 = ctrl.Rule(obj_size['4'],bobot['4'])
	p56 = ctrl.Rule(obj_size['1'],bobot['4'])
	p57 = ctrl.Rule(obj_size['4'],bobot['4'])
	p58 = ctrl.Rule(obj_size['4'],bobot['4'])
	p59 = ctrl.Rule(obj_size['4'],bobot['4'])
	p60 = ctrl.Rule(obj_size['4'],bobot['4'])
	p61 = ctrl.Rule(obj_size['4'],bobot['4'])
	p62 = ctrl.Rule(obj_size['4'],bobot['4'])
	p63 = ctrl.Rule(obj_size['4'],bobot['4'])
	p64 = ctrl.Rule(obj_size['4'],bobot['4'])

	p65 = ctrl.Rule(obj_size['4'],bobot['5'])
	p66 = ctrl.Rule(obj_size['1'],bobot['5'])
	p67 = ctrl.Rule(obj_size['4'],bobot['5'])
	p68 = ctrl.Rule(obj_size['4'],bobot['5'])
	p69 = ctrl.Rule(obj_size['4'],bobot['5'])
	p70 = ctrl.Rule(obj_size['5'],bobot['5'])

	p71 = ctrl.Rule(obj_size['5'],bobot['6'])
	p72 = ctrl.Rule(obj_size['6'],bobot['6'])
	p73 = ctrl.Rule(obj_size['1'],bobot['6'])

	resulting_ctrl = ctrl.ControlSystem([
	    p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,
	    p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p37,p38,
	    p39,p40,p41,p42,p43,p44,p45,p46,p47,p48,p49,p50,p51,p52,p53,p54,p55,p56,
	    p57,p58,p59,p60,p61,p62,p63,p64,p65,p66,p67,p68,p69,p70,p71,p72,p73
	]) 
	resulting = ctrl.ControlSystemSimulation(resulting_ctrl)

	resulting.input['size'] = values
	resulting.compute()

	return resulting.output['bobot']
