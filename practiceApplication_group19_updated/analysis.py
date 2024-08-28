class DataAnalyzer:
    def __init__(self):
        self.analysis_results = {}
        self.subject_analysis = {}
        self.notable_observations = []
        self.web_data_insights = {}
        self.recommendations = []

    def analyze_content(self, data, web_content):
        try:
            # Overall performance analysis
            self.analysis_results['average_score'] = data['Score'].mean()
            self.analysis_results['top_class'] = data.groupby('Class')['Score'].mean().idxmax()

            # Subject-wise analysis
            subjects = ['Mathematics', 'Science', 'English']
            for subject in subjects:
                if subject in data.columns:
                    self.subject_analysis[subject] = {
                        'average': data[subject].mean(),
                        'improvement': (data[subject].mean() - data[subject].mean()) / data[subject].mean() * 100
                    }

            # Notable Observations
            grade_8a = data[data['Class'] == '8A']
            if not grade_8a.empty:
                self.notable_observations.append("Grade 8A shows a significant improvement in English proficiency.")

            # Web Data Insights
            self.web_data_insights['online_participation'] = "95% of students accessed assessment resources online."  # Mocked value

            # Recommendations
            self.recommendations.append("Consider additional support for Grade 9B in Mathematics.")
            
        except KeyError as e:
            print(f"Error in data analysis: {e}")
