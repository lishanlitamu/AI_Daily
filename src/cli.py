import argparse
from .utils import extract_pdf_pages

def main():
    parser = argparse.ArgumentParser(description='AI Daily CLI Tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Create the parser for the "run" command
    run_parser = subparsers.add_parser('run', help='Run AI Daily operations')
    
    # Add PDF break options
    run_parser.add_argument('--break-pdf', action='store_true', help='Extract pages from PDF')
    run_parser.add_argument('--in', dest='input_path', help='Input PDF file path')
    run_parser.add_argument('--out', dest='output_path', help='Output PDF file path')
    run_parser.add_argument('--sp', dest='start_page', type=int, help='Start page number')
    run_parser.add_argument('--ep', dest='end_page', type=int, help='End page number')
    
    args = parser.parse_args()
    
    if args.command == 'run':
        if args.break_pdf:
            if not all([args.input_path, args.output_path, args.start_page, args.end_page]):
                parser.error("--break-pdf requires --in, --out, --sp, and --ep arguments")
            
            try:
                extract_pdf_pages(
                    input_path=args.input_path,
                    output_path=args.output_path,
                    start_page=args.start_page,
                    end_page=args.end_page
                )
                print(f"Successfully extracted pages {args.start_page}-{args.end_page} from {args.input_path} to {args.output_path}")
            except Exception as e:
                print(f"Error: {str(e)}")
        else:
            parser.error("No operation specified. Use --break-pdf to extract PDF pages")
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 