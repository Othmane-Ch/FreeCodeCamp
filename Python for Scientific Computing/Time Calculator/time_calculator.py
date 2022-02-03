def add_time(start, duration, day_of_week = None):
    hours = 0
    minutes = 0
    day_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
    days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satuday", "Sunday"]

    start_list = start.split()  # ['3:34','AM']
    start_time = (start.split()[0]).split(':')  # ['3','34']
    start_hour = int(start_time[0])  # 3 h = 3 * 60
    start_minute = int(start_time[1])  # 34 m

    duration_time = (duration.split()[0]).split(':')
    duration_hour = int(duration_time[0])
    duration_minute = int(duration_time[1])

    minutes = (duration_minute + start_minute) % 60
    hours = duration_hour + start_hour + ((duration_minute + start_minute) // 60)
    if start_list[1] == 'PM':
        hours += 12
        days = hours // 24
        if (hours % 24) > 12:  # PM
            if minutes < 10 :
                if (hours %  12 )== 0:
                  new_time = "12:0" + str(minutes) + " PM"
                else :
                  new_time = str(hours %  12) + ":0" + str(minutes) + " PM"
            else :
                if hours % 12 == 0:
                  new_time = "12:" + str(minutes) + " PM"
                else :
                  new_time = str(hours %  12) + ":" + str(minutes) + " PM"

        else:  # AM
            if minutes < 10:
                if (hours %  12 )== 0:
                    new_time = "12:0" + str(minutes) + " AM"
                else :
                    new_time = str(hours % 12) + ":0" + str(minutes) + " AM"
            else :
                if (hours %  12 )== 0:
                    new_time = "12:" + str(minutes) + " AM"
                else :
                    new_time = str(hours % 12) + ":" + str(minutes) + " AM"



    else:
        days = hours // 24
        if (hours % 24) >= 12:  # PM
            if minutes < 10:
                if (hours % 12) == 0:
                    new_time = "12:0" + str(minutes) + " PM"
                else :
                    new_time = str(hours %  12) + ":0" + str(minutes) + " PM"
            else :
                if (hours % 12) == 0:
                    new_time = "12:0" + str(minutes) + " PM"
                else :
                    new_time = str(hours %  12) + ":" + str(minutes) + " PM"

        else:  # AM
            if minutes < 10:
                if (hours % 12) == 0:
                    new_time =  "12:0" + str(minutes) + " AM"
                else :
                    new_time = str(hours % 12) + ":0" + str(minutes) + " AM"

            else :
                if (hours % 12) == 0:
                    new_time =  "12:0" + str(minutes) + " AM"
                else :
                    new_time = str(hours % 12) + ":" + str(minutes) + " AM"


    if day_of_week == None:
        if days > 1:
            new_time += " (" + str(days) + " days later)"
        elif days == 1:
            new_time += " (next day)"
    else:
        string = day_of_week.lower()
        index = int((day_index[string] + days) % 7)
        if days > 1:
            new_time += ", " + days_list[index] + " (" + str(days) + " days later)"
        elif days == 1:
            new_time += ", " + days_list[index] + " (next day)"
        else:
            new_time += ", " + days_list[index]

    return new_time
