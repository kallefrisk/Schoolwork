
# Set counting variables to zero
leftover, box, boxes = 0, 0, 0

for i in range(1, 101):
    leftover -= i           # Calculate the consumption of candles
    for j in range(i):
        if leftover < 0:    # If there are candles missing; buy 1 box
            leftover += 24  # Add 24 candles to leftover
            box += 1
            boxes += 1
            if leftover < 0:    # If there are still candles missing; repeat
                continue
        else:       # If there are enough candles; break the loop and return
            break
        print(f"Before birthday {i}, buy {box} box(es)")  # Print shopping list
        box = 0             # Reset temporary box counter after looping

print(f"Total number of boxes: {boxes}, remaining candles: {leftover}")
