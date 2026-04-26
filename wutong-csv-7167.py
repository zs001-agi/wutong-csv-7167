import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='CSV Viewer/Filter/Sort/Merge Tool')
    parser.add_argument('file', type=str, help='Input CSV file')
    parser.add_argument('--json', action='store_true', help='Output in JSON format')
    parser.add_argument('--output', type=str, help='Output file name')
    parser.add_argument('--filter', type=str, help='Filter rows using pandas query syntax')
    parser.add_argument('--sort', type=str, nargs='+', help='Sort by columns')
    parser.add_argument('--merge', type=str, nargs='+', help='Merge with other CSV files')

    args = parser.parse_args()

    try:
        df = pd.read_csv(args.file)

        if args.filter:
            df = df.query(args.filter)

        if args.sort:
            df = df.sort_values(by=args.sort)

        if args.merge:
            for merge_file in args.merge:
                other_df = pd.read_csv(merge_file)
                df = pd.concat([df, other_df], ignore_index=True)

        if args.json:
            output = df.to_json(orient='records', lines=True)
        else:
            output = df.to_csv(index=False)

        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
        else:
            print(output)

    except Exception as e:
        parser.error(f'Error: {e}')

if __name__ == '__main__':
    main()