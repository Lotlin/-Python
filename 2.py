time_user = int(input("Пожалуйста, введите время в секундах "))
hours = time_user // 360
minutes = (time_user - hours * 360) // 60
seconds = time_user - hours * 360 - minutes * 60
if hours // 10 == 0:
    hours = "0" + str(hours)  # не смогла придумать другого способа добавить 0 перед числом
if minutes // 10 == 0:
    minutes = "0" + str(minutes)
if seconds // 10 == 0:
    seconds = "0" + str(seconds)
print(f"{hours}:{minutes}:{seconds}")
