import dm

print(__name__, "= app.py's value")
# dm = dm.py's value
# __main__ = app.py's value

print("hello from app.py")
# hello from dm.py
# hello from app.py

# Once we added the if statement if __name__ == "__main__":
# it did not print the dm.py in the console when running app.py

# we can call anything we want from dm.py to run them :
dm.main()