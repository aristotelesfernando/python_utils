# pip install speedtest-cli
import speedtest as sp

test = sp.Speedtest()

down = test.download()
rsDown = round(down)
fDown = int(rsDown / 1e+6)

upload = test.upload()
rsUp = round(upload)
fUp = int(rsUp / 1e+6)

print(f"Velocidade de Download: {fDown} mb/s")
print(f"Velocidade de Upload: {fUp} mb/s")
