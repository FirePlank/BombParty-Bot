from random import randint
import random
import keyboard as k
import time

def butterfinger(text, prob=5, keyboard='qwerty'):

	keyApprox = {}
	
	if keyboard == "qwerty":
		keyApprox['q'] = "qwasedzx"
		keyApprox['w'] = "wqesadrfcx"
		keyApprox['e'] = "ewrsfdqazxcvgt"
		keyApprox['r'] = "retdgfwsxcvgt"
		keyApprox['t'] = "tryfhgedcvbnju"
		keyApprox['y'] = "ytugjhrfvbnji"
		keyApprox['u'] = "uyihkjtgbnmlo"
		keyApprox['i'] = "iuojlkyhnmlp"
		keyApprox['o'] = "oipklujm"
		keyApprox['p'] = "plo['ik"

		keyApprox['a'] = "aqszwxwdce"
		keyApprox['s'] = "swxadrfv"
		keyApprox['d'] = "decsfaqgbv"
		keyApprox['f'] = "fdgrvwsxyhn"
		keyApprox['g'] = "gtbfhedcyjn"
		keyApprox['h'] = "hyngjfrvkim"
		keyApprox['j'] = "jhknugtblom"
		keyApprox['k'] = "kjlinyhn"
		keyApprox['l'] = "lokmpujn"

		keyApprox['z'] = "zaxsvde"
		keyApprox['x'] = "xzcsdbvfrewq"
		keyApprox['c'] = "cxvdfzswergb"
		keyApprox['v'] = "vcfbgxdertyn"
		keyApprox['b'] = "bvnghcftyun"
		keyApprox['n'] = "nbmhjvgtuik"
		keyApprox['m'] = "mnkjloik"
		keyApprox[' '] = " "
	else:
		print("Keyboard not supported.")
		return

	double_down = (False, "6969")
	faster_for_longer = 50 if len(text) >= 10 else 15
	for letter in text:
		typo = False
		lcletter = letter.lower()
		if not lcletter in keyApprox.keys():
			newletter = lcletter
		else:
			if random.choice(range(0, 100)) <= prob:
				newletter = random.choice(keyApprox[lcletter])
				typo = True
			else:
				newletter = lcletter

		if not typo:
			time.sleep(randint(0,100)/(450+faster_for_longer))
			k.write(newletter)
		else:
			if not double_down[0] and letter != text[-1]:
				chance = randint(1,3)
				if chance == 1 or chance == 2:
					time.sleep(randint(0,100)/450)
					k.write(newletter)
					double_down = (True, letter.lower())
					continue
				time.sleep(randint(0,100)/(450+faster_for_longer))
				k.write(newletter)
				time.sleep(randint(0,100)/400)
				k.press_and_release('backspace')
				time.sleep(randint(0,100)/480)
				k.write(letter.lower())
		
		if double_down[0]:
			time.sleep(randint(0,100)/325)
			k.press_and_release('backspace')
			time.sleep(randint(0,100)/525)
			k.press_and_release('backspace')
			time.sleep(randint(0,100)/480)
			k.write(double_down[1])
			time.sleep(randint(0,100)/(485+faster_for_longer))
			k.write(letter.lower())
			double_down = (False, "6969")