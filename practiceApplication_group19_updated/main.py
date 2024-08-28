from data_processing import DataProcessor
from web_data_retrieval import WebDataRetriever
from analysis import DataAnalyzer
from summary_generator import SummaryGenerator
from custom_exceptions import DatabaseConnectionError

def main():
    try:
        # Initialize classes
        processor = DataProcessor()
        retriever = WebDataRetriever()
        analyzer = DataAnalyzer()
        summarizer = SummaryGenerator()

        while True:
            print("\nSchool Assessment Data Analysis")
            print("1. Input new assessment data")
            print("2. View current assessment data")
            print("3. Analyze and generate summary")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                input_assessment_data(processor)
            elif choice == '2':
                view_current_data(processor)
            elif choice == '3':
                generate_summary(processor, retriever, analyzer, summarizer)
            elif choice == '4':
                break
            else:
                print("Invalid option, please try again.")

    except DatabaseConnectionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def input_assessment_data(processor):
    student = input("Enter student name: ")
    student_class = input("Enter class (e.g., 10A): ")
    math_score = float(input("Enter Mathematics score: "))
    science_score = float(input("Enter Science score: "))
    english_score = float(input("Enter English score: "))

    new_data = {
        'Student': student,
        'Class': student_class,
        'Mathematics': math_score,
        'Science': science_score,
        'English': english_score,
        'Score': (math_score + science_score + english_score) / 3
    }

    processor.add_data(new_data)

def view_current_data(processor):
    if processor.data.empty:
        print("No data available.")
    else:
        print("\nCurrent Assessment Data:")
        print(processor.data)

def generate_summary(processor, retriever, analyzer, summarizer):
    web_url = input("Enter the school webpage URL for additional data: ")
    web_content = retriever.fetch_web_data(web_url)

    analyzer.analyze_content(processor.data, web_content)
    summary = summarizer.generate_summary(analyzer)
    print("\n" + summary)

if __name__ == "__main__":
    main()
