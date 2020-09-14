from inputs import get_gamepad
import datetime

def main():
	"""Just print out some event infomation when the gamepad is used."""
	while 1:
		events = get_gamepad()
		for event in events:
			if event.code == "ABS_X":
				if event.state == 255:
					print("right")
				if event.state == 0:
					print("left")


if __name__ == "__main__":
    main()
