import argparse
import csv
from pathlib import Path
import sys

import youtube_dl
from youtube_dl.options import parseOpts

def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"csvfile",
		type=Path,
		help="The music-library-songs.csv file from Google Takeout")
	args, remaining = parser.parse_known_args()

	urls = []
	with open(args.csvfile) as csvfile:
		library_reader = csv.reader(csvfile, delimiter=",", quotechar="\"")
		seen_header = False
		for row in library_reader:
			if seen_header:
				urls.append(row[0])
			if row[0] == "Song URL":
				seen_header = True
		if not seen_header:
			print("Failed to find CSV header, is this a Google Takeout CSV file?")
			sys.exit(1)

	argv = remaining + urls
	youtube_dl.main(argv=argv)
