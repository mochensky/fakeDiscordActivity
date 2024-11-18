import pypresence, time, random

rpcId = 1274102042691895369
rpcState = f"Cruising around Slave Beach ({random.randint(300, 500)} / 1700)"
rpcDetails = "NEXTRP / Server 23"
rpcLargeImage = "largeimage"
rpcLargeText = "NEXTRP"
rpcSmallImage = None
rpcSmallText = None
rpcTime = time.time()

rpcStateOptions = [
    f"Cruising around Slave Beach",
    f"Exploring the Red County",
    f"Walking around Flint County",
    f"Swims in Bone County"
]

rpc = pypresence.Presence(rpcId)
rpc.connect()

print(f"Connected")

start_time = input("Введите время начала игры (в формате ЧЧ:ММ): ")
if start_time:
    hours, minutes = map(int, start_time.split(':'))
    rpcTime = time.time() - (hours * 3600 + minutes * 60)

while True:
    rpcUpdateDelay = random.randint(100, 160)
    rpcState = f"{random.choice(rpcStateOptions)} ({random.randint(450, 460)} / 1700)"
    print(f"Updated {rpcState}")
    rpc.update(state=rpcState, details=rpcDetails, start=rpcTime, large_image=rpcLargeImage, large_text=rpcLargeText, small_image=rpcSmallImage, small_text=rpcSmallText)
    time.sleep(rpcUpdateDelay)