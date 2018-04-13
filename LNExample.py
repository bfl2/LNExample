import sys, funder, fundee

def main(argv):
    print("Executing %s" %(argv[0]))
    if(argv[1] == 'funder'):
        funder.execute()
    elif(argv[1] == 'fundee'):
        fundee.execute()

    return


if __name__ == "__main__":
    main(sys.argv)