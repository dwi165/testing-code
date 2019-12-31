def hitung_state():
    kata = '00110001'
    jml_bit = len(kata)
    print kata
    print jml_bit
    #add = '{}'.format(kata[0:2])
    #print add
    tulis = []

    j = jml_bit-2
    print j
    for i in range (j):
    	add0 = kata [i:i+2]
    	#print add0
    	for k in range (j):
    		add1 = kata[i+1:i+3]
    	
    	state = add0 + " --> " + add1
    	tulis.append(state)
    	#print i,". ", state
    print tulis

    isi_tulis = len(tulis)
    print isi_tulis

    kotak = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    #int(kotak) = []

    for x in range (isi_tulis):
    	if (tulis[x] == "00 --> 00"):
    		kotak[0] += 1
    	elif (tulis[x] == "00 --> 01"):
    		kotak[1] += 1
    	elif (tulis[x] == "00 --> 10"):
    		kotak[2] += 1
    	elif (tulis[x] == "00 --> 11"):
    		kotak[3] += 1
    	elif (tulis[x] == "01 --> 00"):
    		kotak[4] += 1
    	elif (tulis[x] == "01 --> 01"):
    		kotak[5] += 1
    	elif (tulis[x] == "01 --> 10"):
    		kotak[6] += 1
    	elif (tulis[x] == "01 --> 11"):
    		kotak[7] += 1
    	elif (tulis[x] == "10 --> 00"):
    		kotak[8] += 1
    	elif (tulis[x] == "10 --> 01"):
    		kotak[9] += 1
    	elif (tulis[x] == "10 --> 10"):
    		kotak[10] += 1
    	elif (tulis[x] == "10 --> 11"):
    		kotak[11] += 1
    	elif (tulis[x] == "11 --> 00"):
    		kotak[12] += 1
    	elif (tulis[x] == "11 --> 01"):
    		kotak[13] += + 1
    	elif (tulis[x] == "11 --> 10"):
    		kotak[14] += 1
    	elif (tulis[x] == "11 --> 11"):
    		kotak[15] += 1
		
	print kotak

hitung_state()
