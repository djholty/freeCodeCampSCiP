def add_time(starttime, duration, startday = None):
    
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    #access starting time hours, min, duration hours, mins, and AM/PM
    hourminstart, ampmstart = starttime.split(" ")
    hourstart, minstart = hourminstart.split(":")
    hoursdur, mindur = duration.split(":")
    

    #Need to roll over minutes into hours if there are more than 60
    if ( int(mindur) + int(minstart) ) >= 60 :
        addedmin = int(mindur) + int(minstart) #add minutes duration plus minutes of the time
        addedminhour = int(addedmin/60) #find how many hours the minutes column add up to 
        finalmins = addedmin%60 # final minutes
        finalhours = int(hourstart) + int(addedminhour)+ int(hoursdur)
    else:
        finalmins = int(mindur) + int(minstart)
        finalhours = int(hourstart) + int(hoursdur)

    if ampmstart =="AM":
        finalhours = finalhours
    if ampmstart =="PM":
        finalhours = finalhours + 12

    #convert final hours to a 24 hour clock to determine number of days later
    days = int(finalhours/24)
    dayslater =  None
    if days == 1:
        dayslater = "(next day)"
    if days > 1:
        dayslater = f"({days} days later)"
    print("Days: ", days)
    hours24 = finalhours%24 #convert time to 24 hour clock
    print(f"Hours24: {hours24}")
    
    if hours24 > 12 and hours24 < 24:
        hours12 = hours24 - 12
    elif hours24 == 0:
        hours12 = 12
    else:
        hours12 =  hours24
    print(f"Hours12: {hours12}" )
    
    if hours24 >= 12 and hours24 < 24:
        ampmend = "PM"
    else:
        ampmend = "AM"

    if startday is not None:
        index = weekdays.index(startday.lower().capitalize())
        newdayindex = (index + days) % 7 
        print("Newday Index: ", newdayindex)
        weekday = weekdays[newdayindex]
        print(weekday)

        print("Index: ", index)
    if startday is None:   

        if days < 1:
            new_time = f"{hours12}:{finalmins:02} {ampmend}"
        if days == 1: 
            new_time = f"{hours12}:{finalmins:02} {ampmend} {dayslater}"
        if days > 1:
            new_time = f"{hours12}:{finalmins:02} {ampmend} {dayslater}" 

    else:
        if days < 1:
            new_time = f"{hours12}:{finalmins:02} {ampmend}, {weekday}"
        if days == 1: 
            new_time = f"{hours12}:{finalmins:02} {ampmend}, {weekday} {dayslater}"
        if days > 1:
            new_time = f"{hours12}:{finalmins:02} {ampmend}, {weekday} {dayslater}" 


    return new_time
