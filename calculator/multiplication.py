def mul(x:int,y:int):
    try:
        return x*y
    except Exception as e:
        return f"Something went wrong{e}"