class SummaryGenerator:
    def generate_summary(self, analyzer):
        summary = "School Assessment Summary Report:\n\n"

        summary += f"1. Overall Performance of Student A:\n"
        summary += f"   - Average score: {analyzer.analysis_results['average_score']:.2f}\n"
        summary += f"   - Top-performing class: {analyzer.analysis_results['top_class']}\n\n"

        summary += "2. Subject-wise Analysis:\n"
        for subject, analysis in analyzer.subject_analysis.items():
            summary += f"   - {subject}: Improved by {analysis['improvement']:.1f}% compared to the last assessment.\n"

        summary += "\n3. Notable Observations:\n"
        for observation in analyzer.notable_observations:
            summary += f"   - {observation}\n"

        summary += "\n4. Web Data Insights:\n"
        for insight in analyzer.web_data_insights.values():
            summary += f"   - {insight}\n"

        summary += "\n5. Recommendations:\n"
        for recommendation in analyzer.recommendations:
            summary += f"   - {recommendation}\n"

        return summary
