


extracted_queue = []

grey_queue =[]

fram_1 = "fram 1"
fram_2 = "fram 2"
fram_3 = "fram 3"
fram_4 = "fram 4"
fram_5 = "fram 5"
print("\n\n\n")

extracted_queue.append(fram_1)
extracted_queue.append(fram_2)
extracted_queue.append(fram_3)
extracted_queue.append(fram_4)
extracted_queue.append(fram_5)

count = 0
fram_load = 50
#print( extracted_queue)
while count < fram_load:
    try:
        frame = extracted_queue.pop(0)

        print (f"turned fram {frame} grey")

        grey_queue.append(frame)

        #print(extracted_queue)
    except:
        print("No more frams to extract")
        break

print(extracted_queue)

print("\n\n\n")