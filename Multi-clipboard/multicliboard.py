import sys
import clipboard
import json

# Where I wanna save data dir
SAVED_DATA = "clipboard.json"

# Save items to json
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

# Load items from json
def load_data(filepath):
    # Check if that file doesn't exist
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        # Return empty dict
        return {}       

# To have a two command lines args
if len(sys.argv) == 2:
    command = sys.argv[1]
    # Load all data
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key: ")
        # Save dict
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")


