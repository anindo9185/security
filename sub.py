ltr = 'abcdefghijklmnopqrstuvwxyz '
key = 'wcnzmkhobrlxfuivtqajeygsdp '


def decrypt(message):
    result = ''

    for char in message:
        loc = key.find(char)
        result += ltr[loc]
    
    return result


cipher2 = 'cej amxziu, gobxm om zbz uij kiqhmj wfwqdx\'a gwqubuh, zbz uij jobul ik bj gbjo wudhqmwj zmhqmm ik niunmujqwjbiu. oba kiqjbmjo cbqjozwd nwfm wuz gmuj--gbjo jom eaewxvadnoixihbnwx cxig. kiqjd! om gwa uij dieuh wud xiuhmq. xbkm ui xiuhmq ajqmjnomz cmkiqmobf wa w ywaj eunowqjmz kbmxz, bja oiqbpiu xiaj bu jom zbajwunm. om owz cmmu iu jqwujiqkiq mbhoj dmwqa wuz jom jbfm owz vwaamz tebnlxd. wuijomq mbhoj dmwqa wuz om giexzcm umwqxd kbkjd. ixz whm giexz cm xiifbuh. wuz om owz uij mymu fwzm w zmnmujcmhbuubuh bu vadnoiobajiqd! dehi wfwqdx avilm cqbhojxd ik xwga wuz giqlmz iej obamtewjbiua cd fwlbuh zwqbuh waaefvjbiua cwamz iu bujebjbiu. cej oig niexz ium viaabcxd jmajjoiam waaefvjbiua? vadnoiobajiqd gwa uij dmj wu msvmqbfmujwx anbmunm. jom nifvxmjmajezd ik vadnoiobajiqd giexz qmtebqm msvmqbfmuja jowj giexz buyixym giqxza ik vmivxm,nmujeqbma ik jbfm--wuz w jijwx xwnl ik mjobnwx qmaviuabcbxbjd. bj viamz wu bfviaabcxmvqicxmf wuz om qmamujmz owybuh ji avmuz wud jbfm gowjmymq iu zmvwqjfmujwx jwala,ai om gwxlmz oifm wj jom muz ik jom zwd bu w fiqiam fiiz. iqzbuwqbxd om niexz wxgwdanieuj iu w gwxl joqieho jom nwfvea ji qieam oba avbqbja. ajqmmxbuh eubymqabjd gwa obho-zifmz wuz jom nwfvea hwym jom kmmxbuh ik cmbuh iej bu jom ivmu gbjoiej jom umnmaabjdik muzeqbuh jom lbuz ik gmwjomq om owz msvmqbmunmz iu oba ium(wuz iuxd) ybabj ji jombfvmqbwx vwxwnm. jomqm gmqm jqmma, xwgua, gwxla, wxfiaj wa joieho om gmqm iu jomnwfvea ik oba ixz nixxmhm iu oba oifm giqxz ik omxbniu. jom bxxeabiu ik nxiezbumaa owzcmmu wqqwuhmz kiq jom zwd gbjo jom aeuxbhoj(ui aeu, ik nieqam, reaj aeuxbhoj)wvvmwqbuh wuz zbawvvmwqbuh wj izz bujmqywxa. wuz bj gwa w xbjjxm niix, reaj w xbjjxm.bj ammfmz ji amxziu jowj jom niix zwda nwfm w xbjjxm fiqm kqmtemujxd jowu jomd eamz ji.gwa jqwujiq awybuh mumqhd? gwa bj bunqmwabuh bumkkbnbmund? iq(wuz om anigxmzbugwqzxd wa om joiehoj bj) gwa om hmjjbuh ixz wuz gwa oba cxiiz hmjjbuh jobu? om vxwnmzoba owuza bu'


print("Decrypted message:\n")
print(decrypt(cipher2), '\n')