with open("results.txt", "w+") as f:
    while True:
        given = input()
        times = []
        pens = []
        if given.lower().strip() == "stop":
            break
        try:
            given = given.split("\t")
            name = given[0]
            id = given[1]

            f.write(name + "\t")

            given = given[2:]
            for i in range(0, 10, 2):
                time = given[i]
                pen = given[i+1]

                mins, temp = time.split(":")
                sec, ms = temp.split(".")

                mins = int(mins)
                sec = int(sec)

                sec += mins*60
                ms = "." + str(ms)

                curr = float(sec) + float(ms)
                if pen == "No Penalties":
                    times.append(curr)
                    f.write(str(time) + "\t")
                elif pen == "+2":
                    times.append(curr+2)
                    f.write(f"{time}+2\t")
                else:
                    times.append(-1)
                    f.write("DNF\t")
            times = sorted(times)
            print(times)

            if times[0] == -1:
                times = times[1:]
                if times[0] == -1:
                    print("ao5: DNF")
                    f.write("DNF")
                else:
                    times = times[1:]
                    print(f"ao5: {sum(times)/3:.2f}")
                    f.write(f"{sum(times)/3:.2f}")
            else:
                times = times[1:4]
                print(f"ao5: {sum(times)/3:.2f}")
                f.write(f"{sum(times)/3:.2f}")
            f.write("\n")
        except:
            print("error on something")
            continue
print("fin")
