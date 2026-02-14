def get_landing_stance(start_stance, rotation):
    if start_stance == "Regular":
        if abs(rotation)%180 == 0: 
            return "Goofy"
    if start_stance == "Goofy":
        if abs(rotation)%180 != 0:
            return "Regular"
        elif rotation%180 == 0 and rotation < 0:
            return "Regular"

    
    return start_stance

if __name__ == '__main__':
    print(get_landing_stance("Regular", 90))
    print()
    print(get_landing_stance("Regular", 180))
    print()
    print(get_landing_stance("Goofy", -270))
    print()
    print(get_landing_stance("Regular", 2340))
    print()
    print(get_landing_stance("Goofy", 2160))
    print()
    print(get_landing_stance("Goofy", -540))