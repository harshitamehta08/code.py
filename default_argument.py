def greet(name="harshu"):
    print("hello,", name)
    greet("mehta")
    greet()

    # list of 5 names skips "admin"
    names =["aman", "admin", "naren", "vinu", "kinu"]
    for name in names:
        if names == "admin":
          continue
        print(names)