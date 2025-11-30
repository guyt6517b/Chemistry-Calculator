def bohr_animation_auto(symbol, atomic_number, electrons=0, loops=100, delay=0.0001):
    from helpers import clearscreen
    print(f"\nBohr Model Orbit Animation for {symbol.upper()} (atomic number: {atomic_number})\n")

    # distribute electrons with 2n^2 rule
    if not electrons:
        electrons = atomic_number
    else:
        electrons = electrons
    shells = []
    shell_num = 1
    while electrons > 0:
        max_in_shell = 2 * shell_num ** 2
        take = min(electrons, max_in_shell)
        shells.append(take)
        electrons -= take
        shell_num += 1

    radius_step = 3
    max_radius = len(shells) * radius_step
    size = max_radius * 2 + 5
    center = size // 2

    # give each electron an initial angle offset
    electron_angles = []
    for s_index, count in enumerate(shells):
        shell_radius = (s_index + 1) * radius_step
        for e_index in range(count):
            angle = 2 * math.pi * (e_index / count)
            electron_angles.append([shell_radius, angle, 0.15 + s_index * 0.05])  
            # [radius, angle, angular speed]

    try:
        for frame in range(loops):
            clear_screen()
            grid = [[" " for _ in range(size)] for _ in range(size)]

            # nucleus
            grid[center][center] = symbol.upper()

            # electrons
            for i, (radius, angle, speed) in enumerate(electron_angles):
                x = int(center + radius * math.cos(angle))
                y = int(center + radius * math.sin(angle))
                if 0 <= y < size and 0 <= x < size:
                    grid[y][x] = "e"
                # update angle for next frame
                electron_angles[i][1] += speed

            # print grid
            for row in grid:
                print("".join(row))
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nAnimation stopped.")