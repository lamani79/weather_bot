import get_weather
import send_message

from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == '__main__':
    print('form main')

    # get_weather.display_data()
    # send_message.send_message("whatsapp","hello form main")


    yasser_id = "4175433945889126"
    mama_id = "4340565582699536"
    ihabe_id = ""
    walid_id = "6199173423457278"

    def job_function():
        # #send to whatsapp:
        #to yasser (me)
        send_message.send_message("whatsapp",get_weather.display_data(),)

        #send to messanger:

        #to yasser (me)
        send_message.client_id = yasser_id
        send_message.send_message("messanger",get_weather.display_data())

        #to MaMa
        send_message.client_id = mama_id
        send_message.send_message("messanger",get_weather.display_data())

        # #to Ihabe
        # send_message.client_id = ihabe_id
        # send_message.send_message("messanger",get_weather.display_data())

        #to Walid
        send_message.client_id = walid_id
        send_message.send_message("messanger",get_weather.display_data())

        print("Myaw from Yasser \n Take care!")

    sched = BlockingScheduler()

    # Schedule job_function to be called every ...
    sched.add_job(job_function, 'interval', hours =6)


    sched.start()