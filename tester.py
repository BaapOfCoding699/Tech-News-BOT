import speedtest
def test_my_speed():
    st = speedtest.Speedtest()
    print("Finding the best server....")
    st.get_best_server()
    print("testing download speed......")
    download_speed = st.download()/1000000
    print("Testing upload speed.....")
    upload_speed = st.upload()/1000000
    ping = st.results.ping
    print(f"\n---Speed Test Result---")
    print(f"Download : {download_speed:.2f}mbps")
    print(f"Upload : {upload_speed:.2f}mbps")
    print(f"Ping : {ping} ms")
if __name__ == "__main__":
    test_my_speed()
