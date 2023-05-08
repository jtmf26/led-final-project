import evdev

# There is a built-in test module available, just type this in a terminal:
#  python3 -m evdev.evtest

# Find all available devices
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

# Print out information on devices
for device in devices:
	print(device.path, device.name, device.phys)

# Once you know which device path, you can set up the device.
gamepad = evdev.InputDevice('/dev/input/event6')

# Below are very basic examples that are not debounced or anything
# the controller also supports events, which make debouncing easy,
# if you want that.

# Button Codes
# Button events are event type EV_KEY
# A 289		SELECT		296
# B 290		START		297
# X 288		L Shoulder	292
# Y 291		R Shoulder	293

def buttons(pad):
	keys = pad.active_keys()
	if 289 in keys:
		print('A')
		return 'A'
	if 290 in keys:
		print('B')
		return 'B'
	if 288 in keys:
		print('X')
		return 'X'
	if 291 in keys:
		print('Y')
		return 'Y'

# D-Pad uses type EV_ABS
# Left/Right: 	Code 0		Left value: 0	Right value: 	255
# Up/Down:		Code 1		Up value: 	0	Down value:		255
# Neutral value: 127

def d_pad(pad):
	if pad.absinfo(0).value == 0:
		print('LEFT')
		return 'LEFT'
	if pad.absinfo(0).value == 255:
		print('RIGHT')
		return 'RIGHT'
	
	if pad.absinfo(1).value == 0:
		print('UP')
		return 'UP'
	if pad.absinfo(1).value == 255:
		print('DOWN')
		return 'DOWN'


