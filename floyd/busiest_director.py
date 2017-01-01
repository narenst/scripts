"""
Read the IMDB data to identify the busiest directors
"""
import argparse
import csv
from collections import Counter


def main():
    parser = argparse.ArgumentParser(description="Parse input file")
    parser.add_argument('--input', dest='input_file', required=True)
    parser.add_argument('--number', type=int, required=True)
    parser.add_argument('--output', dest='output_file', required=True)

    args = parser.parse_args()

    director_movie_count = Counter()

    with open(args.input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            director_movie_count.update([row[1]])

    with open(args.output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["director", "total_movies"])
        for (director, count) in director_movie_count.most_common(args.number):
            if director and count:
                csvwriter.writerow([director, count])


if __name__ == '__main__':
    main()
