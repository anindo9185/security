cipher = 'cz uczsdj qv lcf day vjqyq vdos ws kwz icwavgo ygsm sq zcm fqqy-lmd sq skd fgdzsz.jguqgjz qv zsjcafd dedasz kcy lm aqn zijdcy coo qedj skd vwdoy, lgs vjqyq nqgoy qaom zcm aqyqgls dedjmskwaf nwoo ld todcjdy gi wa skd uqjawaf. clqgs uwyawfks tcjjwcfdz tcud vqj skdwuiqjscas vqox. qad lm qad skdm jqoody cncm, vwoody nwsk vgoo lgs edjm gazcswzvwdykqllwsz. fcjydadjz tcud lm cjjcafdudas, cay jduqedy wa nkddo-lcjjqnz skqzd skcs kcywacyedjsdasom jducwady ldkway. awfks zoqnom'
all_freq = {}

for i in cipher:
	if i in all_freq:
		all_freq[i] += (1/len(cipher))*100
	else:
		all_freq[i] = (1/len(cipher))*100

print(len(cipher))


for x, y in sorted(all_freq.items()):
    print(x, "%0.3f" % y, '%')

res = 0
for i in all_freq.values():
    res = res+i

print(res)
