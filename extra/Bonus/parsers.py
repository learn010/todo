def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inch = float(parts[1])
    return {"feet": feet , "inch":inch}
