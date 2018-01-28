meeting_1 = (1,3)
meeting_2 = (2,4)
meeting_3 = (4,8)
meeting_4 = (10,12)
meeting_5 = (9,10)
alist=[]
alist.append(meeting_1)
alist.append(meeting_2)


def merge_ranges(alist):
    merged_list = []
    alist.sort() # O(n log n) not quite O(n) but better than quadratic :P
    #if we wanted to sort via second value:
    # sorted(alist,key = lambda x:x[1])
    merged_list = [alist[0]]

    for current_start, current_end in alist[1:]:
        last_merged_start, last_merged_end = merged_list[-1]

        try:
            if (current_start <= last_merged_end):
                merged_list[-1] = (last_merged_start,max(last_merged_end,current_end))
            else:
                merged_list.append((current_start,current_end))
        except IndexError:
            print ("meh")
    print (merged_list)


def main():
    merge_ranges(alist)

if __name__ == "__main__":
    main()