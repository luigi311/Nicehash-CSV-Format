import csv, os, argparse

from scripts.format.cointracking import *

def main():
    """
    Main function
    """

    # Create argparse for file and exchange
    parser = argparse.ArgumentParser(description='Cointracking')
    parser.add_argument('-f', '--file', help='File to read from', required=True)
    parser.add_argument('-e', '--exchange', help='Exchange to format to', required=True)

    args = parser.parse_args()
  
    # Check if file exists and is csv
    if not os.path.isfile(args.file):
        print("File does not exist")
        exit()
    
    if not args.file.endswith('.csv'):
        print("File is not a csv")
        exit()

    # Check if exchange is valid
    if args.exchange not in ['cointracking']:
        print("Exchange is not valid")
        exit()

    # Read file
    with open(args.file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)

    # Format data
    if args.exchange == 'cointracking':
        formatted_data = format_cointracking(data)
    else:
        print("Exchange is not valid")
        exit()

    # Write data to file
    output_file = args.file.replace('.csv', f'_{args.exchange}.csv')
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(formatted_data)

    print(f'Formatted data written to {output_file}')


if __name__ == "__main__":
    main()