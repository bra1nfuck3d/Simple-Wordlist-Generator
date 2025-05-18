import os
import sys
import argparse


base_command_cewl = "./CeWL/cewl.rb"
base_command = "python bopscrk/bopscrk/bopscrk.py "

parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",help="the url to scrape words from",required=True)
parser.add_argument("-o","--output",help="path to save the url word scrape",required=True)
parser.add_argument("-w","--write",help="path to write the wordlist")
parser.add_argument("combos",help="number of combinations to make, the more the more computing power it will need",nargs="?",default=2)
args = parser.parse_args()

if len(sys.argv)<2:
    parser.print_help()
    quit()


def run_main():
    os.system(base_command_cewl+" "+args.url+" -o"+" -w "+args.output)
    try:
        files = open(args.output)
    except:
        print("[!] Wordlist file provided not accesible")
        quit()
    file_reading = files.read()
    ffixed = file_reading.replace("\n",",")
    os.system(base_command+"-w "+ffixed+" -o "+args.write+" -n "+str(args.combos)+" --min 1 -c -l")


run_main()