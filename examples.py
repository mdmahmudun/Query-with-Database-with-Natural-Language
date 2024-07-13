examples = [
    {
        'Question': "how many companies laid of their more than 50% employees?",
        'SQLQuery': "SELECT COUNT(company) FROM layoffs_staging2 WHERE percentage_laid_off > 0.5",
        'SQLResult': "Result of the SQL query",
        'Answer': '164'
    },
    {
        'Question': "Which company had the highest layoffs?",
        'SQLQuery': "SELECT company, SUM(total_laid_off) company_total FROM layoffs_staging2 GROUP BY company ORDER BY 2 DESC LIMIT 1",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Amazon'
    },
    {
        'Question': "Find the highest number of layoffs in a single day by a single company",
        'SQLQuery': "SELECT MAX(total_laid_off) FROM layoffs_staging2",
        'SQLResult': "Result of the SQL query",
        'Answer': '12000'
    },
    {
        'Question': "Which industry had the highest layoffs?",
        'SQLQuery': "SELECT industry, SUM(total_laid_off) company_total FROM layoffs_staging2 GROUP BY industry ORDER BY 2 DESC LIMIT 1",
        'SQLResult': "Result of the SQL query",
        'Answer':'Consumer'
    },
    {
        'Question': "Which year has the most number of layoffs?",
        'SQLQuery': "SELECT YEAR(`date`), SUM(total_laid_off) FROM layoffs_staging2 GROUP BY YEAR(`date`) ORDER BY 2 DESC LIMIT 1",
        'SQLResult': "Result of the SQL query",
        'Answer': '2022'
    },
    
]