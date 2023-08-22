def timeConversion(s):
    # Write your code here
    hours = int(s[:2])
    c_hours = hours % 12
    if c_hours < 10:
        c_hours = "0"+str(c_hours)
    if s[-2] == "A":
        result = str(c_hours) + s[2:-2]
    else:
        c_hours = int(c_hours) + 12
        result = str(c_hours) + s[2:-2]
    return result
