from json import dumps
from httplib2 import Http

answer = 0
# Copy the webhook URL from the Chat space where the webhook is registered.
# The values for SPACE_ID, KEY, and TOKEN are set by Chat, and are included
# when you copy the webhook URL.
print("Which character?")
print("")
print("1 - Spoon Man (Furry GC)")
print("2")
answer = int(input("Select > "))

def main(message):
    """Google Chat incoming webhook quickstart."""
    url = "https://chat.googleapis.com/v1/spaces/AAAAjizvuN0/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=t_SA4hGw_3_nyj7wOAyP6OBsaK9JVH3Tr9OEY2-lb2o"
    app_message = {"text": message}
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(app_message),
    )

def nugget(message):
    """Google Chat incoming webhook quickstart."""
    url = "https://chat.googleapis.com/v1/spaces/AAAAV4_12fE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=M35_meD30AA27rq-jd7PMe_sX53ZA_FvpbvB8GkAO-0"
    app_message = {"text": message}
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(app_message),
    )


loop = True
while loop:
    if answer == 1:
        main(input("> "))
    elif answer == 2:
        nugget(input("> "))
