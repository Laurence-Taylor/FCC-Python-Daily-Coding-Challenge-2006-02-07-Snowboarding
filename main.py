def get_landing_stance(start_stance, rotation):
    if abs(rotation)%180 == 0 and start_stance == "Regular":
        return "Goofy"
    elif abs(rotation)%90 == 0 and start_stance == "Goofy":
            return "Regular"
    
    return start_stance

if __name__ == '__main__':
    #print(get_landing_stance("Regular", 90))
    #print()
    #print(get_landing_stance("Regular", 180))
    #print()
    #print(get_landing_stance("Goofy", -270))
    #print()
    #print(get_landing_stance("Regular", 2340))
    #print()
    print(get_landing_stance("Goofy", 2160))
    #print()
    #print(get_landing_stance("Goofy", -540))