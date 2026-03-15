try:
    with open('sample.txt','a+')as file:
        m = "do the work"
        c=file.write(m)
        d=file.read()
        print(c)
        print("content1:",d)
        file.seek(0)
        lines= file.readlines()
        print(lines)
except Exception as e:
    print(f"Error:{e}")