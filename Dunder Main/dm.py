def gather_ingredients():
    print("Bread, jelly, and peanut butter gathered.")

def combine_ingredients():
    print("Add peanut butter and jelly to slices and put them together.")

def main():
    gather_ingredients()
    combine_ingredients()

print(__name__, "= dm.py's value") # __main__ = dm.py's value

if __name__ == "__main__":
    print("hello from dm.py")
    main()


# adding this if statement code block insures it will run it if it's the main file being run
# So when imported to another like the app.py, it won't run, as we don't want to have many things just activate, but rather things we want.
