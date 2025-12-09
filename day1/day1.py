def main():
    dial = 50
    min = 0
    max = 99
    base = 100
    zero_count = 0

    with open('day1input.txt', 'r') as file:
        for line in file:
            s = line.strip().upper()
            if not s:
                continue

            # Think you could do something with modulo (%) here but ¯\_(ツ)_/¯
            if s.startswith("R"):
                dial += int(s.removeprefix("R"))
                while dial > max:
                    dial -= base

            elif s.startswith("L"):
                dial -= int(s.removeprefix("L"))
                while dial < min:
                    dial += base

            if dial == 0:
                zero_count += 1

            print(s, dial)

    print('password:', zero_count) # 1191
    print('final:', dial) # 52

main()