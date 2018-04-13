import sys, funder, fundee

def main(argv):
    print("Executing %s" %(argv[0]))
    if(len(argv) == 1):
        print("You must pass an argument, funder or fundee. Exiting")
    else:
        if(argv[1] == 'funder'):
            funder.execute()
        elif(argv[1] == 'fundee'):
            fundee.execute()

    return


if __name__ == "__main__":
    main(sys.argv)