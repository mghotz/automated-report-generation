# src/summarizer.py
from collections import Counter

def summarize_data(data, columns):
    summary = {}
    for column in columns:
        column_data = [row[column] for row in data if row[column] is not None]
        if not column_data:
            continue

        first_elem = column_data[0]
        if isinstance(first_elem, (int, float)):
            summary[column] = {
                'count': len(column_data),
                'mean': sum(column_data) / len(column_data) if column_data else 0,
                'min': min(column_data),
                'max': max(column_data)
            }
        elif isinstance(first_elem, str):
            most_common = Counter(column_data).most_common(1)[0]
            summary[column] = {
                'count': len(column_data),
                'most_common': most_common
            }
        elif isinstance(first_elem, bool):
            summary[column] = {
                'count': len(column_data),
                'true_count': sum(column_data),
                'false_count': len(column_data) - sum(column_data)
            }
        else:
            summary[column] = {
                'count': len(column_data),
                'type': str(type(first_elem))
            }
    
    summary_text = "\n".join([f"{col}: {info}" for col, info in summary.items()])
    return summary_text
