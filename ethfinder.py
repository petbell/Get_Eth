import csv, pandas as pd, numpy as np, secrets, time
from eth_account import Account

#function to create a private key and address then save them in a csv file.
def makeAccount():
	#create header for file
	header = ['privatekey', 'address']
	#create a 32 byte hexadecimal random number to start the iteration from
	private_key = secrets.token_hex(32)
	#private_key = priv
	
	rows_list  = []
	print("$tart")
	
	for i in range(1,10):
		
		acct = Account.from_key(private_key)
		#print( "Hex: ", private_key)
		#print ("address :", acct.address)
		#change the random hex number to int
		i = int(private_key, 16)
		i += 1
		#convert back to hexadecimal so as to continue the loop for next address
		private_key = hex(i)
		
		dict1 ={}
		dict1.update({"privatekey":  private_key, "address": acct.address.lower()} )
		rows_list.append(dict1)
		#print ("Done!")
		#print (rows_list)
	
	print ("Voila")	
	df = pd.DataFrame(rows_list)
	#print (df)
	with open ('pk.csv',  'w') as f:
		writer = df.to_csv (f)
		#writer.writerow(header)
		#writer.writerow(row)
#wb.save(filename = wb_name)
	print("finito, God no go shame us!!")
	
	dfArray = np.array(df["address"])
	
	print("Matching.......")
	for i in range(1,6):
		#Load eth balance csv file to pandas datafrane
		ethDf = pd.read_csv('Ethbal0' +str(i) + '.csv' , usecols = ["address"])
		ethDfArray = np.array(ethDf["address"])
		print(ethDfArray)
		print(type(ethDfArray))
	
		match = np.intersect1d(dfArray, ethDfArray)
		if match.size> 0:
			print(match.size)
			data = [match, filename]
			with open("results.csv", 'a') as file:
				writer = csv.writer(file)
				writer.writerow(data)
	
	
		
start = time.time()		
makeAccount()
end = time.time()
print( f" it took {end - start} seconds to finish")