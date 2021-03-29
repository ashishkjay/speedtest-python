import schedule
import time
import speedtest
import requests

URL = "http://localhost:3000/api/hello"

def job():
    try:
        st = speedtest.Speedtest()
        download = str(st.download()/1000000)
        upload =  str(st.upload()/1000000)
        print("Download: "  + download)
        print("Upload: "  + upload)
        servernames =[]
        st.get_servers(servernames)
        ping = st.results.ping
        print(ping)
        PARAMS = {
            'download': download,
            'upload': upload,
            'ping': ping
        }
        requests.post(url=URL,params=PARAMS)
    except:
        print("No internet connection")


schedule.every(10).seconds.do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)

