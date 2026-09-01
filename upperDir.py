import os

def upperDir():
	for item in os.listdir('.'):
		if os.path.isdir(item):
			if item:
				newName = item[0].upper() + item [1:]
				if item != newName:
					os.rename(item, newName)
					print(f"Rename: '{item}? -> '{newName}'")
if __name__ == "__main__":
	upperDir()
