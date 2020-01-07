from twitter import Twitter
import time

tw = Twitter()
def start():
    print("Starting...")
    dms = list()
    while True:
        if len(dms) is not 0:
            print(len(dms))
            for i in range(len(dms)):
                message = dms[i]['message']
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) is not 0 and len(message) <= 500:
                    if "https://" not in message and "http://" not in message:
                        if "[pic]" in message:
                            print("DM will be posting with media")
                            tw.post_tweet_with_media(message, dms[i]['media'])
                            tw.delete_dm(id)

                        elif "[sender]" in message:
                            message = message.replace("[sender]", "")
                            screen_name = tw.get_user_screen_name(sender_id)
                            media.download_image()
                            media.process_image(message, screen_name)
                            tw.post_tweet()
                            tw.delete_dm(id)

                        elif "[whisp]" in message:
                            # message = message.replace("[whisp]","")
                            print ("DM will post without image")
                            tw.post_tweet_text(message)
                            tw.delete_dm(id)

                        else:
                            media.download_image()
                            media.process_image(message, None)
                            tw.post_tweet()
                            tw.delete_dm(id)
                    else:
                        tw.delete_dm(id)
            dms = list()

        else:
            print("DM is empty")
            dms = tw.read_dm()
            if len(dms) is 0:
                time.sleep(60)

if __name__ == "__main__":
    start()
