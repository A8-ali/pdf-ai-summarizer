from pdf_reader import read_pdf
from summarizer import summarize_text
from utils import save_text, generate_output_filename
from errors import PDFEmptyError, APIError


def main():
    try:
        path = input("PDF path: ")

        text = read_pdf(path)

        summary = summarize_text(text)

        output_file = generate_output_filename(path)

        save_text(summary, output_file)

        print(f"Summary saved to: {output_file}")

    except FileNotFoundError:
        print("Error: File not found")

    except PDFEmptyError:
        print("Error: PDF is empty")

    except APIError as err:
        print(f"API Error: {err}")

    except Exception as err:
        print(f"Unexpected Error: {err}")


if __name__ == "__main__":
    main()
